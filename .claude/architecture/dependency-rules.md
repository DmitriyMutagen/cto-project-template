# Clean Architecture Dependency Rules

## Strict Rule: Dependencies point INWARD only
```
Presentation → Application → Domain ← Infrastructure
```

## Layer Responsibilities

### Domain (src/domain/) — THE CORE
- Entities, Value Objects, Domain Events
- Repository Interfaces (abstract)
- Domain Services (pure business logic)
- ZERO external dependencies (no DB, no HTTP, no frameworks)

### Application (src/services/) — USE CASES
- Orchestrates domain objects
- Implements business workflows
- Depends on domain interfaces
- No direct infrastructure access

### Presentation (src/api/) — ENTRY POINTS
- HTTP handlers, routers, middleware
- Request/response serialization
- Authentication/authorization
- Calls application layer only

### Infrastructure (src/infrastructure/) — ADAPTERS
- Database implementations (SQLAlchemy, Redis)
- External API clients (HTTP, gRPC)
- Message queue producers/consumers
- Implements domain interfaces

## Rules for AI
- NEVER import from infrastructure in domain
- NEVER import from presentation in application
- Domain entities are plain Python classes, not ORM models
- Use dependency injection for infrastructure → domain binding
