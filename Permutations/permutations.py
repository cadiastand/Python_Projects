class Node:
    def __init__(self, value, remaining):
        self.value = value
        self.remaining = remaining
        self.children = []

    def generate_permutations(self):
        if not self.remaining:
            return [[self.value]]

        permutations = []
        for i, elem in enumerate(self.remaining):
            child = Node(elem, self.remaining[:i] + self.remaining[i + 1:])
            self.children.append(child)

            for perm in child.generate_permutations():
                permutations.append([self.value] + perm)
        return permutations


def permutations(array):
    if not array:
        return [[]]

    result = []
    for i, elem in enumerate(array):
        root = Node(elem, array[:i] + array[i + 1:])
        result += root.generate_permutations()

    return result
