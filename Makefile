CMD_NOT_FOUND = $(error $(1) is required for this rule)
CHECK_CMD = $(if $(shell command -v $(1)),,$(call CMD_NOT_FOUND,$(1)))
REQUIREMENTS := python3 pip3 curl jq
$(foreach req,$(REQUIREMENTS),$(call CHECK_CMD,$(req)))

GITHUB_API_VERSION := v2.1.0

.PHONY: clean
clean: clean-generated-models clean-generated-decorators
	rm -fr dist

.PHONY: clean-generated-models
clean-generated-models:
	rm -fr github_webhook_app/models/__init__.py

.PHONY: clean-generated-decorators
clean-generated-decorators:
	rm -f github_webhook_app/__init__.py

.PHONY: generate-models
generate-models: github_webhook_app/models/__init__.py

github_webhook_app/models/__init__.py: .venv/bin/activate 
	. .venv/bin/activate
	@echo "Generating webhook models..."
	@curl -fsSL "https://raw.githubusercontent.com/github/rest-api-description/$(GITHUB_API_VERSION)/descriptions/api.github.com/api.github.com.json" | \
		python3 -mgenerate models

.PHONY: generate-decorators
generate-decorators: github_webhook_app/__init__.py

github_webhook_app/__init__.py: .venv/bin/activate
	. .venv/bin/activate
	@echo "Generating webhook decorators..."
	@curl -fsSL "https://raw.githubusercontent.com/github/rest-api-description/$(GITHUB_API_VERSION)/descriptions/api.github.com/api.github.com.json" | \
		python3 -mgenerate decorators

.PHONY: generate
generate: generate-models generate-decorators

.PHONY: regenerate
regenerate: clean generate

.PHONY: regenerate-models
regenerate-models: clean-generated-models generate-models

.PHONY: regenerate-decorators
regenerate-decorators: clean-generated-decorators generate-decorators

.venv/bin/activate:
	python3 -m venv .venv

.venv/bin/poetry:
	pip3 install poetry

.venv/bin/datamodel-codegen: .venv/bin/poetry
	.venv/bin/poetry install

PHONY: publish
publish: .venv/bin/activate .venv/bin/poetry
	. .venv/bin/activate
	rm -fr dist/
	.venv/bin/poetry publish --build

PHONY: test
test:
	python3 -m generate