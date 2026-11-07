from dataclasses import dataclass

@dataclass
class Airport:
    """Represents an Airport navigation node within the system."""
    icao_code: str
    name: str
    latitude: float
    longitude: float

    def get_coordinates(self) -> tuple[float, float]:
        """Returns the (latitude, longitude) coordinate pair for distance calculations."""
        return (self.latitude, self.longitude)

    def __str__(self) -> str:
        """Returns a human-readable string representation of the Airport."""
        return f"Airport [{self.icao_code}] - {self.name}"