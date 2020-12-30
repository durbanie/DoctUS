from voting.low_discourse import LowDiscourse
from post import Post
from user import User

import unittest

RIGHT_ID = 0
CENTER_ID = 1
LEFT_ID = 2

class LowDiscourseTest(unittest.TestCase):
    def setUp(self):
        self.leftUser = User(LEFT_ID, -0.5)
        self.centerUser = User(CENTER_ID, 0.)
        self.rightUser = User(RIGHT_ID, 0.5)
        self.model = LowDiscourse(0.1, 0.6)

    def test_InteractWithMedium_farLeftPost(self):
        farLeftPost = Post(0, -0.85, "Eat the rich!")
        self.model.ModelInteraction(self.leftUser, farLeftPost)
        self.assertEquals(farLeftPost.visibility_score, 0,
                          "LeftUser should ignore farLeftPost.")
        self.model.ModelInteraction(self.centerUser, farLeftPost)
        self.assertEquals(farLeftPost.visibility_score, -1,
                          "CenterUser should vote against farLeftPost.")
        self.model.ModelInteraction(self.rightUser, farLeftPost)
        self.assertEquals(farLeftPost.visibility_score, -2,
                          "RightUser should vote against farLeftPost.")

    def test_InteractWithMedium_leftPost(self):
        leftPost = Post(1, -0.55, "I just want affordable healthcare.")
        self.model.ModelInteraction(self.leftUser, leftPost)
        self.assertEquals(leftPost.visibility_score, 1,
                          "LeftUser should vote for leftPost.")
        self.model.ModelInteraction(self.centerUser, leftPost)
        self.assertEquals(leftPost.visibility_score, 1,
                          "CenterUser should ignore leftPost.")
        self.model.ModelInteraction(self.rightUser, leftPost)
        self.assertEquals(leftPost.visibility_score, 0,
                          "RightUser should vote against leftPost.")

    def test_InteractWithMedium_centerLeftPost(self):
        centerLeftPost = Post(
            2, -0.05, "Capitalism should be constrained for the public good.")
        self.model.ModelInteraction(self.leftUser, centerLeftPost)
        self.assertEquals(centerLeftPost.visibility_score, 0,
                          "LeftUser should ignore centerLeftPost.")
        self.model.ModelInteraction(self.centerUser, centerLeftPost)
        self.assertEquals(centerLeftPost.visibility_score, 1,
                          "CenterUser should vote for centerLeftPost.")
        self.model.ModelInteraction(self.rightUser, centerLeftPost)
        self.assertEquals(centerLeftPost.visibility_score, 1,
                          "RightUser should ignore centerLeftPost.")

    def test_InteractWithMedium_centerRightPost(self):
        centerRightPost = Post(
            3, 0.05, "We should examine the merits of a flat tax system.")
        self.model.ModelInteraction(self.leftUser, centerRightPost)
        self.assertEquals(centerRightPost.visibility_score, 0,
                          "LeftUser should ignore centerRightPost.")
        self.model.ModelInteraction(self.centerUser, centerRightPost)
        self.assertEquals(centerRightPost.visibility_score, 1,
                          "CenterUser should vote for centerRightPost.")
        self.model.ModelInteraction(self.rightUser, centerRightPost)
        self.assertEquals(centerRightPost.visibility_score, 1,
                          "RightUser should ignore centerRightPost.")

    def test_InteractWithMedium_rightPost(self):
        rightPost = Post(4, 0.55, "I just want lower taxes.")
        self.model.ModelInteraction(self.leftUser, rightPost)
        self.assertEquals(rightPost.visibility_score, -1,
                          "LeftUser should vote against rightPost.")
        self.model.ModelInteraction(self.centerUser, rightPost)
        self.assertEquals(rightPost.visibility_score, -1,
                          "CenterUser should ignore rightPost.")
        self.model.ModelInteraction(self.rightUser, rightPost)
        self.assertEquals(rightPost.visibility_score, 0,
                          "RightUser should ignore rightPost.")

    def test_InteractWithMedium_farRightPost(self):
        farRightPost = Post(5, 0.85, "The poor are destroying society!")
        self.model.ModelInteraction(self.leftUser, farRightPost)
        self.assertEquals(farRightPost.visibility_score, -1,
                          "LeftUser should vote against RightPost.")
        self.model.ModelInteraction(self.centerUser, farRightPost)
        self.assertEquals(farRightPost.visibility_score, -2,
                          "CenterUser should vote against farRightPost.")
        self.model.ModelInteraction(self.rightUser, farRightPost)
        self.assertEquals(farRightPost.visibility_score, -2,
                          "RightUser should ignore farRightPost.")

if __name__ == '__main__':
    unittest.main()
