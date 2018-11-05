class Animal(object):

    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'Animal {self.name} moved.')

class Horse(Animal):
    def __init__(self, name, color):
        self.color = color
        super().__init__(name)

    def move(self):
        print(f'Horse {self.name} run.')

    def jump(self, how_high):
        if how_high > 5:
            print(f'Horse {self.name} jumped high.')
        else:
            print(f'Horse {self.name} jumped low.')

class Donkey(Animal):
    def __init__(self, stubborn):
    # def __init__(self, stubborn, owner, hungry):
        self.stubborn = stubborn
        # self.owner = owner
        # self.hungry = hungry
        super().__init__('unknown')

    def move(self):
        if self.stubborn > 8:
            print('Donkey is stubborn, won\'t move')
        else:
            print('Donkey moved a bit.')

class Mule(Horse, Donkey):
    def __init__(self, name, color):
        super().__init__(name, color)


if __name__ == '__main__':
    e_Mule = Mule('stefan', 'czarny')
    print(e_Mule.name)
# Method resolution order mro
    #print(help(Mule))
    # print(Mule.mro())
    # print(Mule.__mro__)