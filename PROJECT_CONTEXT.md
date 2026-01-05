# PROJECT: Autonomous Quantitative Research Agent (Enterprise Grade)

## CORE THESIS
We are NOT building a chatbot. We are building an infrastructure tool that automates quantitative research.
The output is not text; it is a **Reproducible Pull Request** containing code, a report, and a replayable audit log.

## ARCHITECTURE STACK
1. **Brain:** LangGraph (State Machine).
2. **Hands:** Python/Docker (eventually Firecracker MicroVMs).
3. **Eyes:** "Proxy Airlock" (Caching middleware for time-travel replayability).
4. **Audit:** "Evidence Bundle" (Signed JSON with full provenance).

## CURRENT STATUS (Day 1)
- We are building the CLI skeleton and defining schemas.
- We use 'Typer' for the CLI and 'Pydantic' for data validation.

## DIRECTORY STRUCTURE
quant-agent/
├── src/
│   ├── audit/schemas.py  # (Key File) Contains EvidenceBundle & ActionLog definitions
│   ├── agent/graph.py    # (Todo) LangGraph logic
│   ├── tools/proxy.py    # (Todo) Caching fetcher
│   └── main.py           # CLI Entry point
└── artifacts/            # Local storage for run bundles

## CODING RULES
1. **No Magic:** Every external tool call must be logged in the 'EvidenceBundle'.
2. **Type Safety:** Use Pydantic for all data passing.
3. **Reproducibility:** If a run cannot be replayed 100% deterministically, it is broken.
