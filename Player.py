from Hand import *


class Player(object):

    SMALL_BLIND = 1
    BIG_BLIND = 2
    STARTING_STACK = 100 * BIG_BLIND

    def __init__(self, order):
        """
        Generates a player object
        """
        self.starting_pos = order
        self.name = 'Player' + str(order + 1)
        self.position = order
        self.stack = self.STARTING_STACK
        self.hand = Hand()
        self.current_bet = 0
        self.is_folded = False
        self.is_busted = False

    def pay_small_blind(self):
        print(self.name + ' pays small blind of $' + str(self.SMALL_BLIND))
        self.current_bet = self.SMALL_BLIND
        self.stack = self.stack - self.SMALL_BLIND
        return

    def pay_big_blind(self):
        print(self.name + ' pays big blind of $' + str(self.BIG_BLIND))
        self.current_bet = self.BIG_BLIND
        self.stack = self.stack - self.BIG_BLIND
        return

    def receive_card(self, card):
        self.hand.append(card)
        return

    def check_valid_bid(self, current_top_bid):
        """
        makes sure that bid is not above stack or below current bid
        :param current_top_bid:
        :return:
        """
        while True:
            amount = input()
            if current_top_bid == 0 and self.current_bet != self.SMALL_BLIND:
                # Cannot call
                if amount.isalpha():
                    print('Please enter an integer')
                    continue
                elif int(amount) > self.stack or int(amount) < current_top_bid - self.current_bet:
                    print('Please re-enter amount')
                    continue
                else:
                    break
            else:
                if amount.lower() == 'c':
                    amount = 'c'
                    break
                # Bet total should be a min of BB more than last highest bet
                elif 0 < int(amount) + self.current_bet - current_top_bid < self.BIG_BLIND:
                    print('Minimum raise is a Big Blind. Please enter another amount:')
                    continue
                elif amount.isalpha():
                    print('Please enter an integer, or Call: c')
                    continue
                elif int(amount) > self.stack or int(amount) < current_top_bid - self.current_bet:
                    print('Please re-enter amount')
                    continue
                else:
                    break

        return amount

    def check_valid_decision(self, current_top_bid):
        """
        Makes sure that user enters the right character
        :return:
        """
        while True:
            decision = input()
            if decision.lower() == 'b':
                val = 'b'
                break
            elif decision.lower() == 'f':
                val = 'f'
                break
            elif decision.lower() == 'c':
                if current_top_bid == 0 or self.current_bet == current_top_bid:
                    val = 'c'
                    break
                else:
                    print("Cannot check right now, please try again")
                    continue
            else:
                print("Invalid input, please try again")
                if current_top_bid == 0:
                    print('Bet: b, Check: c, Fold: f')
                else:
                    print('Bet: b, Fold: f')
                continue
        return val

    def bet(self, current_top_bid, pot_size, community_cards, position, number_of_players):
        if current_top_bid == 0:
            # cannot call
            # Except this: When checked/folded to in small blind
            if self.current_bet == self.SMALL_BLIND:
                print('How much? Needs to be integer between ' + str(self.SMALL_BLIND)
                      + ' and ' + str(self.stack) + ' incl. Or Call: c')
                amount = self.check_valid_bid(current_top_bid)
                if amount == 'c':
                    amount = str(self.SMALL_BLIND)
                    self.current_bet = self.SMALL_BLIND * 2
                else:
                    self.current_bet = int(amount) + self.current_bet
            else:
                print('How much? Needs to be integer between ' + str(max(current_top_bid, self.BIG_BLIND))
                      + ' and ' + str(self.stack))
                amount = self.check_valid_bid(current_top_bid)
                self.current_bet = int(amount)
            bet = int(amount)
        else:
            # First time betting
            if self.current_bet == 0:
                print('How much? Needs to be integer between ' + str(max(current_top_bid, self.BIG_BLIND))
                      + ' and ' + str(self.stack) + ' incl. Or Call: c')
                # amount needs to be below self.stack, above current_bid
                amount = self.check_valid_bid(current_top_bid)
                if amount == 'c':
                    amount = current_top_bid
                self.current_bet = int(amount)
                bet = int(amount)
            # Already have money in front
            else:
                if self.current_bet == self.SMALL_BLIND:
                    print('How much? Needs to be integer between ' + str(self.SMALL_BLIND)
                          + ' and ' + str(self.stack) + ' incl. Or Call: c')
                else:
                    print('How much? Needs to be integer between ' +
                          str(max(current_top_bid - self.current_bet, self.BIG_BLIND))
                          + ' and ' + str(self.stack) + ' incl. Or Call: c')
                # amount needs to be below self.stack, above current_bid
                amount = self.check_valid_bid(current_top_bid)
                if amount == 'c':
                    amount = current_top_bid - self.current_bet
                self.current_bet = int(amount) + self.current_bet
                bet = int(amount)
        print('prev stack: ' + str(self.stack))
        self.stack = self.stack - bet
        print('post stack: ' + str(self.stack))
        if self.stack == 0:
            print('All in for $' + str(bet))
            print('')
        else:
            print('Bet: $' + str(bet))
            print('')
        return bet

    def check(self):
        return

    def print_info(self, community_cards, current_top_bid, pot_size):
        print('Current player = ' + self.name)
        print('Current hand:' + self.hand.hand_to_str())
        print('Community cards: ' + '[%s]' % ', '.join(map(str, community_cards)))
        print('Current stack = $' + str(self.stack))
        print('Current top bid = $' + str(current_top_bid))
        print('Your current bid = $' + str(self.current_bet))
        print('Pot size = $' + str(pot_size))

    def decide(self, current_top_bid, pot_size, community_cards, position, number_of_players, is_first_cycle):
        self.print_info(community_cards, current_top_bid, pot_size)
        # Implementing bet and fold for now
        # Implementing check now
        if (current_top_bid == 0 or current_top_bid == self.current_bet) and self.current_bet != self.SMALL_BLIND:
            print('Bet: b, Check: c, Fold: f')
        else:
            print('Bet: b, Fold: f')
        decision = self.check_valid_decision(current_top_bid)
        if decision == 'b':
            bet = self.bet(current_top_bid, pot_size, community_cards, position, number_of_players)
        elif decision == 'f':
            print('Fold')
            print('')
            bet = 0
            self.is_folded = True
        else:
            # decision == 'c':
            self.check()
            bet = 0
        return bet

    def showdown_value(self, community_cards):
        """
        Generate an int value showing value of the hand
        :param community_cards:
        :return: int value of showdown value
        """
        for card in community_cards:
            self.hand.append(card)
        return self.hand.find_hand_value()

    # TODO
    # All ins, side pots and all that
    # Is all in check to stop them from being able to bet (DONE: If stack is zero, bet screen does not show up)
