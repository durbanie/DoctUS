# A 'User' interacts with the Forum by subscribing to Boards, making Posts,
# adding Comments, and voting.

class User:
    """
    This class represents a user who interacts with the Forum by subscribing to
    Boards, making Posts, and voting.
    """
    def __init__(self, id, political_bias, affinity_range, tolerance_range):
        """
        Constructor used to create a new instance of a User.
        
        Args:
            id: An `int` specifying the id of the user.
            political_bias: A `float` between -1. and 1. defining the users
                political biases on the U.S.-centric spectrum, with -1. being
                far left and 1. being far right.
            affinity_range: A `float` (>0. and <1.) defining the user's range of
                acceptance for voting for like-minded posts/comments.
            tolerance_range: A `float` defining the user's tolerance for
                dissent. Users may vote against posts or comments beyond this
                range. For consistency, this must be greater than their
                affinity_range.
        """
        self._id = id
        self._political_bias = political_bias
        self._affinity_range = affinity_range
        self._tolerance = tolerance

    def InteractWithPost(self, post):
        """
        Provided a post, determines whether or not to upvote, downvote, or
        ignore, based on the post's leanings, and this user's affinity_range
        and/or tolerance.
        
        Args:
            post: The `Post` that this user will vote on.
        """

        # Don't let the user vote more than once.
        if not post.HasUserVoted(self._id):
            political_difference = abs(
                post.GetPoliticalBias() - self._political_bias)
            if political_difference < self._affinity_range:
                post.VoteFor(self._id)
            if political_difference > self._tolerance_range:
                post.VoteAgainst(self._id)
        
