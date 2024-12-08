import math
import random


class Universe:
    """Universal constants and utility functions"""
    G = 6.67430e-11  # Gravitational constant


class Sun:
    def __init__(self, name, mass, radius, temperature):
        """
        Initialize a Sun object

        :param name: Name of the sun
        :param mass: Mass of the sun
        :param radius: Radius of the sun
        :param temperature: Surface temperature of the sun
        """
        self.name = name
        self._mass = mass
        self._radius = radius
        self._temperature = temperature

        # Default position at the center of the solar system
        self._x_pos = 0.0
        self._y_pos = 0.0

    def get_mass(self):
        """Get the mass of the sun"""
        return self._mass

    def get_x_pos(self):
        """Get x-coordinate of the sun"""
        return self._x_pos

    def get_y_pos(self):
        """Get y-coordinate of the sun"""
        return self._y_pos

    def set_position(self, x, y):
        """Set the position of the sun"""
        self._x_pos = x
        self._y_pos = y


class Planet:
    def __init__(self, name, initial_velocity, mass, radius, x_pos, y_pos, color):
        """
        Initialize a Planet object

        :param name: Name of the planet
        :param initial_velocity: Initial velocity of the planet
        :param mass: Mass of the planet
        :param radius: Radius of the planet
        :param x_pos: Initial x-coordinate
        :param y_pos: Initial y-coordinate
        :param color: Color of the planet for visualization
        """
        self.name = name
        self._mass = mass
        self._radius = radius
        self._color = color

        # Position
        self._x_pos = x_pos
        self._y_pos = y_pos

        # Velocity
        self._x_vel = 0
        self._y_vel = initial_velocity

    def get_mass(self):
        """Get the mass of the planet"""
        return self._mass

    def get_x_pos(self):
        """Get x-coordinate of the planet"""
        return self._x_pos

    def get_y_pos(self):
        """Get y-coordinate of the planet"""
        return self._y_pos

    def get_x_vel(self):
        """Get x-velocity of the planet"""
        return self._x_vel

    def get_y_vel(self):
        """Get y-velocity of the planet"""
        return self._y_vel

    def set_x_vel(self, velocity):
        """Set x-velocity of the planet"""
        self._x_vel = velocity

    def set_y_vel(self, velocity):
        """Set y-velocity of the planet"""
        self._y_vel = velocity

    def move_to(self, x, y):
        """Move the planet to a new position"""
        self._x_pos = x
        self._y_pos = y

    def distance_from_sun(self, sun):
        """Calculate distance from the sun"""
        dx = self._x_pos - sun.get_x_pos()
        dy = self._y_pos - sun.get_y_pos()
        return math.sqrt(dx ** 2 + dy ** 2)


class SolarSystem:
    def __init__(self):
        """Initialize a Solar System"""
        self.the_sun = None
        self.planets = []

    def add_sun(self, sun):
        """Add a sun to the solar system"""
        self.the_sun = sun

    def add_planet(self, planet):
        """Add a planet to the solar system"""
        self.planets.append(planet)

    def move_planets(self):
        """Move planets based on gravitational interactions"""
        dt = 0.001  # Time interval

        for planet in self.planets:
            # Move the planet
            planet.move_to(
                planet.get_x_pos() + dt * planet.get_x_vel(),
                planet.get_y_pos() + dt * planet.get_y_vel())

            # Calculate new distance from sun
            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            new_distance = math.sqrt(dist_x ** 2 + dist_y ** 2)

            # Calculate acceleration
            acc_x = Universe.G * self.the_sun.get_mass() * dist_x / (new_distance ** 3)
            acc_y = Universe.G * self.the_sun.get_mass() * dist_y / (new_distance ** 3)

            # Update velocities
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)


class Simulation:
    def __init__(self, solar_system, width, height, iterations):
        """
        Initialize a Simulation

        :param solar_system: The solar system to simulate
        :param width: Width of the simulation space
        :param height: Height of the simulation space
        :param iterations: Number of simulation iterations
        """
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.iterations = iterations

    def run(self):
        """Run the simulation"""
        for _ in range(self.iterations):
            self.solar_system.move_planets()

            # Print planet positions
            for planet in self.solar_system.planets:
                print(f"{planet.name}: x={planet.get_x_pos():.2f}, y={planet.get_y_pos():.2f}, " +
                      f"distance={planet.distance_from_sun(self.solar_system.the_sun):.2f}")


# Example main method to test the simulation
if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 10000000, 5800)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 47.5, 1, 25, 5.0, 200.0, "green")
    solar_system.add_planet(earth)

    mars = Planet("MARS", 40.5, .1, 62, 10.0, 125.0, "red")
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()