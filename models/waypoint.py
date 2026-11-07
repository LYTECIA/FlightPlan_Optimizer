from dataclasses import dataclass

@dataclass
class Waypoint:
    """Represents an en-route navigation Waypoint along an airway network."""
    id: str
    name: str
    latitude: float
    longitude: float

    def get_coordinates(self) -> tuple[float, float]:
        """Returns the (latitude, longitude) coordinate pair of the Waypoint."""
        return (self.latitude, self.longitude)

    def __str__(self) -> str:
        """Returns a human-readable string representation of the Waypoint."""
        return f"Waypoint [{self.id}] ({self.name})"