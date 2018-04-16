from Deck import *


class Hand(object):
    LEVEL_VALUE = 15

    ROYAL_FLUSH_VALUE = LEVEL_VALUE ** 10
    STRAIGHT_FLUSH_VALUE = LEVEL_VALUE ** 9
    FOUR_OF_A_KIND_VALUE = LEVEL_VALUE ** 8
    FULL_HOUSE_VALUE = LEVEL_VALUE ** 7
    FLUSH_VALUE = LEVEL_VALUE ** 6
    STRAIGHT_VALUE = LEVEL_VALUE ** 5
    THREE_OF_A_KIND_VALUE = LEVEL_VALUE ** 4
    TWO_PAIR_VALUE = LEVEL_VALUE ** 3
    PAIR_VALUE = LEVEL_VALUE ** 2
    HIGH_CARD_VALUE = LEVEL_VALUE ** 1

    def __init__(self):
        """
        Initialises the Hand class
        """
        self.hand = [Card]
        self.hand.pop()
        self.hand_value = 0
        # Seven card objects

    def append(self, new_card):
        """
        Creating this class needs a replacement append method
        :param new_card:
        :return:
        """
        self.hand.append(new_card)
        return

    def clear(self):
        """
        clear() of List for Hand
        :return:
        """
        self.hand.clear()
        return

    def hand_to_str(self):
        """
        Returns a list of the cards in the hand
        :return: String of list of cards in the hand
        """
        return '[%s]' % ', '.join(map(str, self.hand))

    def create_val_hist(self):
        card_val = []
        for x in range(len(self.hand)):
            card_val.append(self.hand[x].value)
        return card_val

    def check_royal_flush(self):
        clubs_list = []
        diamonds_list = []
        hearts_list = []
        spades_list = []
        val_hist = []
        for x in range(len(self.hand)):
            if self.hand[x].suit == Deck.CLUBS:
                clubs_list.append(self.hand[x].value)
            elif self.hand[x].suit == Deck.DIAMONDS:
                diamonds_list.append(self.hand[x].value)
            elif self.hand[x].suit == Deck.HEARTS:
                hearts_list.append(self.hand[x].value)
            else:
                spades_list.append(self.hand[x].value)
        if len(clubs_list) > 4:
            for y in range(len(clubs_list)):
                val_hist.append(clubs_list[y])
            set(val_hist)
            val_hist.sort()
        elif len(diamonds_list) > 4:
            for y in range(len(diamonds_list)):
                val_hist.append(diamonds_list[y])
            set(val_hist)
            val_hist.sort()
        elif len(hearts_list) > 4:
            for y in range(len(hearts_list)):
                val_hist.append(hearts_list[y])
            set(val_hist)
            val_hist.sort()
        elif len(spades_list) > 4:
            for y in range(len(spades_list)):
                val_hist.append(spades_list[y])
            set(val_hist)
            val_hist.sort()
        else:
            return None
        for z in range(len(val_hist) - 4):
            if val_hist[z] + 1 == val_hist[z + 1] and val_hist[z] + 2 == val_hist[z + 2]:
                if val_hist[z] + 3 == val_hist[z + 3] and val_hist[z] + 4 == val_hist[z + 4]:
                    if val_hist[z] == 10:
                        return self.ROYAL_FLUSH_VALUE
        return None

    def check_straight_flush(self):
        clubs_list = []
        diamonds_list = []
        hearts_list = []
        spades_list = []
        val_hist = []
        for x in range(len(self.hand)):
            if self.hand[x].suit == Deck.CLUBS:
                clubs_list.append(self.hand[x].value)
            elif self.hand[x].suit == Deck.DIAMONDS:
                diamonds_list.append(self.hand[x].value)
            elif self.hand[x].suit == Deck.HEARTS:
                hearts_list.append(self.hand[x].value)
            else:
                spades_list.append(self.hand[x].value)
        if len(clubs_list) > 4:
            for y in range(len(clubs_list)):
                val_hist.append(clubs_list[y])
            set(val_hist)
            val_hist.sort()
        elif len(diamonds_list) > 4:
            for y in range(len(diamonds_list)):
                val_hist.append(diamonds_list[y])
            set(val_hist)
            val_hist.sort()
        elif len(hearts_list) > 4:
            for y in range(len(hearts_list)):
                val_hist.append(hearts_list[y])
            set(val_hist)
            val_hist.sort()
        elif len(spades_list) > 4:
            for y in range(len(spades_list)):
                val_hist.append(spades_list[y])
            set(val_hist)
            val_hist.sort()
        else:
            return None
        for z in range(len(val_hist) - 4):
            if val_hist[z] + 1 == val_hist[z + 1] and val_hist[z] + 2 == val_hist[z + 2]:
                if val_hist[z] + 3 == val_hist[z + 3] and val_hist[z] + 4 == val_hist[z + 4]:
                    return self.STRAIGHT_FLUSH_VALUE * val_hist[0]
        return None

    def check_four_of_a_kind(self):
        val_hist = self.create_val_hist()
        val_hist.sort(reverse=True)
        for y in range(len(self.hand) - 3):
            if val_hist[y] == val_hist[y + 1] and val_hist[y] == val_hist[y + 2] and val_hist[y] == val_hist[y + 3]:
                for x in range(5 - len(val_hist)):
                    val_hist.append(0)
                if y == 0:
                    return self.FOUR_OF_A_KIND_VALUE * (val_hist[y] + val_hist[4] / self.LEVEL_VALUE)
                elif y == 1:
                    return self.FOUR_OF_A_KIND_VALUE * (val_hist[y] + val_hist[0] / self.LEVEL_VALUE)
        return None

    def check_full_house(self):
        val_hist = self.create_val_hist()
        val_hist.sort(reverse=True)
        for y in range(len(self.hand) - 2):
            if val_hist[y] == val_hist[y + 1] and val_hist[y] == val_hist[y + 2]:
                for z in range(len(self.hand) - 1):
                    if val_hist[z] == val_hist[z + 1] and val_hist[z] != val_hist[y]:
                        return self.FULL_HOUSE_VALUE * (val_hist[y] + val_hist[z] / self.LEVEL_VALUE)
        return None

    def check_flush(self):
        clubs_list = []
        diamonds_list = []
        hearts_list = []
        spades_list = []
        val_hist = []
        for x in range(len(self.hand)):
            if self.hand[x].suit == Deck.CLUBS:
                clubs_list.append(self.hand[x].value)
            elif self.hand[x].suit == Deck.DIAMONDS:
                diamonds_list.append(self.hand[x].value)
            elif self.hand[x].suit == Deck.HEARTS:
                hearts_list.append(self.hand[x].value)
            else:
                spades_list.append(self.hand[x].value)
        if len(clubs_list) > 4:
            for y in range(len(clubs_list)):
                val_hist.append(clubs_list[y])
            val_hist.sort(reverse=True)
        elif len(diamonds_list) > 4:
            for y in range(len(diamonds_list)):
                val_hist.append(diamonds_list[y])
            val_hist.sort(reverse=True)
        elif len(hearts_list) > 4:
            for y in range(len(hearts_list)):
                val_hist.append(hearts_list[y])
            val_hist.sort(reverse=True)
        elif len(spades_list) > 4:
            for y in range(len(spades_list)):
                val_hist.append(spades_list[y])
            val_hist.sort(reverse=True)
        else:
            return None
        return self.FLUSH_VALUE * (val_hist[0] + val_hist[1] / self.LEVEL_VALUE + val_hist[2] / self.LEVEL_VALUE ** 2
                                   + val_hist[3] / self.LEVEL_VALUE ** 3 + val_hist[4] / self.LEVEL_VALUE ** 4)

    def check_straight(self):
        val_hist = self.create_val_hist()
        set(val_hist)
        val_hist.sort()
        if len(val_hist) > 4:
            for z in range(len(val_hist) - 4):
                if val_hist[z] + 1 == val_hist[z + 1] and val_hist[z] + 2 == val_hist[z + 2]:
                    if val_hist[z] + 3 == val_hist[z + 3] and val_hist[z] + 4 == val_hist[z + 4]:
                        return self.STRAIGHT_VALUE * val_hist[0]
        return None

    def check_three_of_a_kind(self):
        val_hist = self.create_val_hist()
        val_hist.sort(reverse=True)
        for y in range(len(self.hand) - 2):
            if val_hist[y] == val_hist[y + 1] and val_hist[y] == val_hist[y + 2]:
                for x in range(5 - len(val_hist)):
                    val_hist.append(0)
                if y == 0:
                    return self.THREE_OF_A_KIND_VALUE * (val_hist[y] + val_hist[3]
                                                         / self.LEVEL_VALUE + val_hist[4] / self.LEVEL_VALUE ** 2)
                elif y == 1:
                    return self.THREE_OF_A_KIND_VALUE * (val_hist[y] + val_hist[0]
                                                         / self.LEVEL_VALUE + val_hist[4] / self.LEVEL_VALUE ** 2)
                else:
                    return self.THREE_OF_A_KIND_VALUE * (val_hist[y] + val_hist[0]
                                                         / self.LEVEL_VALUE + val_hist[1] / self.LEVEL_VALUE ** 2)
        return None

    def check_two_pair(self):
        val_hist = self.create_val_hist()
        val_hist.sort(reverse=True)
        for y in range(len(self.hand) - 3):
            if val_hist[y] == val_hist[y + 1]:
                z = len(self.hand) - 1
                while z > y + 1:
                    if val_hist[z] == val_hist[z - 1]:
                        for x in range(5 - len(val_hist)):
                            val_hist.append(0)
                        if y == 0:
                            if z == 3:
                                return self.TWO_PAIR_VALUE * (val_hist[y] + val_hist[z]
                                                              / self.LEVEL_VALUE + val_hist[4] / self.LEVEL_VALUE ** 2)
                            else:
                                return self.TWO_PAIR_VALUE * (val_hist[y] + val_hist[z]
                                                              / self.LEVEL_VALUE + val_hist[2] / self.LEVEL_VALUE ** 2)
                        else:
                            return self.TWO_PAIR_VALUE * (val_hist[y] + val_hist[z]
                                                          / self.LEVEL_VALUE + val_hist[0] / self.LEVEL_VALUE ** 2)
                    else:
                        z -= 1
        return None

    def check_pair(self):
        val_hist = self.create_val_hist()
        val_hist.sort(reverse=True)
        for y in range(len(self.hand) - 1):
            if val_hist[y] == val_hist[y + 1]:
                for x in range(5 - len(val_hist)):
                    val_hist.append(0)
                if y == 0:
                    return self.PAIR_VALUE * (val_hist[y] + val_hist[2] / self.LEVEL_VALUE + val_hist[3]
                                              / self.LEVEL_VALUE ** 2 + val_hist[4] / self.LEVEL_VALUE ** 3)
                elif y == 1:
                    return self.PAIR_VALUE * (val_hist[y] + val_hist[0] / self.LEVEL_VALUE + val_hist[3]
                                              / self.LEVEL_VALUE ** 2 + val_hist[4] / self.LEVEL_VALUE ** 3)
                elif y == 2:
                    return self.PAIR_VALUE * (val_hist[y] + val_hist[0] / self.LEVEL_VALUE + val_hist[1]
                                              / self.LEVEL_VALUE ** 2 + val_hist[4] / self.LEVEL_VALUE ** 3)
                else:
                    return self.PAIR_VALUE * (val_hist[y] + val_hist[0] / self.LEVEL_VALUE + val_hist[1]
                                              / self.LEVEL_VALUE ** 2 + val_hist[2] / self.LEVEL_VALUE ** 3)
        return None

    def high_card(self):
        val_hist = self.create_val_hist()
        val_hist.sort()
        for x in range(5 - len(val_hist)):
            val_hist.append(0)
        return self.HIGH_CARD_VALUE * (val_hist[0]
                                       + val_hist[1] / self.LEVEL_VALUE
                                       + val_hist[2] / self.LEVEL_VALUE ** 2
                                       + val_hist[3] / self.LEVEL_VALUE ** 3
                                       + val_hist[4] / self.LEVEL_VALUE ** 4)

    def find_hand_value(self):
        hand_size = len(self.hand)
        if hand_size >= 5:
            self.hand_value = self.check_royal_flush()
            if self.hand_value is not None:
                return self.hand_value
            self.hand_value = self.check_straight_flush()
            if self.hand_value is not None:
                return self.hand_value
        if hand_size >= 4:
            self.hand_value = self.check_four_of_a_kind()
            if self.hand_value is not None:
                return self.hand_value
        if hand_size >= 5:
            self.hand_value = self.check_full_house()
            if self.hand_value is not None:
                return self.hand_value
            self.hand_value = self.check_flush()
            if self.hand_value is not None:
                return self.hand_value
            self.hand_value = self.check_straight()
            if self.hand_value is not None:
                return self.hand_value
        if hand_size >= 3:
            self.hand_value = self.check_three_of_a_kind()
            if self.hand_value is not None:
                return self.hand_value
        if hand_size >= 4:
            self.hand_value = self.check_two_pair()
            if self.hand_value is not None:
                return self.hand_value
        self.hand_value = self.check_pair()
        if self.hand_value is not None:
            return self.hand_value
        else:
            self.hand_value = self.high_card()
        return self.hand_value

    # TODO
    # Need to resolve for ACES

    # TODO
    def opening_hand_ranking(self):
        """
        Takes an opening hand and analyses it to give a ranking
        :return:
        """
        # From https://www.tightpoker.com/poker_hands.html
        dicto = {
            (14, 14): 2.32,
            (13, 13): 1.67,
            (12, 12): 1.22,
            (11, 11): 0.86,
            (10, 10): 0.58,
            (14, 13): 0.51,
            (9, 9): 0.38,
            (14, 12): 0.31,
            (8, 8): 0.25,
            (14, 11): 0.19,
            (13, 12): 0.16,
            (7, 7): 0.16,
            (14, 10): 0.08,
            (13, 11): 0.08,
            (6, 6): 0.07,
            (12, 11): 0.03,
            (5, 5): 0.02,
            (13, 10): 0.01,
            (12, 10): -0.02,
            (4, 4): -0.03,
            (14, 9): -0.03,
            (11, 10): -0.03,
            (13, 9): -0.07,
            (10, 9): -0.07,
            (14, 8): -0.07,
            (3, 3): -0.07,
            (12, 9): -0.08,
            (2, 2): -0.09,
            (11, 9): -0.09,
            (11, 8): -0.10,
            (9, 8): -0.10,
            (10, 8): -0.10,
            (9, 7): -0.10,
            (14, 7): -0.10,
            (10, 7): -0.10,
            (12, 8): -0.11,
            (10, 6): -0.11,
            (7, 5): -0.11,
            (13, 8): -0.11,
            (8, 6): -0.11,
            (13, 7): -0.11,
            (8, 5): -0.11,
            (7, 6): -0.11,
            (14, 6): -0.12,
            (10, 2): -0.12,
            (8, 4): -0.12,
            (6, 2): -0.12,
            (9, 5): -0.12,
            (14, 5): -0.12,
            (12, 7): -0.12,
            (10, 5): -0.12,
            (8, 7): -0.12,
            (8, 3): -0.12,
            (6, 5): -0.12,
            (9, 4): -0.12,
            (7, 4): -0.12,
            (5, 4): -0.12,
            (14, 4): -0.12,
            (10, 4): -0.12,
            (8, 2): -0.12,
            (6, 4): -0.12,
            (4, 2): -0.12,
            (11, 7): -0.12,
            (9, 3): -0.12,
            (7, 3): -0.12,
            (5, 3): -0.12,
            (10, 3): -0.12,
            (6, 3): -0.12,
            (13, 6): -0.12,
            (11, 6): -0.12,
            (9, 6): -0.12,
            (9, 2): -0.12,
            (7, 2): -0.12,
            (5, 2): -0.12,
            (12, 4): -0.13,
            (13, 5): -0.13,
            (11, 5): -0.13,
            (12, 3): -0.13,
            (4, 3): -0.13,
            (13, 4): -0.13,
            (11, 4): -0.13,
            (12, 6): -0.13,
            (12, 2): -0.13,
            (11, 3): -0.13,
            (14, 3): -0.13,
            (12, 5): -0.13,
            (11, 2): -0.13,
            (13, 3): -0.14,
            (13, 2): -0.14,
            (3, 2): -0.14,
            (14, 2): -0.15
        }

        s_dicto = {
            (14, 13): 0.78,
            (14, 12): 0.59,
            (14, 11): 0.44,
            (13, 12): 0.39,
            (14, 10): 0.32,
            (13, 11): 0.29,
            (12, 11): 0.23,
            (13, 10): 0.20,
            (14, 9): 0.19,
            (12, 10): 0.17,
            (11, 10): 0.15,
            (14, 8): 0.10,
            (13, 9): 0.09,
            (14, 5): 0.08,
            (14, 7): 0.08,
            (10, 9): 0.05,
            (14, 4): 0.05,
            (12, 9): 0.05,
            (11, 9): 0.04,
            (14, 6): 0.03,
            (14, 3): 0.02,
            (13, 8): 0.01,
            (9, 8): 0.00,
            (10, 8): 0.00,
            (13, 7): 0.00,
            (14, 2): 0.00,
            (8, 7): -0.02,
            (12, 8): -0.02,
            (11, 8): -0.03,
            (7, 6): -0.03,
            (9, 7): -0.04,
            (13, 6): -0.04,
            (13, 5): -0.05,
            (13, 4): -0.05,
            (10, 7): -0.05,
            (12, 7): -0.06,
            (6, 5): -0.07,
            (8, 6): -0.07,
            (11, 7): -0.07,
            (5, 4): -0.08,
            (12, 6): -0.08,
            (13, 3): -0.08,
            (7, 5): -0.09,
            (6, 4): -0.09,
            (12, 5): -0.09,
            (13, 2): -0.09,
            (9, 6): -0.09,
            (12, 3): -0.10,
            (12, 4): -0.10,
            (11, 5): -0.11,
            (11, 4): -0.11,
            (7, 4): -0.11,
            (5, 3): -0.11,
            (6, 3): -0.11,
            (11, 6): -0.11,
            (10, 6): -0.11,
            (9, 5): -0.12,
            (10, 5): -0.12,
            (12, 2): -0.12,
            (8, 5): -0.12,
            (4, 3): -0.13,
            (10, 4): -0.13,
            (11, 3): -0.13,
            (10, 3): -0.13,
            (8, 4): -0.13,
            (8, 2): -0.14,
            (4, 2): -0.14,
            (9, 3): -0.14,
            (7, 3): -0.14,
            (11, 2): -0.14,
            (9, 2): -0.14,
            (5, 2): -0.14,
            (10, 2): -0.14,
            (6, 2): -0.14,
            (8, 3): -0.15,
            (9, 4): -0.15,
            (7, 2): -0.15,
            (3, 2): -0.15
        }

        val_list = []
        suit_list = []
        for x in range(2):
            val_list.append(self.hand[x].value)
            suit_list.append(self.hand[x].suit)
        val_list.sort(reverse=True)
        if suit_list[0] == suit_list[1]:
            # Suited
            rank = s_dicto[val_list[0], val_list[1]]
        else:
            # Unsuited
            rank = dicto[val_list[0], val_list[1]]
        return rank



