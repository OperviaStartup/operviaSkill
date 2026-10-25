# Ticket workflow

## Ticket source

Prefer versioned tickets at:

```text
docs/sprints/<sprint>/tickets/<ticket-id>.md
```

The sprint index should link tickets and summarize status; the ticket owns its details. Trello exports and the academic report are supporting sources, not replacements for a current execution ticket.

If the repository uses another documented location, preserve it. Search for the exact ticket ID before concluding it is missing.

## Minimum ticket contract

A ticket ready for implementation identifies:

- ticket ID, type, parent story and sprint;
- objective, in-scope behavior and explicit exclusions;
- measurable acceptance criteria;
- dependencies with the required state or contract;
- affected API or data contracts;
- verification expected for completion;
- assignee only when the team has recorded one.

Use [the ticket template](../assets/ticket-template.md) when the team creates or normalizes tickets. Do not add guessed values to satisfy the template.

## Readiness classification

- `READY`: requirements and contracts are actionable, and required dependencies are available in the working base.
- `PARTIAL`: at least one independent slice is actionable, while named slices remain blocked.
- `BLOCKED`: a required dependency, contract or decision prevents meaningful implementation.
- `INSUFFICIENT`: the ticket cannot be evaluated because essential scope or acceptance evidence is missing or contradictory.

A dependency marked done in a document must still be verified in the current base. Work on another branch is available only after the user selects that branch as the integration base or it is merged into the current base.

## Delivery loop

1. Map each acceptance criterion to one or more implementation slices and checks.
2. Put dependency or uncertainty reduction before dependent functionality.
3. Implement the smallest coherent slice and add the tests needed to demonstrate its behavior.
4. Run focused checks, review the diff, then commit the slice if local commits were requested.
5. Repeat until enabled criteria are covered or evidence reveals a blocker.
6. Run the relevant broader Gradle verification and review all ticket commits together.

If a fix changes behavior already tested or reviewed, invalidate the affected evidence and rerun it. A ticket reaches `DONE` only when its acceptance criteria, dependencies, checks, review and required integration state are satisfied under the team's definition of done.

## Progress record

Keep durable progress in the versioned ticket when the repository adopts that practice. Record only compact facts: current status, completed criteria, commit IDs, verification results, blockers and next action. Avoid a conversational diary or claims that cannot be reconstructed from Git and CI.
