
class Snake:
    def __init__(self):
        self.name = 'Unnamed'
        self.species = 'Snake'
        self.prey = []

    def __str__(self):
        return '{} {}'.format(self.name, self.species)


class Zebra:
    def __init__(self):
        self.name = 'Unnamed'
        self.species = 'Zebra'
        self.prey = ['Snake']

    def __str__(self):
        return '{} {}'.format(self.name, self.species)


class Lion:
    def __init__(self):
        self.name = 'Unnamed'
        self.species = 'Lion'
        self.prey = ['Zebra']

    def __str__(self):
        return '{} {}'.format(self.name, self.species)


class Cage:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        # check if current animal is the prey for any other animal already in the cage

        for item in self.animals:
            if animal.species in item.prey:
                # don't add current animal to the list
                print('Oh no! Seems like you put a predator\'s prey in the cage!')
                print('{} has eaten {}!'.format(item, animal))
                return

        # no one is the predator of current animal, check if any prey is already in the cage
        for prey in animal.prey:
            for item in self.animals:
                if prey == item.species:
                    # found a prey
                    print('Oh no! Seems like you put a prey in a predator\'s cage!')
                    print('{} has eaten {}!'.format(animal, item))
                    self.animals.remove(item)

        self.animals.append(animal)

    def animals_inside(self):
        if len(self.animals) is 0:
            print('This cage is empty.')
        else:
            print('Animals in this cage: {}.'.format([str(x) for x in self.animals]))


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cage(self, cage):
        self.cages.append(cage)

    def n_of_cages(self):
        return len(self.cages)


zoo = Zoo()
for i in range(4):
    zoo.add_cage(Cage())

snake = Snake()
lion = Lion()
zebra = Zebra()

snake.name = 'Venom'
lion.name = 'Leo'
zebra.name = 'Stripy'

zoo.cages[0].add_animal(snake)
zoo.cages[0].add_animal(zebra)
zoo.cages[0].animals_inside()

zoo.cages[0].add_animal(lion)
zoo.cages[0].animals_inside()
