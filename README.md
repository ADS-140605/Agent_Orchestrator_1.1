# Agent Orchestrator

OpenRouter-compatible LLM API gateway — a unified proxy for OpenAI, Anthropic, and Google Gemini.

## Todo

### Phase 1: Foundation
- [ ] Project structure, config, DB schema, provider abstraction
- [ ] Data models: User, ApiKey, Provider, Model, ChatCompletion, UsageLog (SQLAlchemy + Alembic)
- [ ] Provider abstraction layer (interface + registry)

### Phase 2: Provider integrations
- [ ] OpenAI-compatible adapter (HTTP client + streaming + tool calls)
- [ ] Anthropic adapter (Claude API, native tool use)
- [ ] Google Gemini adapter

### Phase 3: Core API
- [ ] `POST /v1/chat/completions` — unified request/response mapping
- [ ] Streaming support (SSE)
- [ ] Model routing — map model slugs to provider(s) with failover
- [ ] `GET /v1/models` — list available models

### Phase 4: Auth & API key management
- [ ] API key authentication middleware (Bearer token)
- [ ] API key CRUD endpoints (create, list, revoke)

### Phase 5: Rate limiting, cost tracking, usage logging
- [ ] Rate limiter (per-key / per-IP, token-bucket or sliding window)
- [ ] Usage logging — token counts, cost, latency
- [ ] Cost calculator per model per provider

### Phase 6: Admin (CLI)
- [ ] Admin CLI: user management, usage stats, provider health

### Phase 7: Production hardening
- [ ] CORS, structured logging, error handling middleware
- [ ] Response caching
- [ ] Health checks, Prometheus metrics
- [ ] Dockerfile + docker-compose (app + postgres + redis)

### Phase 8: Testing & DX
- [ ] Unit tests for provider adapters
- [ ] Integration tests with `/v1/chat/completions` (mock providers)
- [ ] Client SDK examples (Python, curl, JS)
