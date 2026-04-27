---
name: todo-planner
description: >
 Skill for turn requirements into simple Todo List, with task break down, solve dependency, ask better question. Output clear goal, overview doc, Todo List, reference map.
---

Turn my requirements to tasks using codebase, references (docs, tickets, issues, images).

Ask many questions about all parts till we both understand. Walk design tree, solve dependency one-by-one. Give recommended answer for each question.

Ask one question at time.

If answer in references, check references first.

## Step
1. Use Context(codebase, references) + Web Search to find info for task. Then make/output simple index for search/reference. Use /docs/tmp for this.
2. Break down requirements to tasks in Todo list format, output it. Use /docs/tmp/todo.md for this.
3. Summarize requirements + tasks into overview doc, output it. Use /docs/tmp/overview.md for this.
4. Rename /docs/tmp to /docs/<task_title> by title we choose.
5. Ask me questions to improve todo list and we improve todo-list together.

## Output
1. Reference Map: list at /docs/<task_title>/reference.md
2. Todo List: structured/hierarchical todo list at /docs/<task_title>/todo.md
3. Overview: overview doc with title + task summary. No detail task inside but have overview + references.

## Example Output

1. Reference Map
path: /docs/tmp/reference.md

```markdown
# Reference Map
- [Current User Definition](backend/domain/user.go) - The current user model in the backend, which may need to be extended to support roles and permissions.
- [DB Schema management](infra/db/schema.sql) - The current database schema, which may require changes to accommodate new tables or fields for authentication and authorization.
- [New Authentication Flow Diagram](./references/auth_flow_diagram.mmd) - A visual representation of the new authentication flow, including the interactions between the frontend, backend, and any third-party services.
- [Backend API Design Document](../specs/auth.md) - The design document outlining the API endpoints, request/response formats, and authentication logic for the backend implementation.
- [Best RBAC Implementation Guide](https://example.com/rbac-guide) - A comprehensive guide on implementing Role-Based Access Control (RBAC) in web applications, which can be used as a reference for designing the authorization system.
- [OAuth 2.0 Overview](https://example.com/oauth2-overview)
```

2. Todo List
/docs/tmp/todo.md
```markdown
# Todo List to accomplish User's requirements

- [ ] Draw the new authentication flow diagram by Mermaid.js
- [ ] Model and DB Update (DBA)
  - [ ] Design the new user model
  - [ ] Extend the current user model to include roles and permissions
  - [ ] Update the database schema to accommodate new fields for authentication and authorization
- [ ] Provision new Auth Infrastructure (Infra-SWE)
  - [ ] Set up an Identity Provider (IdP) if necessary (e.g., Auth0, Keycloak) or plan for in-house implementation
- [ ] Backend Implementation (Backend-SWE)
  - [ ] Design API endpoints for user authentication and authorization
  - [ ] Update UserController to handle login requests and issue JWT tokens
  - [ ] Add AuthService to manage authentication logic and token generation
  - [ ] Update UserQuery to retrieve user information along with roles and permissions
  - [ ] Implement middleware to protect routes based on user roles and permissions
  - [ ] Generate new version of OpenAPI schema reflecting the changes
- [ ] Frontend Implementation (Frontend-SWE)
  - [ ] Design the login page and user interface for authentication
  - [ ] Design State management strategy for handling authentication state and user roles
  - [ ] Implement the login form and handle user input
  - [ ] Integrate with the backend API to authenticate users and handle JWT tokens
  - [ ] Implement role-based access control on the frontend to show/hide UI elements based on user roles and permissions
```
```

3. Overview
path: /docs/tmp/overview.md
```markdown
# Title
Implement User Auth Feature

# Summary
This task involves implementing a user authentication and authorization system for our application. The goal is to allow users to securely log in and access protected resources based on their roles. The implementation will follow best practices for security and scalability, and will be designed to integrate seamlessly with our existing codebase.
```
