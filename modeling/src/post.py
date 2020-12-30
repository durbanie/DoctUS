# A 'Post' is a 'Medium' that holds content.

from medium import Medium

class Post(Medium):
    """
    This class represents a post, which holds content that Users can interact
    with, including voting for or against it and commenting on it. Posts need
    to keep track of a visibility score which pushes it to the top of the
    board. Posts also need to track who already voted on them.
    """
    def __init__(self, id, political_bias, content):
        """
        Constructor to create a new instance of a Post.

        Args:
            id: An `int` specifying the id of the post.
            political_bias: A `float` between -1. and 1. defining the users
                political biases on the U.S.-centric spectrum, with -1. being
                far left and 1. being far right.
            content: A `string` describing the content.
        """
        Medium.__init__(self, id, political_bias)
        self._content = content

    @property
    def content(self):
        """A `string` describing the content."""
        return self._content
