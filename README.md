![movie-metadata-gen banner](assets/banner.png)

# Movie-Metadata-Generator

A small Python class for movie metadata. The `Movies` class in
`movie-metadata.py` stores a title, director, production company, actors,
duration, and release year, and answers simple questions about the movie.

## Requirements

- Python 3, standard library only.

## Running the demo

```bash
python3 movie-metadata.py
```

Verified output:

```text
The Matrix (Film) Wachowski (Director) Warner Bros (Production Company) 1999 (Release Year)
False
True
False
True
```

Those lines are, in order: the movie printed through `__str__`, whether
it is recent, whether George Lucas worked on it, whether it requires a
bathroom break, and whether the two demo movies compare equal.

Importing the module does not run the demo; the demo is under
`if __name__ == "__main__":`, so `Movies` can be imported and reused.

## The Movies class

Constructor fields, in order: `Title`, `Director`,
`Production_Company`, `Actors`, `Duration`, `Release_Year`. `Actors` is
normally a list of names; a single string is also accepted and is matched
as one whole name. `Duration` and `Release_Year` may be numbers or
numeric strings, including decimal strings such as `"200.5"`.

Methods (all verified):

- `requiresBathroomBreak()` - returns True when the duration is over
  180 minutes, otherwise False.
- `isRecent()` - returns True when the release year is after 2020,
  otherwise False.
- `workedOnBy(name)` - returns True when `name` is the director or is
  one of the actors, otherwise False. It returns False (and does not
  raise) for an empty actor list.
- `__str__` - returns the title, director, production company, and
  release year, each followed by its label in parentheses.
- `__eq__` - two movies are equal when title, director, and release
  year match; other fields do not affect equality. Comparing a movie
  with a non-movie (for example a string or None) returns False instead
  of raising. Equal movies hash equally, so movies can be used in sets
  and as dictionary keys.

## Notes from the original assignment

- What does a certain line of the code do? The `print(movie1)` line in
  the demo prints the movie through the `__str__` method described
  above.
- Objects and classes: an object is an instance created from a class;
  the class defines the fields and methods, and each object holds its
  own values for them.
- How this class could be useful: a program that catalogues movies, for
  example a theater screening menu, could store each film as a `Movies`
  object and filter or label it with these methods.
- Simulated versus real: a real movie can be watched and played; this
  class only models its metadata, which real movies also carry.

## Files

- `movie-metadata.py` - the `Movies` class and its demo.
- `assets/banner.png`, `assets/logo.png` - project branding.
- `LICENSE` - GPL-3.0.
