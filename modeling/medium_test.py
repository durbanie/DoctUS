from medium import InvalidAction, Medium
import unittest

class MediumTest(unittest.TestCase):
    def setUp(self):
        self.medium = Medium(1, 0.5)

    def test_Constructor(self):
        self.assertEquals(self.medium.id, 1, "ID not correctly initialized.")
        self.assertEquals(self.medium.political_bias, 0.5,
                          "Political bias not correctly initialized.")
        self.assertEquals(self.medium.visibility_score, 0,
                          "Visibility score not correctly initialized.")
        self.assertFalse(self.medium.HasUserVoted(123),
                         "HasUserVoted should return FALSE on initialization")

    def test_VoteFor(self):
        self.medium.VoteFor(123)
        self.assertEquals(self.medium.visibility_score, 1,
                          "VoteFor should increment visibility score.")
        self.assertTrue(self.medium.HasUserVoted(123),
                        "HasUserVoted should return TRUE after voting.")
        self.assertFalse(
            self.medium.HasUserVoted(456),
            "HasUserVoted should return FALSE for non-voting user.")
        self.medium.VoteFor(456)
        self.assertEquals(self.medium.visibility_score, 2,
                          "VoteFor should increment visibility score.")
        self.assertTrue(self.medium.HasUserVoted(456),
                        "HasUserVoted should return TRUE after voting.")

    def test_VoteFor_throwsExceptionIfSameVotesTwice(self):
        self.medium.VoteFor(123)
        with self.assertRaises(InvalidAction):
            self.medium.VoteFor(123)

    def test_VoteAgainst(self):
        self.medium.VoteAgainst(123)
        self.assertEquals(self.medium.visibility_score, -1,
                          "VoteAgainst should decrement visibility score.")
        self.assertTrue(self.medium.HasUserVoted(123),
                        "HasUserVoted should return TRUE after voting.")
        self.assertFalse(
            self.medium.HasUserVoted(456),
            "HasUserVoted should return FALSE for non-voting user.")
        self.medium.VoteAgainst(456)
        self.assertEquals(self.medium.visibility_score, -2,
                          "VoteAgainst should decrement visibility score.")
        self.assertTrue(self.medium.HasUserVoted(456),
                        "HasUserVoted should return TRUE after voting.")

    def test_VoteAgainst_throwsExceptionIfSameUserVotesTwice(self):
        self.medium.VoteAgainst(123)
        with self.assertRaises(InvalidAction):
            self.medium.VoteAgainst(123)


if __name__ == '__main__':
    unittest.main()
