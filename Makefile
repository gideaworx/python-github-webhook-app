CMD_NOT_FOUND = $(error $(1) is required for this rule)
CHECK_CMD = $(if $(shell command -v $(1)),,$(call CMD_NOT_FOUND,$(1)))
REQUIREMENTS := python3 pip3
$(foreach req,$(REQUIREMENTS),$(call CHECK_CMD,$(req)))

GITHUB_API_VERSION := v2.1.0

.PHONY: generate-models clean
clean:
	rm -fr github_webhook_app/models/generated/*

generate-models: github_webhook_app/models/generated/__init__.py

github_webhook_app/models/generated/__init__.py: .venv/bin/activate .venv/bin/datamodel-codegen
	. .venv/bin/activate
	.venv/bin/datamodel-codegen \
		--url "https://raw.githubusercontent.com/github/rest-api-description/$(GITHUB_API_VERSION)/descriptions/api.github.com/api.github.com.json" \
		--output github_webhook_app/models/generated/__init__.py --target-python-version 3.11 \
		--use-annotated --use-generic-container-types --use-union-operator \
		--use-unique-items-as-set --use-field-description --use-schema-description \
		--use-double-quotes --collapse-root-models

.venv/bin/activate:
	python3 -m venv .venv

.venv/bin/poetry:
	pip3 install poetry

.venv/bin/datamodel-codegen: .venv/bin/poetry
	.venv/bin/poetry install