import itertools as it
from utils import timefunc


class Battle_Ram:
    def __init__(self, charset, length):
        self.charset = charset
        self.length = length


    def crackit(self, password):
        pass

    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield  ''.join(guess)

@timefunc
def main():
    brute = Battle_Ram('abcdefghijklmnop', 6)
    for guess in brute.guesses:
        print(guess)




if __name__ == '__main__':
    main()
