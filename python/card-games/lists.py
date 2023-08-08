"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


JACK_CARD = 11


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number + increment for increment in [0, 1, 2]]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    sum_of_hand = sum(hand)
    cards_in_hand = len(hand)

    return sum_of_hand / cards_in_hand


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values )
    OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    first_card = hand[0]
    last_card = hand[-1]
    average_of_first_and_last_cards = card_average([first_card, last_card])

    cards_in_hand = len(hand)
    median_card_index = (cards_in_hand - 1) // 2
    median_of_hand = hand[median_card_index]

    return card_average(hand) in [average_of_first_and_last_cards, median_of_hand]


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_cards = hand[1::2]
    even_cards_average = card_average(even_cards)

    odd_cards = hand[::2]
    odd_cards_average = card_average(odd_cards)

    return even_cards_average == odd_cards_average


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == JACK_CARD:
        return hand[:-1] + [JACK_CARD * 2]

    return hand
