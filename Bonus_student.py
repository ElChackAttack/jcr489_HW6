import random

random.seed(0)

SIZE = 10
LOGGING = True

class PancakeStack():
    def __init__(self, stack = None):
        self.stack = stack

    def get_size(self):
        return len(self.stack)

    # All of the pancakes are sorted after index
    # Returns the index of largest unsorted pancake
    def find_largest_pancake(self, index):
        largest_pancake = self.stack[index]
        largest_index = index

        for i in range(index):
            if self.stack[i] > largest_pancake:
                largest_pancake = self.stack[i]
                largest_index = i

        if LOGGING:
            print("Insert the pan at index %d with the largest in flip as %d" \
                  %(largest_index, largest_pancake))
        return largest_index

    # Slide the pan under pancake at desired index and flip to top
    def flip(self, index):
        new_stack = self.stack[:(index + 1)]
        new_stack.reverse()
        new_stack += self.stack[(index + 1):]
        self.stack = new_stack
        return


def sort_pancakes(pancakes):
    pancakes_size = pancakes.get_size()
    for i in reversed(range(pancakes_size)):
        flip_index = pancakes.find_largest_pancake(i)
        pancakes.flip(flip_index)
        if LOGGING: print("Flip Up", pancakes.stack)
        pancakes.flip(i)
        if LOGGING: print("Flip Down", pancakes.stack)
    return pancakes.stack


if __name__ == "__main__":
    my_stack = random.sample(range(1, 20), SIZE)
    print("Unsorted pancakes:", my_stack)
    case_one = PancakeStack(my_stack)
    print("Final order of pancakes: ", sort_pancakes(case_one))

    
    
