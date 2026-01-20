# Guidelines for AI Agents - France Travail API

This document outlines coding standards and repository interaction guidelines for AI agents working on the {{cookiecutter.project_name}} project.

Work exclusively in [TDD](.ai/docs/rules/tdd.md).

## Standards
Detailed rules in [`.ai/rules/`](.ai/rules/):
- **Clean code:** [`.ai/rules/clean-code.md`](.ai/rules/clean-code.md)
- **Naming:** [`.ai/rules/naming-conventions.md`](.ai/rules/naming-conventions.md)
- **Testing:** [`.ai/rules/testing-standards.md`](.ai/rules/testing-standards.md), [`.ai/rules/testing-unit.md`](.ai/rules/testing-unit.md), [`.ai/rules/testing-integration.md`](.ai/rules/testing-integration.md)
- **TDD:** [`.ai/rules/tdd.md`](.ai/rules/tdd.md)
- **Debugging:** [`.ai/rules/debug.md`](.ai/rules/debug.md)

## Repository Interaction

- Use the provided `Makefile` commands to interact with the repository. All commands use `uv` for dependency management.
