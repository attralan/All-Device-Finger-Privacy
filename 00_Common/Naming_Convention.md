# Git Commit Convention

## Purpose

This document defines the Git commit message rules for the Fingerprint-Laptop-Unlock-System project.

Both Android and Laptop development must follow the same commit style to keep the project history clear and understandable.

---

# Commit Message Format

Use the following format:

```
type: description
```

Example:

```
feat: add authentication server
```

---

# Commit Types

## feat - New Feature

Use when adding a new feature or module.

Format:

```
feat: add <feature_name>
```

Examples:

```
feat: add communication server

feat: add authentication manager

feat: add biometric authentication

feat: add encryption module
```

---

## fix - Bug Fix

Use when fixing an error or issue.

Format:

```
fix: solve <problem>
```

Examples:

```
fix: solve socket connection error

fix: solve authentication validation issue

fix: solve database connection error
```

---

## docs - Documentation

Use when changing documentation files.

Format:

```
docs: update <document_name>
```

Examples:

```
docs: update communication protocol

docs: update project architecture

docs: add README documentation
```

---

## refactor - Code Improvement

Use when improving code structure without changing functionality.

Format:

```
refactor: improve <module_name>
```

Examples:

```
refactor: improve authentication service structure

refactor: simplify communication layer
```

---

## test - Testing

Use when adding or modifying test cases.

Format:

```
test: add <test_name>
```

Examples:

```
test: add authentication test cases

test: add server connection tests

test: update security tests
```

---

## config - Configuration Changes

Use when changing configuration files.

Format:

```
config: update <configuration_name>
```

Examples:

```
config: update python dependencies

config: update application settings

config: add database configuration
```

---

## security - Security Changes

Use for security-related features or improvements.

Format:

```
security: add <security_feature>
```

Examples:

```
security: add encryption support

security: improve token verification

security: add replay protection
```

---

## integration - Integration Changes

Use when connecting Android and Laptop modules.

Format:

```
integration: connect <modules>
```

Examples:

```
integration: connect android and laptop communication

integration: test authentication workflow
```

---

# Commit Message Rules

## 1. Use lowercase after commit type

Correct:

```
feat: add communication server
```

Incorrect:

```
Feat: Add Communication Server
```

---

## 2. Keep messages short and meaningful

Recommended length:

```
50-72 characters
```

---

## 3. One commit should contain one logical change

Correct:

```
feat: add socket communication server
```

Incorrect:

```
feat: add server database encryption and fix bugs
```

---

## 4. Avoid unclear commit messages

Do not use:

```
update code

changes

final

test

working

new
```

Use specific descriptions.

---

# Branch Naming

## Main Branch

```
main
```

Contains stable working code.

---

## Development Branches

Android:

```
android-development
```

Laptop:

```
laptop-development
```

---

## Feature Branches

Format:

```
feature/<feature_name>
```

Examples:

```
feature/security-layer

feature/database

feature/windows-integration

feature/communication-protocol
```

---

# Example Development Commit Flow

## Laptop Development

Branch:

```
laptop-development
```

Commits:

```
feat: create laptop application structure

feat: add communication server

feat: add authentication validator

security: add request verification

test: add authentication tests
```

---

## Android Development

Branch:

```
android-development
```

Commits:

```
feat: create android application

feat: add biometric authentication

feat: add communication client

security: add android key storage
```

---

## Integration

Branch:

```
main
```

Commits:

```
integration: connect android and laptop modules

test: verify complete authentication flow

docs: update final documentation
```

---

# Commit Before Push Checklist

Before pushing code:

- Code should run without errors.
- Do not commit passwords or private keys.
- Do not commit virtual environments.
- Do not commit unnecessary files.
- Update documentation if architecture changes.
- Test the changes before committing.

---

# Final Rule

Any change affecting:

- Communication Protocol
- Data Format
- Security Design
- Project Architecture

must be discussed by both members before committing.

Common files inside:

```
00_Common
```

must remain synchronized between Android and Laptop development.
