from user import User
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
        self.assertEquals(self.rightUser.GetId(), RIGHT_ID,
                          "Right-leaning User ID incorrect.")
        self.assertEquals(self.rightUser.GetPoliticalBias(), 0.5,
                          "Right-leaning User political bias incorrect.")
        self.assertEquals(self.centerUser.GetId(), CENTER_ID,
                          "Centrist User ID incorrect.")
        self.assertEquals(self.centerUser.GetPoliticalBias(), 0.,
                          "Centrist User political bias incorrect.")
        self.assertEquals(self.leftUser.GetId(), LEFT_ID,
                          "Left-leaning User ID incorrect.")
        self.assertEquals(self.leftUser.GetPoliticalBias(), -0.5,
                          "Left-leaning User political bias incorrect.")

    def test_InteractWithPost_farLeftPost(self):
        farLeftPost = Post(0, -0.85)
        self.leftUser.InteractWithPost(farLeftPost)
        self.assertEquals(farLeftPost.GetVisibilityScore(), 0,
                          "LeftUser should ignore farLeftPost.")
        self.centerUser.InteractWithPost(farLeftPost)
        self.assertEquals(farLeftPost.GetVisibilityScore(), -1,
                          "CenterUser should vote against farLeftPost.")
        self.rightUser.InteractWithPost(farLeftPost)
        self.assertEquals(farLeftPost.GetVisibilityScore(), -2,
                          "RightUser should vote against farLeftPost.")

    def test_InteractWithPost_leftPost(self):
        leftPost = Post(1, -0.55)
        self.leftUser.InteractWithPost(leftPost)
        self.assertEquals(leftPost.GetVisibilityScore(), 1,
                          "LeftUser should vote for leftPost.")
        self.centerUser.InteractWithPost(leftPost)
        self.assertEquals(leftPost.GetVisibilityScore(), 1,
                          "CenterUser should ignore leftPost.")
        self.rightUser.InteractWithPost(leftPost)
        self.assertEquals(leftPost.GetVisibilityScore(), 0,
                          "RightUser should vote against leftPost.")

    def test_InteractWithPost_centerLeftPost(self):
        centerLeftPost = Post(2, -0.05)
        self.leftUser.InteractWithPost(centerLeftPost)
        self.assertEquals(centerLeftPost.GetVisibilityScore(), 0,
                          "LeftUser should ignore centerLeftPost.")
        self.centerUser.InteractWithPost(centerLeftPost)
        self.assertEquals(centerLeftPost.GetVisibilityScore(), 1,
                          "CenterUser should vote for centerLeftPost.")
        self.rightUser.InteractWithPost(centerLeftPost)
        self.assertEquals(centerLeftPost.GetVisibilityScore(), 1,
                          "RightUser should ignore centerLeftPost.")

    def test_InteractWithPost_centerRightPost(self):
        centerRightPost = Post(3, 0.05)
        self.leftUser.InteractWithPost(centerRightPost)
        self.assertEquals(centerRightPost.GetVisibilityScore(), 0,
                          "LeftUser should ignore centerRightPost.")
        self.centerUser.InteractWithPost(centerRightPost)
        self.assertEquals(centerRightPost.GetVisibilityScore(), 1,
                          "CenterUser should vote for centerRightPost.")
        self.rightUser.InteractWithPost(centerRightPost)
        self.assertEquals(centerRightPost.GetVisibilityScore(), 1,
                          "RightUser should ignore centerRightPost.")

    def test_InteractWithPost_rightPost(self):
        rightPost = Post(4, 0.55)
        self.leftUser.InteractWithPost(rightPost)
        self.assertEquals(rightPost.GetVisibilityScore(), -1,
                          "LeftUser should vote against rightPost.")
        self.centerUser.InteractWithPost(rightPost)
        self.assertEquals(rightPost.GetVisibilityScore(), -1,
                          "CenterUser should ignore rightPost.")
        self.rightUser.InteractWithPost(rightPost)
        self.assertEquals(rightPost.GetVisibilityScore(), 0,
                          "RightUser should ignore rightPost.")

    def test_InteractWithPost_farRightPost(self):
        farRightPost = Post(5, 0.85)
        self.leftUser.InteractWithPost(farRightPost)
        self.assertEquals(farRightPost.GetVisibilityScore(), -1,
                          "LeftUser should vote against RightPost.")
        self.centerUser.InteractWithPost(farRightPost)
        self.assertEquals(farRightPost.GetVisibilityScore(), -2,
                          "CenterUser should vote against farRightPost.")
        self.rightUser.InteractWithPost(farRightPost)
        self.assertEquals(farRightPost.GetVisibilityScore(), -2,
                          "RightUser should ignore farRightPost.")
        pass

if __name__ == '__main__':
    unittest.main()
