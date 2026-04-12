# chaos-pilot

A self-healing infrastructure lab. Three containers run a live app. 
A chaos agent breaks things on purpose. A healing engine fixes them 
automatically. Everything is tracked in real time on a Grafana dashboard.

Built to learn and demonstrate chaos engineering — a discipline used 
by Netflix, Amazon, and Google to harden production systems.

---

## What's inside

| Component      | Name       | Role                                                        |
|----------------|------------|-------------------------------------------------------------|
| Flask app      | canary     | The target — receives traffic, talks to Redis and Postgres  |
| Chaos Agent    | gremlins   | Injects failures — kills containers, spikes CPU, fills disk |
| Healing Engine | medic      | Watches for failures and recovers automatically             |
| Metrics        | Prometheus | Scrapes health data from every component                    |
| Dashboard      | Grafana    | Visualizes chaos events and recovery in real time           |

---

## Phases

- [x] Phase 1 — canary: multi-container app running with Docker Compose
- [ ] Phase 2 — gremlins: chaos injection engine
- [ ] Phase 3 — medic: automated healing engine  
- [ ] Phase 4 — observability: Prometheus + Grafana dashboard
- [ ] Phase 5 — security pipeline: GitHub Actions with CVE and secret scanning

---

## Run it locally

coming soon

---

## Author

Zahra — CS student building toward DevOps engineering.
