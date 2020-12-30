from post import Post
import unittest

class PostTest(unittest.TestCase):
    def setUp(self):
        self.post = Post(1, 0.5, "Test content.")

    def test_Constructor(self):
        self.assertEquals(self.post.id, 1, "ID not correctly initialized.")
        self.assertEquals(self.post.political_bias, 0.5,
                          "Political bias not correctly initialized.")
        self.assertEquals(self.post.visibility_score, 0,
                          "Visibility score not correctly initialized.")
        self.assertFalse(self.post.HasUserVoted(123),
                         "HasUserVoted should return FALSE on initialization")
        self.assertEquals(self.post.content, "Test content.",
                          "Content not correctly initialized.")

    def test_Voting(self):
        ayes = 49
        nays = 51
        for i in range(ayes):
            id = i
            self.post.VoteFor(id)
        for i in range(nays):
            id = ayes + i
            self.post.VoteAgainst(id)
        self.assertEquals(self.post.visibility_score, -2, "The nays have it.")

    def test_VotingException(self):
        self.post.VoteFor(123)
        with self.assertRaises(Exception):
            self.post.VoteAgainst(123)

if __name__ == '__main__':
    unittest.main()
