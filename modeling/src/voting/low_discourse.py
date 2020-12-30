# A voting model which decides based on political leanings alone.

class LowDiscourse:
    """
    This class represents a model where the user votes entirely based on their
    political leanings relative to the medium they are voting on.
    """
    def __init__(self, affinity_range, tolerance_range):
        """
        Constructor used to create a new instance of LowDiscourse.

        Args:
            affinity_range: A `float` (>0. and <1.) defining the user's range of
                acceptance for voting for like-minded posts/comments.
            tolerance_range: A `float` defining the user's tolerance for
                dissent. Users may vote against posts or comments beyond this
                range. For consistency, this must be greater than their
                affinity_range.
        """
        self._affinity_range = affinity_range
        self._tolerance_range = tolerance_range

    def ModelInteraction(self, user, media):
        """
        Provided the user, and the media, determines whether or not the user
        votes for, against, or ignore the media.

        Args:
            user: The `User` that is deciding whether or not to vote.
            media: The `media` that the user is voting on.
        """
        political_difference = abs(user.political_bias - media.political_bias)
        if political_difference < self._affinity_range:
            media.VoteFor(user.id)
        if political_difference > self._tolerance_range:
            media.VoteAgainst(user.id)
