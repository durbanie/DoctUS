# A 'User' interacts with the Forum by subscribing to Boards, making Posts,
# adding Comments, and voting on/interacting with media.

class User:
    """
    This class represents a user who interacts with the Forum by subscribing to
    Boards, making Posts, and voting.
    """
    def __init__(self, id, political_bias, interaction_model=None):
        """
        Constructor used to create a new instance of a User.

        Args:
            id: An `int` specifying the id of the user.
            political_bias: A `float` between -1. and 1. defining the users
                political biases on the U.S.-centric spectrum, with -1. being
                far left and 1. being far right.
            interaction_model: A model for how users interact with media (i.e.
                vote for, against, or ignore).
        """
        self._id = id
        self._political_bias = political_bias
        self._interaction_model = interaction_model

    @property
    def id(self):
        """The user's ID (a positive `int`)."""
        return self._id

    @property
    def political_bias(self):
        """The user's political bias (a `float` between -1. and 1.)."""
        return self._political_bias

    def InteractWithMedium(self, media):
        """
        Provided media, determines whether or not to vote for, against, or
        ignore, based on the media's leanings, and this user's affinity_range
        and/or tolerance_range.

        Args:
            media: The `Media` that this user will vote on.
        """
        # Make sure the model is defined. If not, just ignore the post (i.e. the
        # lurker strategy).
        if self._interaction_model is None:
            return

        # Don't let the user vote more than once.
        if not media.HasUserVoted(self.id):
            self._interaction_model.ModelInteraction(self, media)
