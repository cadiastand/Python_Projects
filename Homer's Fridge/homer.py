"""
Homer's fridge
Course: B0B36ZAL
"""

#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
#predesly kod nijak nemodifikujte!

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
# openFridge(fridge)


"""
Task #1
"""
def maxExpirationDay(fridge):
    if not fridge:
        return -1
    return max(food.expiration for food in fridge)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""
def histogramOfExpirations(fridge):
    max_expiration = maxExpirationDay(fridge)
    histogram = [0] * (max_expiration + 1)
    for food in fridge:
        histogram[food.expiration] += 1
    return histogram

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]


"""
Task #3
"""
def cumulativeSum(histogram):
    cumulative = [0] * len(histogram)
    cumulative[0] = histogram[0]
    for i in range(1, len(histogram)):
        cumulative[i] = cumulative[i - 1] + histogram[i]
    return cumulative

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(cumulativeSum([0, 2, 0, 1, 1]))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""
def sortFoodInFridge(fridge):
    histogram = histogramOfExpirations(fridge)
    cumulative = cumulativeSum(histogram)
    sorted_fridge = [None] * len(fridge)
    positions = cumulative[:]
    for food in fridge:
        pos_ind = positions[food.expiration] - 1
        sorted_fridge[pos_ind] = food
        positions[food.expiration] -= 1
    return sorted_fridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""
def reverseFridge(fridge):
    reversed_fridge = fridge[:]
    for i in range(len(fridge) // 2):
        reversed_fridge[i], reversed_fridge[-(i + 1)] = reversed_fridge[-(i + 1)], reversed_fridge[i]
    return reversed_fridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""
def eatFood(name, fridge):
    fridge_copy = fridge[:]
    min_expiration = None
    food_index = None
    for i, food in enumerate(fridge_copy):
        if food.name == name:
            if min_expiration is None or food.expiration < min_expiration:
                min_expiration = food.expiration
                food_index = i
    if food_index is not None:
        fridge_copy.pop(food_index)
    return fridge_copy

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 3), Food("donut", 1), Food("donut", 6)]
#     ))
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)
