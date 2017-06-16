# iterators are used to iterate the items of the container. python uses iter()
# method to return an iterator object of class.The iterator method uses the
# __next__() method to get the next item. When the iteration is done an
# StopIteration exception is raised.

#iterator always returns an iterable object....


class Reverse:
    def __init__(self, name):
        self.name = name
        self.index = len(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index-1
        return self.name[self.index]

if __name__ == "__main__":
    r = Reverse('amardeep')
    for char in r:
        print(char)
