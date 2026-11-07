from dataclasses import dataclass, field
from typing import List

@dataclass
class FlightPlan:
    """Encapsulates the result of a computed optimal flight trajectory."""
    departure_icao: str
    arrival_icao: str
    waypoints_path: List[str] = field(default_factory=list)
    total_distance_km: float = 0.0
    total_fuel_kg: float = 0.0

    def get_path_summary(self) -> str:
        """Formats the waypoint path sequence into a visual route string (e.g., LFBO ➔ WP1 ➔ LFPG)."""
        return " ➔ ".join(self.waypoints_path)

    def __str__(self) -> str:
        """Returns a formatted summary string of the FlightPlan metrics."""
        return (
            f"FlightPlan ({self.departure_icao} ➔ {self.arrival_icao}) | "
            f"Distance: {self.total_distance_km:.1f} km | "
            f"Fuel: {self.total_fuel_kg:.1f} kg"
        )