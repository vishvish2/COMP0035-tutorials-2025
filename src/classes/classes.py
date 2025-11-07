class ParalympicEvent:
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in
            the event

     Methods:
         describe() Prints a description of the event
         register_athlete() Adds an athlete to the list of athletes
     """

    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []  # Empty list to hold athlete names

    def describe(self):
        """ Describes the event """
        print(f"{self.name} is a {self.sport} event for classification"
              f" {self.classification}.")
        print("Athletes competing:", ", ".join(self.athletes))

    def register_athlete(self, athlete_name):
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)


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
