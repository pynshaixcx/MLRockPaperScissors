import unittest
from RPS_game import play, pynshai, mei2, quincy, dari
from RPS import player


class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_quincy(self):
        print("Testing game against quincy...")
        actual = play(player, quincy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat quincy at least 60% of the time.')

    def test_player_vs_mei2(self):
        print("Testing game against abbey...")
        actual = play(player, mei2, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat mei2 at least 60% of the time.')

    def test_player_vs_dari(self):
        print("Testing game against dari...")
        actual = play(player, dari, 1000) >= 60
        self.assertTrue(
            actual, 'Expected player to defeat dari at least 60% of the time.')

    def test_player_vs_pynshai(self):
        print("Testing game against pynshai...")
        actual = play(player, pynshai, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat pynshai at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()
