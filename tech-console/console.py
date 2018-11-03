import sys
from subprocess import Popen, PIPE

from prompt_toolkit import prompt, PromptSession
from prompt_toolkit import print_formatted_text as print
from bitarray import bitarray

from mastermind import Mastermind
from config import PROMPT


class TechConsole(object):
    def __init__(self, prompt_text: str = PROMPT, debug: bool = False) -> None:
        self.session = PromptSession()
        self.prompt_text = prompt_text
        self.debug = debug

    def runrepair(self):
        mm = Mastermind()
        print('=== Daedalus repair console ===')
        while True:
            input_string = self.session.prompt('provide repair string: ')
            if input_string == 'exit':
                print('Exiting repair console')
                break
            if not set(input_string).issubset({'0', '1'}):
                print('Repair string should only contain "0"\'s and "1"\'s')
                continue
            input_string = bitarray(input_string)
            res = mm.guess(input_string)
            if res is None:
                print('repaired')
            else:
                print(res)

    @staticmethod
    def clear() -> None:
        p = Popen(['clear'])
        p.communicate()

    def run(self) -> None:
        while True:
            cmd = None
            try:
                cmd = self.session.prompt(self.prompt_text)
            except KeyboardInterrupt:
                print('CTRL-C pressed')
            except EOFError:
                print('CTRL-D pressed')
            if cmd == 'exit':
                self.exit()
            if cmd == 'repair':
                self.runrepair()
            if cmd == 'clear':
                self.clear()
            print('cmd is {}'.format(cmd))

    def exit(self):
        sys.exit(0)


if __name__ == '__main__':
    console = TechConsole()
    console.run()