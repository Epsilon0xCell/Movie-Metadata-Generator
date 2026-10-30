# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:21:20 2024

@author: cy83r-3x71nc710n
"""

# Movie Class
# I wrote this as one small class with no imports on purpose. It holds the
# facts I was asked to track about a film and answers three plain questions
# about them. Nothing here reads a file or calls a service.


class Movies:
    # I list the fields once here and set the same names in __init__. With
    # __slots__ there is no loose __dict__, so if I ever typo a field name
    # on assignment I get an error at that line instead of a silent extra
    # attribute that the methods below would never see.
    __slots__ = [
        "Title", "Director", "Production_Company", "Actors", "Duration",
        "Release_Year"
    ]

    def __init__(self, Title, Director, Production_Company, Actors, Duration,
                 Release_Year):
        self.Title = Title
        self.Director = Director
        self.Production_Company = Production_Company
        self.Actors = Actors
        self.Duration = Duration
        self.Release_Year = Release_Year

    def requiresBathroomBreak(self):
        # I store Duration as it was handed to me, and the demo below hands
        # it in as the string "136". float() takes that string, a number,
        # and a decimal string like "90.5". int() crashed on "90.5", which
        # is why this is float. The cut is strict: exactly 180 is False.
        return float(self.Duration) > 180

    def workedOnBy(self, name):
        # I check the director first so a film with an empty actor list
        # still answers True for its director and False for anyone else.
        # An earlier version of this method read its answer out of a loop
        # variable, and an empty list left that variable unset and crashed.
        if self.Director == name:
            return True
        # A single string in Actors is one person's name, not a list of
        # names. If I let the membership test below run on a string it
        # would walk it character by character and a whole name could
        # never match, so I compare the string as a whole here.
        if isinstance(self.Actors, str):
            return self.Actors == name
        # On a list this is an exact element match. "Keanu" does not match
        # "Keanu Reeves", and I want it that way.
        return name in self.Actors

    def isRecent(self):
        # 2020 is a fixed line I picked, not a window that moves with the
        # current year. A 2020 film is not recent by this test, a 2021
        # film is, and that will still be the rule in ten years unless I
        # change the number. float() for the same reason as Duration.
        return float(self.Release_Year) > 2020

    def __str__(self):
        # Each label sits right after the value it names. The first version
        # of this line had the values and labels shifted against each
        # other, printed the title twice, and never printed the director.
        return f"{self.Title} (Film) {self.Director} (Director) {self.Production_Company} (Production Company) {self.Release_Year} (Release Year)"

    def __eq__(self, other):
        # NotImplemented, not False, for anything that is not a Movies.
        # Returning it lets Python try the other object's comparison and
        # then settle on False. The first version reached for other.Title
        # directly and crashed with AttributeError on a string or None.
        if not isinstance(other, Movies):
            return NotImplemented
        # I compare only title, director, and release year. Two records
        # with a different production company, cast, or duration count as
        # the same film here. That is the identity I wanted: what the film
        # is, not the details of one record of it.
        return (self.Title == other.Title
                and self.Director == other.Director
                and self.Release_Year == other.Release_Year)

    def __hash__(self):
        # This has to hash the same three fields __eq__ compares, or two
        # equal movies could land in different buckets and a set would
        # hold both. Defining __eq__ alone also made Movies unhashable,
        # so this method is what lets a movie sit in a set or be a
        # dictionary key at all.
        return hash((self.Title, self.Director, self.Release_Year))


if __name__ == "__main__":
    # The demo lives under this guard because it used to run at import
    # time, so anyone importing Movies to reuse it got five lines of demo
    # output they never asked for. The duration and year below are
    # strings on purpose: they are the shape that forced float() in the
    # methods above, and I want the demo to keep proving that shape works.
    movie1actorlist = ["Keanu Reeves", 'George Lucas']
    movie2actorlist = ["Keanu Reeves", "George Lucas"]
    movie1 = Movies("The Matrix", "Wachowski", "Warner Bros", movie1actorlist,
                    "136", "1999")
    movie2 = Movies("The Matrix", "Wachowski", "Warner Bros", movie2actorlist,
                    "136", "1999")
    print(movie1)
    print(movie1.isRecent())
    print(movie1.workedOnBy("George Lucas"))
    print(movie1.requiresBathroomBreak())
    print(movie1 == movie2)
