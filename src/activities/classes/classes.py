from dataclasses import dataclass
from datetime import date
from typing import List


class ParalympicEvent:
    """Represents a Paralympic event

        Attributes:
            name (str): A string representing the name of the event
            sport (str): A string representing the sport that the event
                belongs to
            classification (str): An string representing the event
                classification
            athletes (list): A list of strings representing the athletes that
                compete in the event

        Methods:
            describe(): Prints a description of the event
            register_athlete(): Adds an athlete to the list of athletes
    """
    def __init__(self, name: str, sport: str, classification: str):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []  # Empty list to hold athlete names

    def describe(self) -> None:
        """ Describes the event """
        print(f"{self.name} is a {self.sport} event for classification"
              f" {self.classification}.")
        print("Athletes competing:", ", ".join(self.athletes))

    def register_athlete(self, athlete_name: str) -> None:
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)


@dataclass
class Medal:
    type: str
    design: str
    date_designed: date


class Athlete:
    """Represents a Paralympic event

        Attributes:
            name (str): A string representing the name of the athlete
            team (str): A string representing the team the athlete plays for
            disabilitity (str): A string representing any disabilities the
                athlete has

        Methods:
    """

    def __init__(self, first_name: str, last_name: str, team_code: str,
                 disability_class: str, medals: List[Medal]):
        self.first_name = first_name
        self.last_name = last_name
        self.team_code = team_code
        self.disability_class = disability_class
        self.medals = medals  # Composition: Athlete has Medals

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} plays for"\
            f" {self.team_code} with disability class {self.disability_class}"

    def introduce(self) -> str:
        return f"{self.first_name} {self.last_name} represents "\
            f"{self.team_code} in disability class {self.disability_class}."


class Runner(Athlete):
    def __init__(self, first_name: str, last_name: str, team_code: str,
                 disability_class: str, distance: str):
        super().__init__(first_name, last_name, team_code, disability_class)
        self.distance = distance  # e.g., 100m, 400m

    def race_info(self) -> None:
        print(f"{self.first_name} is running the {self.distance} race.")


event = ParalympicEvent(
    name="100m Sprint",
    sport="Running",
    classification="BC1",
)

# Should print the event description, "Athletes competing" will be empty
event.describe()

# should register the athlete
event.register_athlete("Usain Bolt")
event.register_athlete("Mo Farah")

# Should print event again, "Athletes competing" should include the abov
event.describe()

# athlete1 = Athlete("Bob", "Guy", "UK", "Paralysis")
# athlete1.introduce()

# runner1 = Runner("Li", "Na", "CHN", "T12", "100m")
# runner1.introduce()  # Inherited method
# runner1.race_info()  # Subclass-specific method

# Create medals
medal1 = Medal("gold", "Paris 2024 design", date(2023, 7, 1))
medal2 = Medal("silver", "Tokyo 2020 design", date(2019, 8, 25))

# Create an athlete with medals
athlete = Athlete(
    first_name="Wei",
    last_name="Wang",
    team_code="CHN",
    disability_class="T54",
    medals=[medal1, medal2]
)

print(athlete)
print(athlete.introduce())
