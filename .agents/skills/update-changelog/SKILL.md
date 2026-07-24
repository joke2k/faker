---
name: update-changelog
description: >-
  Update CHANGELOG.md with commits since the latest version. Use when preparing
  a release, updating the changelog, or when the user asks to update CHANGELOG.md.
disable-model-invocation: true
---

# Update Changelog

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Ensure you are on the master branch
- [ ] Draft CHANGELOG.md entry and wait for confirmation
- [ ] Commit with message: 📝 Update CHANGELOG.md
- [ ] Push the repo
```

### Draft the entry

1. Ensure you are on the `master` branch.
2. Update `CHANGELOG.md` with a new entry:
   - Use today's date.
   - For the entry description, use the git commit subjects since the latest version increment.
   - Exclude commits that are just linting code.
   - Exclude commits whose subjects start with `:lipstick:` or `💄`.
   - Increment the **MINOR** number.
   - Thank the original author by their GitHub username (link to their GitHub profile), not their first name.
   - Use existing entries as examples.
3. **Wait for confirmation before committing or pushing.**
4. Commit the change with the message `📝 Update CHANGELOG.md`.
5. Push the repo.
