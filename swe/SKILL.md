---
name: swe
description: General software engineering skill for implementing features based on a Todo List. Tasks should be classified by domain and implemented by referring to the corresponding domain-specific skills.
---

# General SWE  
Skill to implement features from Todo List. Follow principles and guidelines below.  

## Precondition  
> Pre-start Check: No Todo List, STOP.  

Before implement, check Todo List in prompt, context, or file.  
If from `todo-planner` agent, Todo List at `/docs/<task_title>/TODO.md`.  

- If provided: Start implement with below guidelines and future domain agents.  
- If not: Output message and STOP:  
  > Todo List not found. Use `skills/todo-planner/SKILL.md` to create design and Todo List, then try this skill again.  

## Guidelines (Three Principles for Software Implement)  

### Less is More  
- Simplicity First  
  - Write minimum code to solve problem. No speculative implement.  
  - Propose simpler approach if exist. Push back if needed.  
- Surgical Changes  
  - Change only what needed. Clean only what you touch.  

### Todo List Before/After Coding  
- Keep Todo List Updated  
  - Mark done items, add new if find gaps.  
- Clarify Todo Items  
  - State assumptions. If unclear, stop and ask.  
- Define Success Criteria  
  - Each item has success criteria and validate against them.  

### TDD Cycle  
- Red  
  - Pre-check: Write simple failing test to check test environment.  
  - Test First: Write test defining expected behavior from Todo Item.  
- Green  
  - Write minimum code to pass test. No extra logic.  
- Refactor  
  - Improve code, keep tests passing, follow Refactor Principles.  

## Refactor Principles  

### 1. SRP / High Cohesion  
- Each module/class/function single responsibility.  
- No premature abstraction, abstract only if duplicate.  
- Use data-driven design: logic near data, higher layers orchestrate cohesive units.  

### 2. Architectural Consistency  
- Follow existing architecture/patterns.  
- No new patterns unless needed, get approval first.  

### 3. Testability First  
- Prioritize quality: less bugs, predictable behavior.  
- Favor testability over strict current architecture if needed.  
- Cover more cases with fewer tests.  
- Each test check one behavior/user story.  

### 4. Comments  
- Minimize comments, prefer self-explaining code.  
- Annotations/tags are part of code.  
- Q/A Format Comment: explain non-obvious technical decision when logic not from business rules or code.  
  - example:  
    - Q: Why implement function this way?  
    - A: It follows existing pattern, easier for devs understand.  
      ref: usecases/user/profile.go#L10-L20  

## Steps  

## Round 1: Todo List Review and Design  
1. Check Todo List exists in prompt, context, or files. Stop if no.  
2. Classify each Todo Item by domain (domain skills come later).  

## Iteration  
1. Pick one Todo Item, implement with TDD and refactor principles.  
2. Summarize spec after implement using code as source of truth.
