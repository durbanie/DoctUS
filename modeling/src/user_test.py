from user import User
from medium import Medium
from post import Post
import unittest

RIGHT_ID = 0
CENTER_ID = 1
LEFT_ID = 2

class UserTest(unittest.TestCase):
    def setUp(self):
        # Set-up Users.
        self.leftUser = User(LEFT_ID, -0.5, 0.1, 0.6)
        self.centerUser = User(CENTER_ID, 0., 0.1, 0.6)
        self.rightUser = User(RIGHT_ID, 0.5, 0.1, 0.6)

    def test_Constructor(self):
        self.assertEquals(self.rightUser.id, RIGHT_ID,
                          "Right-leaning User ID incorrect.")
        self.assertEquals(self.rightUser.political_bias, 0.5,
                          "Right-leaning User political bias incorrect.")
        self.assertEquals(self.centerUser.id, CENTER_ID,
                          "Centrist User ID incorrect.")
        self.assertEquals(self.centerUser.political_bias, 0.,
                          "Centrist User political bias incorrect.")
        self.assertEquals(self.leftUser.id, LEFT_ID,
                          "Left-leaning User ID incorrect.")
        self.assertEquals(self.leftUser.political_bias, -0.5,
                          "Left-leaning User political bias incorrect.")

    def test_InteractWithMedium_farLeftPost(self):
        farLeftPost = Post(0, -0.85, "Eat the rich!")
        self.leftUser.InteractWithMedium(farLeftPost)
        self.assertEquals(farLeftPost.visibility_score, 0,
                          "LeftUser should ignore farLeftPost.")
        self.centerUser.InteractWithMedium(farLeftPost)
        self.assertEquals(farLeftPost.visibility_score, -1,
                          "CenterUser should vote against farLeftPost.")
        self.rightUser.InteractWithMedium(farLeftPost)
        self.assertEquals(farLeftPost.visibility_score, -2,
                          "RightUser should vote against farLeftPost.")

    def test_InteractWithMedium_leftPost(self):
        leftPost = Post(1, -0.55, "I just want affordable healthcare.")
        self.leftUser.InteractWithMedium(leftPost)
        self.assertEquals(leftPost.visibility_score, 1,
                          "LeftUser should vote for leftPost.")
        self.centerUser.InteractWithMedium(leftPost)
        self.assertEquals(leftPost.visibility_score, 1,
                          "CenterUser should ignore leftPost.")
        self.rightUser.InteractWithMedium(leftPost)
        self.assertEquals(leftPost.visibility_score, 0,
                          "RightUser should vote against leftPost.")

    def test_InteractWithMedium_centerLeftPost(self):
        centerLeftPost = Post(
            2, -0.05, "Capitalism should be constrained for the public good.")
        self.leftUser.InteractWithMedium(centerLeftPost)
        self.assertEquals(centerLeftPost.visibility_score, 0,
                          "LeftUser should ignore centerLeftPost.")
        self.centerUser.InteractWithMedium(centerLeftPost)
        self.assertEquals(centerLeftPost.visibility_score, 1,
                          "CenterUser should vote for centerLeftPost.")
        self.rightUser.InteractWithMedium(centerLeftPost)
        self.assertEquals(centerLeftPost.visibility_score, 1,
                          "RightUser should ignore centerLeftPost.")

    def test_InteractWithMedium_centerRightPost(self):
        centerRightPost = Post(
            3, 0.05, "We should examine the merits of a flat tax system.")
        self.leftUser.InteractWithMedium(centerRightPost)
        self.assertEquals(centerRightPost.visibility_score, 0,
                          "LeftUser should ignore centerRightPost.")
        self.centerUser.InteractWithMedium(centerRightPost)
        self.assertEquals(centerRightPost.visibility_score, 1,
                          "CenterUser should vote for centerRightPost.")
        self.rightUser.InteractWithMedium(centerRightPost)
        self.assertEquals(centerRightPost.visibility_score, 1,
                          "RightUser should ignore centerRightPost.")

    def test_InteractWithMedium_rightPost(self):
        rightPost = Post(4, 0.55, "I just want lower taxes.")
        self.leftUser.InteractWithMedium(rightPost)
        self.assertEquals(rightPost.visibility_score, -1,
                          "LeftUser should vote against rightPost.")
        self.centerUser.InteractWithMedium(rightPost)
        self.assertEquals(rightPost.visibility_score, -1,
                          "CenterUser should ignore rightPost.")
        self.rightUser.InteractWithMedium(rightPost)
        self.assertEquals(rightPost.visibility_score, 0,
                          "RightUser should ignore rightPost.")

    def test_InteractWithMedium_farRightPost(self):
        farRightPost = Post(5, 0.85, "The poor are destroying society!")
        self.leftUser.InteractWithMedium(farRightPost)
        self.assertEquals(farRightPost.visibility_score, -1,
                          "LeftUser should vote against RightPost.")
        self.centerUser.InteractWithMedium(farRightPost)
        self.assertEquals(farRightPost.visibility_score, -2,
                          "CenterUser should vote against farRightPost.")
        self.rightUser.InteractWithMedium(farRightPost)
        self.assertEquals(farRightPost.visibility_score, -2,
                          "RightUser should ignore farRightPost.")

    def test_InteractWithMedium_votingTwice(self):
        medium = Medium(1, 0.)
        self.centerUser.InteractWithMedium(medium)
        self.assertEquals(medium.visibility_score, 1)
        self.centerUser.InteractWithMedium(medium)
        self.assertEquals(medium.visibility_score, 1,
                          "User shoud not be allowed to vote twice.")

if __name__ == '__main__':
    unittest.main()
