# Development Journal & Learning Log

This log tracks design decisions, technical choices, challenges, and progress throughout the development of **FlightPlan Manager Optimizer**.

---

## 📝 Entry 1: Project Scoping, Database Design & Safety Logic

### What I Did:
1. **Project Scoping:** Defined the core objectives of this personal side-project, initiated on my own during my L3 Computer Science year to practice class concepts and fuel my aerospace passion.
2. **Repository Architecture:** Structured the repository into dedicated layer modules (`database/`, `models/`, `core/`, `ui/`, `tests/`).
3. **SQL Schema Design:** Drafted the relational schema (`schema.sql`) covering `airports`, `waypoints`, `routes`, `restricted_zones`, and the junction table `waypoint_restrictions`.
4. **Environment Setup:** Configured Python 3.12 virtual environment (`venv`) and installed core dependencies (`streamlit`, `networkx`, `pytest`, `pandas`).

### Challenges & Insights (What I Realized):
* **Pedagogical Alignment & Strategic Scope:**
  As a Computer Science student aspiring to pursue an engineering degree in aerospace, this project is a personal initiative. My vision is to bridge software engineering with flight dynamics and avionics. Developed alongside my L3 studies, I made a conscious engineering choice to first prioritize solid software foundations (modular architecture, relational SQL, graph algorithms) matching my current curriculum, while keeping the architecture extensible to integrate physical flight dynamics in future iterations.
* **Decoupling Safety Constraints from Core Pathfinder:**
  Instead of modifying Dijkstra's algorithm to check zone validity during execution, applying a **pre-filtering step** is significantly cleaner. The system queries `waypoint_restrictions` for active zones and prunes invalid nodes/edges from the graph *before* running the search.
* **Database Selection (SQLite vs. MySQL):**
  Reflecting on prior experience with MySQL in L2, SQLite is ideal for this project: serverless, embedded in a single `database.db` file, requiring zero external service setup while fully enforcing relational integrity constraints (`FOREIGN KEY`).

### Next Steps:
* Implement `database/db_manager.py` to automate `schema.sql` execution and seed initial navigation data.

---

## 📝 Entry 2: Database Layer Implementation & OOP-SQL Integration

### What I Did:
1. **Database Manager Implementation:** Developed the `DatabaseManager` class in `database/db_manager.py` using Python's native `sqlite3` library.
2. **Initialization & Seeding:** Automated schema execution (`schema.sql`) and populated the database with initial sample navigation data (Airports, Waypoints, Routes, and Restricted Zones).
3. **Debugging & Visual Verification:** Fixed syntax separation issues between SQL files and Python scripts, and verified table states using the VS Code SQLite Viewer extension.

### Challenges & Insights (What I Realized):
* **Bridging Java/PHP Experience with Python:**
  Coming from Java (OOP) and PHP/PDO (SQL), foundational concepts (DAO pattern, foreign keys, transactions) were well understood. However, adapting to Python-specific paradigms—such as `__init__` constructors, explicit `self` reference passing, and `with` Context Managers for transaction handling—required targeted study (video tutorials and documentation).
* **Why OOP for Database Management?**
  * **Encapsulation & Centralization:** Isolates raw SQL strings and centralizes configuration (`self.db_path`, explicit `PRAGMA foreign_keys = ON;`).
  * **Lifecycle & Resource Management:** Automates connection opening, closing, and transaction commits through context managers (`with self.get_connection()`).
  * **Domain Abstraction:** Hides low-level database operations behind clean method signatures (`db.init_db()`, `db.seed_data()`).
  * **Testability & Scalability:** Allows seamless instantiation of temporary in-memory databases (`:memory:`) for isolated unit testing without corrupting production data.

### Next Steps:
* Build domain models in `models/` (`Airport`, `Waypoint`, `FlightPlan`) to bridge raw SQL tuples with strongly-typed Python objects.