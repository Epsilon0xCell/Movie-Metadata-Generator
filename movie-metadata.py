# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:21:20 2024

@author: cy83r-3x71nc710n
"""

# Movie Class


class Movies:
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
        return float(self.Duration) > 180

    def workedOnBy(self, name):
        if self.Director == name:
            return True
        if isinstance(self.Actors, str):
            return self.Actors == name
        return name in self.Actors

    def isRecent(self):
        return float(self.Release_Year) > 2020

    def __str__(self):
        return f"{self.Title} (Film) {self.Director} (Director) {self.Production_Company} (Production Company) {self.Release_Year} (Release Year)"

    def __eq__(self, other):
        if not isinstance(other, Movies):
            return NotImplemented
        return (self.Title == other.Title
                and self.Director == other.Director
                and self.Release_Year == other.Release_Year)

    def __hash__(self):
        return hash((self.Title, self.Director, self.Release_Year))


if __name__ == "__main__":
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
