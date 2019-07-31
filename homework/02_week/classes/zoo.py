class Animal:
    """ Can be placed inside cages, and according to its place in food chain
    it has a list attribute of its prey (what it likes to eat).
    """
    prey = []

    def __init__(self, name):
        self.name = 'Unnamed' if not name else name  # Default naming, to be modified

    def __repr__(self):
        """ Identifies the Animal by its name and species (subclass).
        """
        species = self.__class__.__name__
        return self.name + " " + species if self.name != 'Unnamed' else species


class Mouse(Animal):
    pass

class Goat(Animal):
    pass

class Rabbit(Animal):
    prey = [Mouse]


class Jackal(Animal):
    prey = [Goat, Rabbit]


class Owl(Animal):
    prey = [Mouse]


class Snake(Animal):
    prey = [Mouse]


class Kite(Animal):
    prey = [Snake]


class WildCat(Animal):
    prey = [Rabbit, Mouse]


class Lion(Animal):
    prey = [Goat, Jackal, WildCat, Kite]


class Cage:
    """ Contains a list of animals inside and performs methods to check
    intern competition where there might be a conflict of prey and predator,
    where a prey gets eaten.
    """

    def __init__(self):
        self.animals_list = []
        self.name = 'Cage'  # Default name configuration

    def __repr__(self):
        if len(self.animals_list) > 0:  # Checks if cage isn't empty
            return "{} contains {} animal(s): {}".format(
                self.name, self.n_of_animals(),
                ', '.join(map(str, self.animals_list)))
        else:
            return "{} (empty)".format(self.name)

    def n_of_animals(self):
        return len(self.animals_list)

    def check_prey(self):
        """ Method for checking the animals chain food competition inside a
        cage: iterates through its animals list and kills (deletes) the
        predator's prey.
        """
        death_statements = {}  # Dictionary to handle preys getting eaten

        # Check if any animals in the list have listed prey inside this cage:
        for predator in self.animals_list:
            for prey in self.animals_list:  # Parses animals prey's lists
                """ Compares the listed classes in an animal's prey list
                with the class of each other animal on the cage. """
                if type(prey) in predator.prey:
                    death_statements[prey] = (prey, "{} got eaten by {}."
                                              .format(prey, predator))

        if len(death_statements) > 0:  # Checks if there were any deaths
            print("Oops! Seems like you put predator and prey on same cage.")
            for prey in death_statements:
                print(death_statements[prey][1])  # Prints name of prey
                self.animals_list.remove(death_statements[prey][0])
                # Prints statement of death identifying the predator

        print('Now ' + str(self))  # Shows updated list of animals in cage

    def add_animals(self, add_list):
        """ Inserts animals inside the Cage object. """
        duplicate_animals = []

        for animal in add_list:
            """ Checks if the parent class of the list item is not an Animal
            object (in this case, the item won't be inserted in the Cage)
            """
            if animal.__class__.__base__ != Animal:
                print("{} object could not be added because it's not an "
                      "Animal subclass.".format(animal.__class__.__name__))
            elif animal not in self.animals_list:
                self.animals_list.append(animal)
                # Inserts Animal object in cage if not already inside
            elif animal not in duplicate_animals:
                duplicate_animals.append(animal)

        if len(duplicate_animals) > 0:  # Checks duplicate insert attempt
            print("Duplicate animal(s) found: {} already inside.".format(
                ', '.join(map(str, duplicate_animals))))
            print(self)

        return self.check_prey()
        # Starts check on whether there is prey and predator on the same cage


class Zoo:
    """ Contains a list of Cage objects and informs about the animals inside
    itself.
    """

    def __init__(self):
        super().__init__()
        self.name = 'Zoo'  # Default name
        self.cages = []

    def __repr__(self):
        if len(self.cages) > 0:
            return '{} contains {} cage(s) and a total of {} animal(s)'.format(
                self.name, len(self.cages), self.n_of_animals())
        else:
            return '{} (empty)'.format(self.name)

    def add_cages(self, list_to_add):  # Takes list of cages as argument
        for cage in list_to_add:
            if type(cage) == Cage:
                self.cages.append(cage)
            else:
                print("{} object could not be added because it's not a Cage."
                      .format(cage.__class__.__name__))
        return self

    def n_of_cages(self):  # User method to find out number of cages
        return len(self.cages)

    def n_of_animals(self):
        """ Accessing attributes from instances of class Cage, it calculates
        how many animals are in total inside all cages of the zoo.
        """
        self.n_of_animals = 0
        for item in self.cages:
            # Appends to attribute sum of animals inside each cage
            self.n_of_animals += len(item.animals_list)
        return self.n_of_animals


if __name__ == '__main__':
    london_zoo = Zoo()
    cage_1 = Cage()
    cage_7 = Cage()
    cage_2 = Cage()
    cage_5 = Cage()

    london_zoo.cages = [cage_1, cage_7, cage_2, cage_5]  # Populate Zoo with cages
    print(london_zoo.n_of_cages())

    snake_3 = Snake('Rattle')
    snake_5 = Snake('Salmon')

    rabbit_1 = Rabbit('Duffy')
    rabbit_2 = Rabbit('Nicey')
    cage_5.add_animals([snake_3, snake_5, rabbit_1, rabbit_2])
    print(cage_5.animals_list)

    del cage_5.animals_list[1]
    cage_5.add_animals([Jackal('Bohoo')])

    print(london_zoo)