CMD_NOT_FOUND = $(error $(1) is required for this rule)
CHECK_CMD = $(if $(shell command -v $(1)),,$(call CMD_NOT_FOUND,$(1)))
REQUIREMENTS := python3 pip3 curl jq
$(foreach req,$(REQUIREMENTS),$(call CHECK_CMD,$(req)))

GITHUB_API_VERSION := v2.1.0

.PHONY: clean
clean: clean-generated-models clean-generated-decorators

.PHONY: clean-generated-models
clean-generated-models:
	rm -fr github_webhook_app/models/generated/*

.PHONY: clean-generated-decorators
clean-generated-decorators:
	rm -f github_webhook_app/decorators/events/__generated.py

.PHONY: generate-models
generate-models: github_webhook_app/models/generated/__init__.py

github_webhook_app/models/generated/__init__.py: .venv/bin/activate .venv/bin/datamodel-codegen
	. .venv/bin/activate
	@echo "Generating webhook modules..."
	@.venv/bin/datamodel-codegen \
		--url "https://raw.githubusercontent.com/github/rest-api-description/$(GITHUB_API_VERSION)/descriptions/api.github.com/api.github.com.json" \
		--output github_webhook_app/models/generated/__init__.py --target-python-version 3.11 \
		--use-annotated --use-generic-container-types --use-union-operator \
		--use-unique-items-as-set --use-field-description --use-schema-description \
		--use-double-quotes --collapse-root-models >/dev/null 2>&1

.PHONY: generate-decorators
generate-decorators: github_webhook_app/decorators/events/__generated.py

github_webhook_app/decorators/events/__generated.py: .venv/bin/activate
	. .venv/bin/activate
	@echo "Generating webhook decorators..."
	@curl -fsSL "https://raw.githubusercontent.com/github/rest-api-description/$(GITHUB_API_VERSION)/descriptions/api.github.com/api.github.com.json" | \
		jq -r '.["x-webhooks"]' | python3 -m "github_webhook_app.decorators.events.generate" >/dev/null 2>&1

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