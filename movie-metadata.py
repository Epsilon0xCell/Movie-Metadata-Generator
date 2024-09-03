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
    if int(self.Duration) > 180:
      return True
    else:
      return False

  def workedOnBy(self, name):
    # Updated loop as it was getting stuck with a mistake of exiting before return True could be setup
    for i, val in enumerate(self.Actors):
      if val == name or self.Director == name:
        return True
      else:
        i = 0
    if i == 0:
      return False

  def isRecent(self):
    if int(self.Release_Year) > 2020:
      return True
    else:
      return False

  def __str__(self):
    return f"{self.Title} (Director) {self.Release_Year} (Release Year) {self.Title} (Film) {self.Production_Company} (Production Company)"

  def __eq__(self, other):
    if self.Title == other.Title and self.Director == other.Director and self.Release_Year == other.Release_Year:
      return True
    else:
      return False


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
