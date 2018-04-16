from random import shuffle
import time
from Alpha_Bot import *


class Table(object):

    TIMER = 0

    def __init__(self, number_of_humans, number_of_bots):
        """
        Initialises a table with given number of players
        :param number_of_players:
        """
        # This line vvvvvvvv
        number_of_players = number_of_humans + number_of_bots
        player = []
        for x in range(number_of_humans):
            player.append(Player(x))
        for y in range(number_of_bots):
            player.append(Nit_Bot(y + number_of_humans, self.TIMER))
        # Replace this line only vvvvvvvv
        # player = [Player(x) for x in range(int(number_of_players))]
        self.player = player
        self.number_of_players = int(number_of_players)
        self.deck = []
        self.community_cards = []
        self.pot = 0
        self.round = 0

    def blinds(self):
        """
        Start a hand of poker by paying the blinds
        :return:
        """
        for y in range(self.number_of_players):
            x = y + self.round
            x = self.circulation(x)
            sb = 1 + self.round
            sb = self.circulation(sb)
            bb = 2 + self.round
            bb = self.circulation(bb)
            if x == sb:
                self.player[x].pay_small_blind()
            elif x == bb:
                self.player[x].pay_big_blind()
        self.pot = self.player[0].SMALL_BLIND + self.player[0].BIG_BLIND
        return



        #
        # count = 0
        # # Button is always at position = 0
        # for y in range(self.number_of_players):
        #     y = [y + 0]
        #     x = [0, 0]
        #     for z in range(1):
        #         x[z] = y[z] + self.round
        #         x[z] = self.circulation(x[z])
        #         if x[z] < self.number_of_players - 3:
        #             number = x[z] + 3
        #         else:
        #             number = x[z] - (self.number_of_players - 3)
        #         if number == 1:
        #             self.player[number].pay_small_blind()
        #         elif number == 2:
        #             self.player[number].pay_big_blind()
        #             self.pot = self.player[0].SMALL_BLIND + self.player[0].BIG_BLIND
        #             return
        # return

    def initialise_deck(self):
        """
        Starts a shuffled deck of cards
        :return:
        """
        deck = Deck()
        shuffle(deck.card)
        self.deck = deck
        return

    def deal_cards(self):
        """
        Deals 2 cards to all players
        :return:
        """
        y = 0
        while y < 2:
            for x in range(self.number_of_players):
                if x < self.number_of_players - 1:
                    self.player[x + 1].receive_card(self.deck.pop())
                else:
                    self.player[x - (self.number_of_players - 1)].receive_card(self.deck.pop())
            y += 1
        return

    def resolve_win_by_fold(self):
        """
        Checks if a player wins because everyone else folded
        :return:
        """
        count = 0
        for x in range(self.number_of_players):
            if self.player[x].is_folded:
                count += 1
                if count == self.number_of_players - 1:
                    for y in range(self.number_of_players):
                        if self.player[y].is_folded is False:
                            return self.player[y]
        return None

    def plus_one_circulation(self, x):
        if x >= self.number_of_players:
            x = x - self.number_of_players
            if x >= self.number_of_players:
                x = self.circulation(x)
        return x

    def circulation(self, x):
        if x >= self.number_of_players:
            x = x - self.number_of_players
            if x >= self.number_of_players:
                x = self.circulation(x)
        return x

    def betting_round(self, round_state):
        """
        Does a round of betting (initial in mind for now)
        :return: Winner if winner is found (through folds)
        """
        cycle = 0
        all_called = 0
        if round_state == 0:
            prev_top_bid = 2
        else:
            prev_top_bid = 0
        is_first_cycle = True
        # Can only raise 4 times
        while cycle < 4:
            # Preflop ordering
            if round_state == 0:
                round_indicator = 3
            # Other ordering
            else:
                round_indicator = 1
            for y in range(self.number_of_players):
                x = y + self.round
                x = self.circulation(x)
                if x < self.number_of_players - round_indicator:
                    number = x + round_indicator
                else:
                    number = x - (self.number_of_players - round_indicator)
                if self.player[number].is_busted is True:
                    pass
                # Past the first cycle, if it hits a player with bet = current max bet, betting round over, move on
                if is_first_cycle is False and self.player[number].current_bet == prev_top_bid:
                    return None
                # Pre-flop first is already 0 money, no betting allowed
                if self.player[number].stack == 0 and is_first_cycle is True and round_state == 0:
                    self.player[number].is_folded = True
                if self.player[number].is_folded is False:
                    bid = self.player[number].\
                        decide(prev_top_bid, self.pot, self.community_cards, x, self.number_of_players, is_first_cycle)
                    # If player raised (does not count if first move in betting round)
                    if self.player[number].current_bet > prev_top_bid:
                        self.pot = self.pot + bid
                        prev_top_bid = self.player[number].current_bet
                    # Else: just folded or checked or called
                    else:
                        self.pot = self.pot + bid
                else:

                    # Already folded
                    all_called += 1
                winner = self.resolve_win_by_fold()
                if winner is not None:
                    return winner
            is_first_cycle = False
            cycle += 1

    def reveal_card(self):
        """
        Draws a card that is added to the 5 potentially visible cards on the table
        :return:
        """
        self.community_cards.append(self.deck.pop())
        return

    def pre_flop(self):
        return

    def the_flop(self):
        """
        Simulates the flop
        :return:
        """
        print('The Flop')
        time.sleep(self.TIMER)
        self.reveal_card()
        print('[%s]' % ', '.join(map(str, self.community_cards)))
        time.sleep(self.TIMER)
        self.reveal_card()
        print('[%s]' % ', '.join(map(str, self.community_cards)))
        time.sleep(self.TIMER)
        self.reveal_card()
        print('[%s]' % ', '.join(map(str, self.community_cards)))
        time.sleep(self.TIMER)
        print('')
        for x in range(self.number_of_players):
            self.player[x].current_bet = 0
        return self.betting_round(1)

    def the_turn(self):
        """
        Simulates the turn
        :return:
        """
        print('The Turn')
        time.sleep(self.TIMER)
        self.reveal_card()
        print('[%s]' % ', '.join(map(str, self.community_cards)))
        time.sleep(self.TIMER)
        print('')
        for x in range(self.number_of_players):
            self.player[x].current_bet = 0
        return self.betting_round(2)

    def the_river(self):
        """
        Simulates the turn
        :return:
        """
        print('The River')
        time.sleep(self.TIMER)
        self.reveal_card()
        print('[%s]' % ', '.join(map(str, self.community_cards)))
        time.sleep(self.TIMER)
        print('')
        for x in range(self.number_of_players):
            self.player[x].current_bet = 0
        return self.betting_round(3)

    def showdown(self):
        """
        Simulates a showdown (currently just for end of the round)
        :return:
        """
        value = [0] * self.number_of_players
        for x in range(self.number_of_players):
            if self.player[x].is_folded:
                value[x] = 0
            else:
                value[x] = self.player[x].showdown_value(self.community_cards)
            # print(str(value[x]))
        self.declare_winner(self.player[value.index(max(value))], max(value))
        return

    @staticmethod
    def check_valid_continue():
        """
        Makes sure that user enters the right character for continuing
        :return:
        """
        while True:
            decision = input()
            if decision.lower() == 'y':
                return 'y'
            elif decision.lower() == 'n':
                return 'n'
            else:
                print("Invalid input, please try again")
                print('Yes: y or No: n')
                continue

    def declare_winner(self, player, value):
        """
        Declares the winner!
        By what method
        Prepares next round
        Asks whether user wants to play next round
        :return:
        """
        print(player.name + ' wins the pot of $' + str(self.pot))
        self.player[player.starting_pos].stack = self.player[player.starting_pos].stack + self.pot

        if value == 0:
            print('through folds')
        else:
            if value >= Hand.ROYAL_FLUSH_VALUE:
                print('with a Royal Flush')
            elif value >= Hand.STRAIGHT_FLUSH_VALUE:
                print('with a Straight Flush')
            elif value >= Hand.FOUR_OF_A_KIND_VALUE:
                print('with a Four of a Kind')
            elif value >= Hand.FULL_HOUSE_VALUE:
                print('with a Full House')
            elif value >= Hand.FLUSH_VALUE:
                print('with a Flush')
            elif value >= Hand.STRAIGHT_VALUE:
                print('with a Straight')
            elif value >= Hand.THREE_OF_A_KIND_VALUE:
                print('with a Three of a Kind')
            elif value >= Hand.TWO_PAIR_VALUE:
                print('with a Two Pair')
            elif value >= Hand.PAIR_VALUE:
                print('with a Pair')
            else:
                print('with a High Card')

        print('---------------')
        for player_number in range(self.number_of_players):
            print(self.player[player_number].name + ' = $' + str(self.player[player_number].stack))
            if self.player[player_number].position == self.number_of_players - 1:
                self.player[player_number].position = 0
            else:
                self.player[player_number].position = self.player[player_number].position + 1
            self.player[player_number].hand.clear()
            self.player[player_number].current_bet = 0
            self.player[player_number].is_folded = False
            if self.player[player_number].stack == 0:
                self.player[player_number].is_busted = True
        self.pot = 0
        self.round += 1
        self.community_cards = []
        print('---------------')
        print('This has been Round ' + str(self.round))
        print('Continue?')
        print('y or n')
        return

    # TODO
    # Bigger picture:
    # Each round check if player is eliminated
