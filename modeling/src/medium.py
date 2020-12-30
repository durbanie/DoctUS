# A 'Medium' (e.g. comment or post) holds content that Users can interact with,
# including voting for or against it and commenting on it. Media need to keep
# track of a visibility score which pushes them to the top of the board or
# comment chain. Media also need to track who already voted on them, and raise
# exceptions if Users try to vote more than once.

class InvalidAction(Exception):
    """Raised when a user attempts an invalid action."""
    pass

class Medium:
    """
    This class represents a medium (e.g. comment or post), which holds content
    that users can interact with, including voting for or against it and
    commenting on it. Media need to keep track of a visibility score which
    pushes them to the top of the board. Media also need to track who already
    voted on them, and raise exceptions if users try to vote more than once.
    """
    def __init__(self, id, political_bias):
        """
        Constructor to create a new instance of a Medium.

        Args:
            id: A positive `int` specifying the ID of the medium.
            political_bias: A `float` between -1. and 1. defining the medium's
                political bias on the U.S.-centric spectrum, with -1. being
                far left and 1. being far right.
        """
        self._id = id
        self._political_bias = political_bias
        self._visibility_score = 0
        self._already_voted = set([])

    @property
    def id(self):
        """A positive `int` specifying the ID of the medium's."""
        return self._id

    @property
    def political_bias(self):
        """
        A `float` between -1. and 1. defining the medium's political bias on the
        U.S.-centric spectrum, with -1. being far left and 1. being far right.
        """
        return self._political_bias

    @property
    def visibility_score(self):
        """
        An unbounded `int` representing the visibility score, indicating where
        in the visibility hierarchy (position on the board or rank in the
        comment list) the medium should be.
        """
        return self._visibility_score

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
        Allows the user with the provided user_id to vote for the medium (i.e.
        increase its visibility.).

        Args:
            user_id: The ID of the user attempting to vote.

        Raises:
            InvalidAction: If the user has already voted.
        """
        self._Vote(user_id, 1)

    def VoteAgainst(self, user_id):
        """
        Allows the user with the provided user_id to vote against the medium
        (i.e. decrease its visibility.).

        Args:
            user_id: The ID of the user attempting to vote.

        Raises:
            InvalidAction: If the user has already voted.
        """
        self._Vote(user_id, -1)

    def _Vote(self, user_id, value):
        if self.HasUserVoted(user_id):
            raise InvalidAction("User attempted to vote multiple times.")
        self._visibility_score += value
        self._already_voted.add(user_id)
