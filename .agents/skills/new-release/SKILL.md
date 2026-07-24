---
name: new-release
description: >-
  Cut a full Faker release: prepare the branch, bump the version, run make
  release, and push. Use when cutting a new release or when the user asks for
  a new-release.
disable-model-invocation: true
---

# New Release

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Follow prepare-release
- [ ] Infer version bump part; wait for confirmation
- [ ] Activate .venv-3.11 and bumpversion
- [ ] Wait for confirmation, then make release
- [ ] Push the repo
```

1. Follow the [prepare-release](../prepare-release/SKILL.md) skill.
2. By looking at the `VERSION` file and the latest entry in `CHANGELOG.md`, infer which part of the version needs to be incremented.
3. **Wait for confirmation about which part to bump before proceeding further.**
4. Activate the Python virtual environment in `.venv-3.11`. If the environment doesn't exist, create it and install dependencies from `dev-requirements.txt`.
5. Bump the version with `bumpversion <PART>` (e.g. `bumpversion minor`).
6. **Wait for confirmation to run `make release` before proceeding further.**
7. Run `make release`.
8. Push the repo.
