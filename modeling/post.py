# A 'Post' holds content that Users can interact with, including voting for or
# against it and commenting on it. Posts need to keep track of a visibility
# score which pushes it to the top of the board. Posts also need to track who
# already voted on them.

from sets import Set

class InvalidAction(Exception):
    """Raised when a user attempts an invalid action."""
    pass

class Post:
    """
    This class represents a post, which holds content that Users can interact
    with, including voting for or against it and commenting on it. Posts need
    to keep track of a visibility score which pushes it to the top of the
    board. Posts also need to track who already voted on them.             
    """
    def __init__(self, id, political_bias):
        """
        Constructor to create a new instance of a Post.

        Args:
            id: An `int` specifying the id of the post.
            political_bias: A `float` between -1. and 1. defining the users
                political biases on the U.S.-centric spectrum, with -1. being
                far left and 1. being far right.
        """
        self._id = id
        self._political_bias = political_bias
        self._visibility_score = 0
        self._already_voted = Set([])

    def GetVisibilityScore(self):
        """
        Gets the visibility score, indicating where in the visibility hierarchy
        the post should be.

        Returns:
            An `int` that can be positive or negative, and is unbounded,
            representing the visibility score.
        """
        return self._visiblity_score

    def GetPoliticalBias(self):
        """
        """
        return self._political_bias

    def HasUserVoted(self, user_id):
        """
        Determines whether or not the user with the provided user_id has already
        voted.

        Args:
            user_id: An `int` specifying the id of the user to check.

        Returns:
            A `boolean` that is TRUE if the user has already voted, and FALSE
            otherwise.
        """
        return user_id in self._already_voted

    def VoteFor(self, user_id):
        """
        Votes for
        """
        self._Vote(user_id, 1)

    def VoteAgainst(self, user_id):
        """
        """
        self._Vote(user_id, -1)

    def _Vote(self, user_id, value):
        if self.HasUserVoted(user_id):
            raise InvalidAction("User attempted to vote multiple times.")
        self._visibility_score += value
        self._already_voted.add(user_id)
