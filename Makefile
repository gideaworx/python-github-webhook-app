CMD_NOT_FOUND = $(error $(1) is required for this rule)
CHECK_CMD = $(if $(shell command -v $(1)),,$(call CMD_NOT_FOUND,$(1)))
REQUIREMENTS := jq curl python3
$(foreach req,$(REQUIREMENTS),$(call CHECK_CMD,$(req)))

schemas/api.github.com.json:
	curl -o schemas/api.github.com.json \
		"https://raw.githubusercontent.com/github/rest-api-description/v2.1.0/descriptions/api.github.com/api.github.com.json"

schemas/webhooks.json: schemas/api.github.com.json
	jq '.["x-webhooks"]' < schemas/api.github.com.json > schemas/webhooks.json

schemas/components.json: schemas/api.github.com.json
	jq '.components.schemas' < schemas/api.github.com.json > schemas/components.json

.PHONY: update-schemas
update-schemas: schemas/webhooks.json schemas/components.json

.PHONY: generate generate-models generate-decorators

generate: generate-models generate-decorators

generate-models: schemas/webhooks.json schemas/components.json
	$(shell ./bin/generate-models.py)

generate-decorators: schemas/webhooks.json schemas/components.json
	$(shell ./bin/generate-decorators.py)

