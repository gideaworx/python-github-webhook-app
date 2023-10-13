#!/usr/bin/env python3

from pathlib import Path
from github_webhook_app.generator_utils import load_webhooks, load_components

def main():
  schema_dir = Path(__file__, "..", "..", "schemas")
  webhooks = load_webhooks(schema_dir)
  components = load_components(schema_dir)