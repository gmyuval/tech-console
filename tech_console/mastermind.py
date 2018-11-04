import random
from bitarray import bitarray
from typing import List, Optional

from .config import DEFAULT_NODE_WEIGHT, INPUT_LENGTH, ALLOWED_GUESSES


class Mastermind(object):
    def __init__(self, input_length: int = INPUT_LENGTH, allowed_guesses: int = ALLOWED_GUESSES,
                 weight_mask: List[int] = None) -> None:
        self.__desired_state: bitarray = None
        self.desired_weight: int = None
        self.input_length = input_length
        self.__allowed_guesses = allowed_guesses
        self.__weights = weight_mask or [DEFAULT_NODE_WEIGHT ** i for i in range(input_length)]
        self.__current_guess = 0
        self.reset_game()

    def guess(self, input_str: bitarray) -> Optional[int]:
        if input_str == self.__desired_state:
            return None
        self.__current_guess += 1
        if self.__current_guess > self.__allowed_guesses:
            self.reset_game()
        return sum([int(i) * w for i, w in zip(input_str, self.__weights)])

    def reset_game(self) -> None:
        self.__desired_state = \
            bitarray('{0:b}'.format(random.SystemRandom().getrandbits(self.input_length)).zfill(self.input_length))
        self.desired_weight = sum([int(i) * w for i, w in zip(self.__desired_state, self.__weights)])
        self.__current_guess = 0
