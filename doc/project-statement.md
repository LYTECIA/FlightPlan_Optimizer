
# Project Statement

## Purpose
This project, **FlightPlan Manager Optimizer**, aims to design and implement a software decision-support system inspired by aeronautical Flight Management Systems (FMS).

The main goal of the system is to allow users to select departure and arrival airports, process a network of navigation waypoints, apply predefined airspace restrictions (such as military zones or adverse weather areas), and calculate the most optimal flight trajectory based on user-defined criteria (shortest distance or minimum fuel consumption considering altitude profiles).

As a Computer Science student aspiring to pursue an engineering degree in aerospace, my long-term vision is to bridge software engineering with flight physics and avionics. For this L3 project, given the academic timeline and scope, I made the conscious engineering choice to prioritize strong software architecture, relational data modeling (SQLite), and efficient graph pathfinding algorithms (Dijkstra). The core system is modularly designed so that physical flight dynamics, aerodynamic drag models, and continuous navigation parameters can be seamlessly integrated into future iterations as my engineering background expands.

---

## ✈️ Real FMS Modeling & Inspiration

In civil aviation, pilots interact with the FMS (via a cockpit interface called MCDU or CDU) to prepare and manage the aircraft's route. This project adapts the core principles of an FMS into a decision-support software tool.

### Operational Reality:
1. **The Navigation Database (NavDB):** Aircraft carry a globally updated database (on a 28-day AIRAC cycle) containing all airports, waypoints, and airways.
2. **Flight Plan Input:** The pilot inputs the departure airport (e.g., `LFBO`), arrival airport (e.g., `LFPG`), and the planned route or sequence of waypoints.
3. **Restrictions Management (NOTAMs & Weather):** Before and during flight, pilots check safety notices (NOTAMs for temporary military areas or weather alerts). If an area is closed, the FMS or ground dispatchers calculate a reroute.
4. **Optimization Calculations:** The FMS computes the trajectory, distance, vertical profile, and estimated fuel consumption based on speed and Cost Index.

### 📊 Comparison: Real FMS vs. FlightPlan Manager Optimizer

| Feature | Real FMS in Aircraft ✈️ | Our Python Project 💻 |
| :--- | :--- | :--- |
| **Data Storage** | Onboard Database (NavDB) | SQLite Database (`data/database.db`) |
| **Origin / Destination** | ICAO codes entered by pilot | Airport selection (`departure_icao`, `arrival_icao`) |
| **Waypoints** | Waypoints and Airways | `waypoints` table and connection graph |
| **Restricted Airspace** | P/R/D (Prohibited/Restricted/Danger) & Weather | `restricted_zones` & `waypoint_restrictions` tables |
| **Pathfinding** | FMS Computer / 3D/4D Trajectory | Dijkstra Algorithm (Filtered Graph) |
| **Optimization** | Vertical Profile & Cost Index (Fuel vs Speed) | Cost Comparison (Distance vs Fuel) |

---

## 🌌 Global System Architecture Overview

The application is structured around four main operational pillars:

1. **The Navigation Database (Persistence Layer):** Built on SQLite, it stores spatial and relational data representing airports, waypoints, airways, and restricted airspace zones.
2. **The Core Pathfinder (Algorithmic Layer):** Uses Graph Theory and a modified version of Dijkstra's Algorithm to dynamically filter out prohibited airspaces and calculate optimal trajectories.
3. **The Object Models (Domain Layer):** Encapsulates navigation entities (Airports, Waypoints, Flight Plans) into clean, object-oriented Python structures.
4. **The User Interface (Presentation Layer):** An interactive web GUI built with Streamlit, allowing users to select routes, toggle airspace restrictions, compare path results, and consult explanatory logs.

---

## 🎯 Personal and Educational Objectives

* **Bridging Software Engineering with Aerospace Passion:** Applying computer science skills to avionics and air navigation concepts—translating a personal passion for civil aviation into a practical, well-architected software project.
* **Mastery of Graph Algorithms & Optimization:** Implementing graph construction and constraint-based pathfinding (Dijkstra) in Python to emulate real-world route selection.
* **Relational Database Design:** Practicing SQL schema design, foreign keys, table joins, and spatial data handling using SQLite.
* **Software Architecture & Clean Code:** Applying Object-Oriented Programming (OOP), separation of concerns, and modular layer structure.
* **Technical Writing & Career Preparation:** Documenting code, architectures, and design decisions in a professional, industry-standard manner.

### 🚀 Evolutionary Roadmap & Academic Integration
* **Phase 1 (Current L3 Scope):** Solid software architecture, SQLite relational navigation database, and constraint-filtered Dijkstra pathfinding using discrete altitude consumption coefficients.
* **Phase 2 (ISAE-SUPAERO MOOC Integration):** Progressively refining the fuel burn model by replacing arbitrary coefficients with aerodynamic and flight mechanics principles learned through the ISAE-SUPAERO "How an Airplane Flies" course (drag polar equations, airspeed/angle-of-attack dynamics, and range optimization).