"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    @classmethod
    def increment_total_aliens_created(cls):
        """Add one to total number of aliens created."""
        cls.total_aliens_created += 1

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        self.increment_total_aliens_created()

    def hit(self):
        """Decrement Alien health by one point."""
        if self.is_alive():
            self.health -= 1

    def is_alive(self):
        """Return a Boolean for if Alien is alive (if health is > 0).

        Returns:
            bool: True if Alien is alive, otherwise False.
        """
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien to new coordinates.

        Args:
            new_x_coordinate (int): New x-coordinate.
            new_y_coordinate (int): New y-coordinate.
        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        """Detects if Alien has collided with another object.

        Args:
            other_object (TODO): TODO
        """


def new_aliens_collection(alien_start_positions):
    """Create new aliens with start positions provided.

    Args:
        alien_start_positions (list(tuple(int))): List of tuples of x- and y-coordinates.

    Returns:
        list(Alien): List of Aliens created.
    """
    coordinates = [
        (start_position[0], start_position[1])
        for start_position in alien_start_positions
    ]

    return [
        Alien(x_coordinate, y_coordinate) for x_coordinate, y_coordinate in coordinates
    ]
