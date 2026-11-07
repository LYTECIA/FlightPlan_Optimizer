# FlightPlan Manager Optimizer — Global Architecture

This document describes the software design, directory layout, and architectural layers of the FlightPlan Manager Optimizer system.

---

## 🏗️ Folder Structure & Architectural Layers

```text
flightplan_optimizer/
│
docs/
├── project_statement.md   # Purpose, FMS alignment & educational goals
├── architecture.md        # Software layout & execution flow
├── journal.md             # Development log & learning journal
└── simulation-choices.md  # Model simplifications & future technical   roadmap
│
├── data/
│   └── database.db          # Persistent SQLite database file
│
├── database/
│   ├── schema.sql           # Database creation & table relational structure
│   └── db_manager.py        # Python SQLite connector & CRUD operations
│
├── models/
│   ├── airport.py           # Domain model representing an Airport
│   ├── waypoint.py          # Domain model representing a Waypoint
│   └── flight_plan.py       # Domain model encapsulating a calculated Flight Plan
│
├── core/
│   ├── navigation_graph.py  # Graph representation built from SQL data
│   └── pathfinder.py        # Constraint-filtering & Dijkstra optimization algorithms
│
├── ui/
│   └── app.py               # Streamlit interactive graphic user interface
│
├── tests/
│   └── test_pathfinder.py   # Automated unit tests using Pytest
│
└── main.py                  # Project entry point and environment initializer