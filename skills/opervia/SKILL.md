---
name: opervia
description: Validate and deliver an Opervia Service Compliance API ticket from repository evidence through implementation, testing, review, and local commits. Use when a team member supplies a sprint ticket ID or asks for readiness, dependency, or progress analysis of the Java/Spring API.
---

# Opervia ticket delivery

Work from a ticket in the currently open Service Compliance API repository. Keep every conclusion traceable to repository evidence. This skill covers the Java/Spring API; mobile work is limited to verifying or defining an agreed API contract.

## Load the relevant guidance

Read these references before acting:

- [Project context and evidence rules](references/project-context.md) for every request.
- [Ticket workflow](references/ticket-workflow.md) when validating or delivering a ticket.
- [Backend conventions](references/backend-conventions.md) before planning, editing, testing, or reviewing Java/API work.
- [Git workflow](references/git-workflow.md) before creating a branch, staging, or committing.

## Start from evidence

1. Inspect repository instructions, `git status`, the current branch, remotes, recent commits, build configuration, and relevant implementation.
2. Locate the exact ticket ID in tracked project files. Prefer `docs/sprints/<sprint>/tickets/<ticket>.md`. If several documents define it, identify the conflict instead of choosing silently.
3. Trace its parent story, acceptance criteria, dependencies, contracts, and current code. Planned architecture and prior sprint prose do not prove implementation.
4. Classify readiness as `READY`, `PARTIAL`, `BLOCKED`, or `INSUFFICIENT`, citing paths, symbols, tests, branches, or commit IDs that support the result.

Do not invent a missing ticket, endpoint, field, business rule, dependency status, assignee, test result, or contribution. Label statements as verified fact, documented decision, working assumption, or unknown when the distinction matters.

## Execute the requested mode

- **Readiness or status:** inspect and report; do not edit, branch, or commit.
- **Plan:** produce work slices tied to acceptance criteria; do not implement unless the user also requests execution.
- **Deliver:** complete the enabled slices through implementation, tests, review, and local commits when commits are explicitly requested.
- **Resume:** re-read the ticket, Git history, working tree, and validation evidence. Do not trust stale progress notes over current code.

When a dependency is missing, continue only with independent work or against an approved contract. A fake, stub, or mock can validate the consumer against that contract, but cannot prove real integration. If no approved contract exists, stop the affected slice and state the smallest decision or merged capability required to resume.

## Maintain the handoff

Report the readiness classification, work completed, acceptance criteria covered, checks actually run, commits created, remaining risks, and dependency state. Distinguish local implementation, committed work, reviewed work, merged work, deployed work, and verified production behavior.

Never attribute work to a teammate without evidence. Never mark a story or ticket complete merely because code exists; all acceptance criteria and required dependencies must have current verification.
