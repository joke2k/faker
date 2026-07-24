---
name: prepare-release
description: >-
  Prepare the master branch for a release: pull, lint, commit lint fixes, then
  update the changelog. Use when preparing a release or when the user asks to
  prepare-release.
disable-model-invocation: true
---

# Prepare Release

## Workflow

1. Checkout the `master` branch and pull the repo.
2. Activate the Python virtual environment in `.venv-3.11`. If the environment doesn't exist, create it and install dependencies from `dev-requirements.txt`.
3. Run `make lint`. Ignore its results.
4. Use `git diff` to check if there are any changes. If so, commit them with the message `:lipstick: Lint code` and push.
5. Follow the [update-changelog](../update-changelog/SKILL.md) skill.
