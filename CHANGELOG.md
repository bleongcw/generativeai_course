# Changelog

All notable course updates are recorded here.

## 2026-06-25

### Changed

- Updated `agents/Lab1_introduction_to_agents_openAI.ipynb` for current OpenAI Agents SDK guidance: `openai-agents` install wording, explicit state continuation surfaces, current streaming event pattern, handoffs vs agents-as-tools, guardrails, human approval, and trace/eval framing.
- Updated OpenAI model and tool cost examples against the official pricing page: `gpt-5.4-mini` standard short-context pricing now uses `$0.75/1M` input and `$4.50/1M` output, and web search examples use `$10/1k calls` plus search content tokens billed at model rates.
- Updated `agents/Lab2_build_agenticAI_namecard_to_crm.ipynb` to use the current Responses API `web_search` tool instead of the legacy preview web-search tool.
- Refreshed README and architecture notes for the updated OpenAI Agents SDK teaching flow.

### Verified

- Confirmed official OpenAI docs for Agents SDK quickstart, running agents, results/state, orchestration, guardrails/human review, agent evals, tools, and pricing before editing.

## 2026-06-22

### Added

- Added notebook-local response caching examples to `agents/Lab1_introduction_to_agents_openAI.ipynb`.
- Added notebook-local OpenAI Responses API text caching to `agents/Lab2_build_agenticAI_namecard_to_crm.ipynb`.
- Added documentation for cache behavior, cost strategy, and cache-related roadmap work.

### Changed

- Updated agent lab documentation to describe GPT-5.4 mini vs GPT-5.5 cost trade-offs.
- Clarified that Lab 2 caches extraction, search planning, web search, and dossier synthesis reruns, while Google Sheets writes remain uncached because they are side effects.

### Verified

- Confirmed both updated agent notebooks parse as valid notebook JSON.
- Confirmed code cells in both updated agent notebooks parse cleanly.
- Confirmed the latest notebook update was pushed to `main` in commit `65518b0`.
