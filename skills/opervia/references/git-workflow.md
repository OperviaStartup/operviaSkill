# Opervia Git workflow

## Before changing Git state

Inspect the working tree, current branch, available `main` and `develop` branches, remotes, recent commit style and repository instructions. Preserve unrelated changes and never stage them with the ticket.

The team workflow uses:

- `main` for stable releases;
- `develop` for integrated development;
- `feature/<ticket>-<short-description>` for new behavior;
- `fix/<ticket>-<short-description>` for corrections;
- `docs/<ticket>-<short-description>` for documentation-only work;
- `chore/<ticket>-<short-description>` for maintenance;
- `release/<version>` and `hotfix/<version>-<description>` when a real release requires them.

Use lowercase kebab-case after the ticket ID. Start ordinary ticket branches from the verified `develop` base. If `develop` does not exist, report that Git Flow has not been bootstrapped; do not pretend a branch from `main` followed this policy.

## Commits

Use Conventional Commits:

```text
<type>(<scope>): <imperative summary>

[reason or material trade-off]

Refs: <ticket-id>
```

Prefer `feat`, `fix`, `docs`, `test`, `chore`, `refactor`, `build` or `ci` according to the actual change. Each commit must represent one coherent, reviewable advance and pass the relevant focused checks. Do not manufacture a commit per file or mix unrelated cleanup into a ticket commit.

Before committing, review the staged diff and run `git diff --cached --check`. A request for separated commits authorizes local commits for the ticket; it does not authorize push, pull, PR creation, merge, tagging, deployment or history rewriting unless the user also requests those operations.

Never use force-push, destructive reset, clean, published-history rewriting or branch deletion without explicit authorization for that exact operation.
