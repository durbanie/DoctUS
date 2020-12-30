# A class which builds a population of Users with extremely simple properties.
# The population is focused entirely on voting based on political position,

from medium import Medium
from user import User
from voting.low_discourse import LowDiscourse
from numpy.random import Generator, PCG64

class PopulationBuilder:
    def __init__(self, num_users):
        self._num_users = num_users
        self._generator = Generator(PCG64())

    @property
    def num_users(self):
        return self._num_users

    def CreatePopulation(self, alpha, beta, affinity=0.01, tolerance=0.01):
        users = []
        user_biases = self._generator.beta(alpha, beta, self.num_users) * 2 - 1
        model = LowDiscourse(affinity, tolerance)
        for id, bias in enumerate(user_biases):
            users.append(User(id, bias, model))
        return users

if __name__ == '__main__':
    builder = PopulationBuilder(10000)
    users = builder.CreatePopulation(1.25, 1.73, 0.3, 0.6)

    leftPost = Medium(1, -0.5)
    centerPost = Medium(2, 0)
    rightPost = Medium(3, 0.5)

    def classify(user):
        if user.political_bias < -0.33:
            return "liberal"
        if user.political_bias > 0.33:
            return "conservative"
        return "moderate"

    population_biases = {
        "liberal": 0,
        "moderate": 0,
        "conservative": 0
    }
    for user in users:
        population_biases[classify(user)] += 1
        user.InteractWithMedium(leftPost)
        user.InteractWithMedium(centerPost)
        user.InteractWithMedium(rightPost)

    print(population_biases)
    print(leftPost.visibility_score)
    print(centerPost.visibility_score)
    print(rightPost.visibility_score)
