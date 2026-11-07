import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path="data/database.db"):
        self.db_path = db_path
        # Ensure the data/ directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def get_connection(self):
        """Opens a connection to the SQLite database with Foreign Keys enabled."""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def init_db(self, schema_path="database/schema.sql"):
        """Reads and executes the SQL schema file to create tables."""
        if not os.path.exists(schema_path):
            raise FileNotFoundError(f"Schema file {schema_path} was not found.")
        
        with open(schema_path, "r", encoding="utf-8") as f:
            schema_script = f.read()

        with self.get_connection() as conn:
            conn.executescript(schema_script)
            conn.commit()
        print(" Database initialized successfully.")

    def seed_data(self):
        """Populates the database with initial sample navigation data."""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # Check if sample data is already present
            cursor.execute("SELECT COUNT(*) FROM airports")
            if cursor.fetchone()[0] > 0:
                print("Sample data is already present in database.")
                return

            # Sample Airports (Toulouse, Paris, Lyon)
            airports = [
                ("LFBO", "Toulouse-Blagnac", 43.6291, 1.3638),
                ("LFPG", "Paris-CDG", 49.0097, 2.5479),
                ("LFLL", "Lyon-Saint-Exupéry", 45.7256, 5.0811)
            ]
            cursor.executemany("INSERT INTO airports VALUES (?, ?, ?, ?)", airports)

            # Sample Waypoints
            waypoints = [
                ("WP_AGEN", "Agen-Point", 44.1747, 0.6478),
                ("WP_LIMOGES", "Limoges-Point", 45.8600, 1.2625),
                ("WP_CLERMONT", "Clermont-Point", 45.7869, 3.1114),
                ("WP_ORLEANS", "Orleans-Point", 47.9029, 1.9038)
            ]
            cursor.executemany("INSERT INTO waypoints VALUES (?, ?, ?, ?)", waypoints)

            # Sample Airway Routes (from, to, distance_km, base_fuel_kg)
            routes = [
                # Toulouse to Waypoints
                ("LFBO", "WP_AGEN", 90.0, 360.0),
                ("LFBO", "WP_LIMOGES", 220.0, 880.0),
                ("LFBO", "WP_CLERMONT", 270.0, 1080.0),

                # Inter-waypoint connections
                ("WP_AGEN", "WP_ORLEANS", 480.0, 1920.0),
                ("WP_LIMOGES", "WP_ORLEANS", 230.0, 920.0),
                ("WP_CLERMONT", "WP_ORLEANS", 250.0, 1000.0),

                # Waypoints to Paris
                ("WP_ORLEANS", "LFPG", 130.0, 520.0)
            ]
            cursor.executemany(
                "INSERT INTO routes (from_point, to_point, distance_km, base_fuel_kg) VALUES (?, ?, ?, ?)", 
                routes
            )

            # Sample Restricted Airspace Zones (e.g., Active Military Zone over Agen)
            cursor.execute("INSERT INTO restricted_zones (id, name, is_active) VALUES (1, 'R101 Military Zone Agen', 1)")
            cursor.execute("INSERT INTO waypoint_restrictions (waypoint_id, zone_id) VALUES ('WP_AGEN', 1)")

            conn.commit()
            print(" Sample navigation data inserted successfully.")

if __name__ == "__main__":
    db = DatabaseManager()
    db.init_db()
    db.seed_data()