# Service Compliance API conventions

## Architecture

Preserve the modular monolith. Organize behavior by business context under `com.api.servicecompliance.<context>` and follow the repository's established layers:

- `domain` for business concepts and repository contracts;
- `application` for use-case orchestration;
- `interfaces.rest` for HTTP controllers and request/response mapping;
- `infrastructure` for security, persistence and external integrations;
- `shared` only for concepts that are genuinely shared across contexts.

Do not introduce a new service, framework, architectural pattern or broad refactor unless the ticket requires it. When existing code differs from the target design, change only the boundary needed by the ticket and document a material architectural decision.

## Java and HTTP

- Use Java 17 and the Gradle Wrapper versions declared by the repository.
- Use `PascalCase` types, `camelCase` members, `UPPER_SNAKE_CASE` constants and lowercase packages.
- Keep technical identifiers and API resources in English.
- Keep controllers focused on HTTP concerns and application services focused on use-case coordination.
- Validate requests at the boundary and express domain failures through the established exception mapping.
- Preserve `/api/v1` compatibility unless the ticket explicitly defines a breaking change or a new version.
- Use resource nouns, appropriate HTTP status codes and the existing `ApiError` shape.
- Enforce authorization for the relevant role and test both permitted and forbidden behavior.

## Data and integrations

- Change PostgreSQL schemas only through a new, immutable Flyway migration. Never edit a migration already applied outside a disposable local environment.
- Keep JPA mappings, migration definitions and API serialization consistent.
- Never commit credentials, tokens, local secrets or production data.
- Treat mobile apps, Firebase and object storage as external boundaries. Do not claim integration until exercised against the real boundary or an explicitly identified test environment.

## Verification

Choose tests based on the behavior changed:

- unit tests for domain rules and pure transformations;
- application tests for orchestration and failure behavior;
- integration tests for HTTP, security, persistence, migrations and serialization;
- end-to-end tests for the smallest critical user flows.

Use `./gradlew` on Unix-like systems and `gradlew.bat` on Windows. Run focused tests during a slice and the relevant broader suite before handoff. Report the command and result; never translate an unrun or skipped check into a pass.
