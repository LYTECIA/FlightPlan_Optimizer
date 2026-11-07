-- Database Schema for FlightPlan Manager Optimizer

-- 1. Airports Table
CREATE TABLE IF NOT EXISTS airports (
    icao_code VARCHAR(4) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);

-- 2. Waypoints Table (Navigation points in the sky)
CREATE TABLE IF NOT EXISTS waypoints (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);

-- 3. Airways / Routes Table (Graph Edges)
CREATE TABLE IF NOT EXISTS routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_point VARCHAR(10) NOT NULL,
    to_point VARCHAR(10) NOT NULL,
    distance_km REAL NOT NULL,
    base_fuel_kg REAL NOT NULL
);

-- 4. Restricted Airspace Zones Table
CREATE TABLE IF NOT EXISTS restricted_zones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT 1
);

-- 5. Junction Table linking Waypoints and Restricted Zones
CREATE TABLE IF NOT EXISTS waypoint_restrictions (
    waypoint_id VARCHAR(10),
    zone_id INTEGER,
    PRIMARY KEY (waypoint_id, zone_id),
    FOREIGN KEY (waypoint_id) REFERENCES waypoints(id),
    FOREIGN KEY (zone_id) REFERENCES restricted_zones(id)
);

-- 6. Flight Plan History Table
CREATE TABLE IF NOT EXISTS flight_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    departure_icao VARCHAR(4) NOT NULL,
    arrival_icao VARCHAR(4) NOT NULL,
    path_summary TEXT NOT NULL,
    total_distance_km REAL NOT NULL,
    total_fuel_kg REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);