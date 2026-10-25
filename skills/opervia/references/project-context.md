# Opervia project context and evidence rules

## Confirmed baseline

Service Compliance is an academic Opervia project for traceability of outsourced cleaning-service compliance. The current backend is a modular monolith in the `serviceComplianceAPI` repository.

The verified v1 baseline at the time this skill was authored includes:

- Java 17, Spring Boot 4.1.1 and Gradle Wrapper;
- Spring MVC, Security, Validation and Data JPA;
- PostgreSQL with Flyway migrations;
- JWT authentication and role authorization;
- OpenAPI/Swagger documentation;
- modules for authentication, obligations, executions and shared concerns;
- endpoints under `/api/v1` for authentication, obligations, executions and evidence.

Treat this list as orientation, not proof that a checkout still has those capabilities. Recheck `build.gradle`, source code, migrations, tests and Git history on every ticket.

The academic design also describes future bounded contexts for Identity & Access, Service Planning, Field Operations, Compliance Management, and Reporting & Follow-up. A diagram or report section is a target design unless code and tests demonstrate it is implemented.

## Evidence precedence

Use the most specific, current, accepted source:

1. explicit user direction for the current task;
2. repository-level agent instructions and the exact sprint ticket;
3. accepted API contracts and architecture decisions;
4. current code, migrations, tests and Git state;
5. project report and older sprint evidence;
6. assumptions, which must be labeled and must not decide material product behavior.

When sources disagree, report the disagreement and its impact. Do not silently rewrite the ticket or code to make them appear consistent.

## Anti-hallucination rules

- Cite file paths, symbols, commands, test output or commit IDs for implementation claims.
- Say `unknown` when evidence is unavailable. Do not fill gaps with a plausible design.
- A planned user story is not implemented. A local branch is not integrated. A passing mock test is not a passing integration.
- Do not claim that a teammate authored code from a planning assignment or report table.
- Never fabricate screenshots, interviews, measurements, deployments, test runs or academic evidence.
- Do not infer that every item assigned to a sprint was delivered.

## Scope boundary

This version implements and reviews the Java/Spring API. Kotlin Android or other mobile clients may be considered only as consumers of a documented API contract. Do not create mobile code unless a future version of the skill explicitly adds its repository and conventions.
