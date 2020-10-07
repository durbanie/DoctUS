from post import Post
import unittest

class PostTest(unittest.TestCase):
    def setUp(self):
        self.post = Post(0, 0.)

    def test_Constructor(self):
        self.assertEqual(self.post.GetPoliticalBias(), 0.,
                         "Political bias not correctly initialized.")
        self.assertEqual(self.post.GetVisibilityScore(), 0,
                         "Visibility score not correctly initialized.")
        self.assertFalse(self.post.HasUserVoted(123),
                         "HasUserVoted should return FALSE on initialization")

    def test_GetPoliticalBias(self):
        post = Post(1, 0.5)
        self.assertEqual(post.GetPoliticalBias(), 0.5,
                         "Political bias not correctly initialized.")

    def test_VoteFor(self):
        self.post.VoteFor(123)
        self.assertEquals(self.post.GetVisibilityScore(), 1,
                          "VoteFor should increment visibility score.")
        self.assertTrue(self.post.HasUserVoted(123),
                        "HasUserVoted should return TRUE after voting.")
        self.assertFalse(
            self.post.HasUserVoted(456),
            "HasUserVoted should return FALSE for non-voting user.")

    def test_VoteAgainst(self):
        self.post.VoteAgainst(123)
        self.assertEquals(self.post.GetVisibilityScore(), -1,
                          "VoteAgainst should decrement visibility score.")
        self.assertTrue(self.post.HasUserVoted(123),
                        "HasUserVoted should return TRUE after voting.")
        self.assertFalse(
            self.post.HasUserVoted(456),
            "HasUserVoted should return FALSE for non-voting user.")

if __name__ == '__main__':
    unittest.main()
