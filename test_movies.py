import importlib.util
import subprocess
import sys
import unittest

spec = importlib.util.spec_from_file_location("movie_metadata",
                                              "movie-metadata.py")
mm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mm)
Movies = mm.Movies


def make(**overrides):
    fields = dict(Title="The Matrix", Director="Wachowski",
                  Production_Company="Warner Bros",
                  Actors=["Keanu Reeves", "George Lucas"],
                  Duration="136", Release_Year="1999")
    fields.update(overrides)
    return Movies(**fields)


class ConstructionTests(unittest.TestCase):
    def test_demo_shape_is_accepted(self):
        movie = make()
        self.assertEqual(movie.Title, "The Matrix")
        self.assertEqual(movie.Duration, "136")

    def test_non_numeric_duration_is_rejected_at_construction(self):
        with self.assertRaises(ValueError) as caught:
            make(Duration="abc")
        self.assertIn("Duration", str(caught.exception))

    def test_non_numeric_year_is_rejected_at_construction(self):
        with self.assertRaises(ValueError) as caught:
            make(Release_Year="abc")
        self.assertIn("Release_Year", str(caught.exception))

    def test_none_duration_is_rejected(self):
        with self.assertRaises(ValueError):
            make(Duration=None)

    def test_empty_title_is_rejected(self):
        for bad in ("", "   ", None, 42):
            with self.assertRaises(ValueError, msg=repr(bad)):
                make(Title=bad)

    def test_actors_must_be_a_name_or_a_list(self):
        with self.assertRaises(TypeError):
            make(Actors=None)
        with self.assertRaises(TypeError):
            make(Actors=42)
        self.assertEqual(make(Actors="Keanu Reeves").Actors,
                         "Keanu Reeves")


class MethodTests(unittest.TestCase):
    def test_bathroom_break_cut_is_strictly_over_180(self):
        self.assertFalse(make(Duration="180").requiresBathroomBreak())
        self.assertTrue(make(Duration="181").requiresBathroomBreak())
        self.assertFalse(make(Duration="90.5").requiresBathroomBreak())
        self.assertTrue(make(Duration=200).requiresBathroomBreak())

    def test_is_recent_line_is_after_2020(self):
        self.assertFalse(make(Release_Year="2020").isRecent())
        self.assertTrue(make(Release_Year="2021").isRecent())
        self.assertFalse(make(Release_Year=1999).isRecent())

    def test_worked_on_by_director_actor_and_stranger(self):
        movie = make()
        self.assertTrue(movie.workedOnBy("Wachowski"))
        self.assertTrue(movie.workedOnBy("Keanu Reeves"))
        self.assertFalse(movie.workedOnBy("Steven Spielberg"))

    def test_worked_on_by_partial_name_does_not_match(self):
        self.assertFalse(make().workedOnBy("Keanu"))

    def test_worked_on_by_empty_actor_list(self):
        movie = make(Actors=[])
        self.assertTrue(movie.workedOnBy("Wachowski"))
        self.assertFalse(movie.workedOnBy("Keanu Reeves"))

    def test_worked_on_by_single_string_actor(self):
        movie = make(Actors="Keanu Reeves")
        self.assertTrue(movie.workedOnBy("Keanu Reeves"))
        self.assertFalse(movie.workedOnBy("Keanu"))

    def test_str_format(self):
        self.assertEqual(
            str(make()),
            "The Matrix (Film) Wachowski (Director) Warner Bros "
            "(Production Company) 1999 (Release Year)")


class EqualityTests(unittest.TestCase):
    def test_equal_when_title_director_and_year_match(self):
        self.assertEqual(make(), make(Production_Company="Other",
                                      Duration="10"))

    def test_not_equal_when_a_compared_field_differs(self):
        self.assertNotEqual(make(), make(Release_Year="2003"))
        self.assertNotEqual(make(), make(Title="Other"))

    def test_comparison_with_non_movie_is_false_not_an_error(self):
        self.assertFalse(make() == "The Matrix")
        self.assertFalse(make() == None)  # noqa: E711
        self.assertTrue(make() != "The Matrix")

    def test_equal_movies_hash_equally_and_dedup_in_a_set(self):
        self.assertEqual(hash(make()), hash(make()))
        self.assertEqual(len({make(), make()}), 1)


class DemoTests(unittest.TestCase):
    def test_demo_output_matches_the_readme(self):
        result = subprocess.run(
            [sys.executable, "movie-metadata.py"],
            capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            result.stdout,
            "The Matrix (Film) Wachowski (Director) Warner Bros "
            "(Production Company) 1999 (Release Year)\n"
            "False\nTrue\nFalse\nTrue\n")


if __name__ == "__main__":
    unittest.main()
