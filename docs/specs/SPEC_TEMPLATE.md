# Feature Specification: [FEATURE NAME]

## Status: DRAFT | APPROVED | IN PROGRESS | DONE
## Date: YYYY-MM-DD
## Author: [name]

---

## 1. Business Requirements
**Goal**: What business metric does this move?
**User Story**: As a [role], I want [feature] so that [benefit]
**Success Metrics**: How do we measure success?

## 2. Technical Design
**Architecture**: Which layers are affected?
**API Contract**:
```
POST /api/v1/resource
Request: { field: type }
Response: { field: type }
```
**Data Model**: New tables/fields?
**Dependencies**: External services, libraries?

## 3. Task Decomposition
- [ ] Task 1: [description] — [file paths] — [est. time]
- [ ] Task 2: [description] — [file paths] — [est. time]
- [ ] Task 3: [description] — [file paths] — [est. time]

## 4. Edge Cases
- What if input is empty?
- What if external API is down?
- What if data volume is 100x expected?

## 5. Non-Requirements (explicitly NOT doing)
- [what we're NOT building in this iteration]

## 6. Definition of Done
- [ ] All tasks completed
- [ ] Tests pass (>80% coverage)
- [ ] No lint errors
- [ ] Sentry: no new errors
- [ ] Code review passed
- [ ] Spec compliance verified
