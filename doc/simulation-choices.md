# Simulation Choices and Design Decisions

## Purpose of this Document
This document tracks design decisions, model simplifications, and architectural trade-offs made during the development of **FlightPlan Manager Optimizer**.

As a software engineering project developed alongside L3 Computer Science studies, certain complex physical phenomena are simplified in initial versions and iteratively refined as domain knowledge expands.

---

## 1. Fuel Consumption Model

### Current Choice (Version 1)
In the initial implementation, fuel consumption values (`base_fuel_kg`) per route segment are statically defined in the SQLite database (`routes` table) using simplified baseline estimates (approx. 4 kg/km).

### Motivation & Scoping
Calculating exact fuel burn in real civil aviation depends on continuous aerodynamic drag equations, aircraft mass, engine thrust profiles, atmospheric weather, and cruising altitude profiles. 

To prioritize core computer science objectives (database design, OOP domain modeling, and graph pathfinding algorithms), physical flight dynamics are abstracted into pre-calculated baseline database metrics for the initial release.

### Future Roadmap & Enhancements (Version 2+)
Driven by ongoing self-study in flight mechanics (including the ISAE-SUPAERO "How an Airplane Flies" MOOC), future iterations will replace static values with:
1. **Altitude-Dependent Multipliers:** Adjusting fuel burn based on cruising levels (e.g., FL290 vs. FL370).
2. **Cost Index (CI) Optimization:** Emulating real Flight Management System (FMS) trade-offs between flight time cost and fuel cost.