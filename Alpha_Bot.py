from Player import *
import time
import random


class Nit_Bot(Player):
    # Nit:
    # Pre-flop selection
    # Post-flop aggression
    # Raise half pot?

    def __init__(self, order, timer):
        """
        Generates a bot object
        - Can know when to bet/fold. Depending on:
            -
        - How much to bet. Depending on:
            -
        """
        super().__init__(order)
        self.name = 'Bot' + str(order + 1)
        self.is_checked = False
        self.timer = timer
        # vpip, pfr and agg stored as integer% (/ 100)
        # TODO
        # Dictionary?
        # Translate to playable hand ratings
        self.vpip = 18
        # Translate to preflop 3-bet hand ratings
        self.pfr = 14
        self.agg = 00
        self.total_hand = Hand()

    def find_total_hand_value(self, community_cards):
        # Value of community cards
        community_card_list = Hand()
        for card in community_cards:
            community_card_list.append(card)
        community_value = community_card_list.find_hand_value()
        # Value of community cards + opening_cards
        for card_cc in community_cards:
            self.total_hand.append(card_cc)
        for x in range(2):
            self.total_hand.append(self.hand.hand[x])
        total_value = self.total_hand.find_hand_value()
        return total_value - community_value

    def bet_fold_algorithm(self, current_top_bid,
                           pot_size, community_cards, position, number_of_players, is_first_cycle, total_value):
        """
        Decides whether to bet or fold at this point in time
        :param current_top_bid:
        :param pot_size:
        :param community_cards:
        :param position:
        :param number_of_players:
        :param is_first_cycle:
        :return:
        """
        # If pre-flop
        if len(community_cards) == 0:
            rank = self.hand.opening_hand_ranking()
            # Cut-off rank = 0.00 right now
            # Else bet for now
            cutoff = self.stat_to_ev(self.vpip)
            if rank <= cutoff:
                # Fold
                return 'f'
            else:
                return 'b'
        # If post-flop
        else:
            # Greater than 10 high card
            if total_value > self.agg_to_total_value_cutoff():
                return 'b'
            elif position == number_of_players - 1 and current_top_bid < pot_size / 5:
                return 'b'
            elif current_top_bid == 0:
                return 'c'
            else:
                return 'f'

    def amount_algorithm(self, current_top_bid, pot_size,
                         community_cards, position, number_of_players, is_first_cycle, total_value):

        """
        Decides amount to bet
        :param current_top_bid:
        :param pot_size:
        :param community_cards:
        :param position:
        :param number_of_players:
        :param is_first_cycle:
        :return:
        """
        # If pre-flop
        if len(community_cards) == 0:
            if is_first_cycle is False:
                return current_top_bid - self.current_bet
            rank = self.hand.opening_hand_ranking()
            # 168 hands
            # Nits Voluntary Put in Pot (VPIP) = 18%
            # Pre-flop Raise (PFR) = 14%
            # So 168 * 0.14 = 23 top hands
            # Triple bet: > 0.15
            # 168 * 0.18 = 28 top hands
            # Min raise: > 0.05
            # Change as slider
            # TODO
            rand_rank = 0  # Change to random 0-0.15?
            cutoff = self.stat_to_ev(self.pfr)
            if rank > cutoff - rand_rank:
                # Triple bet
                return current_top_bid * 3 - self.current_bet
            else:
                # Min raise
                return current_top_bid * 2 - self.current_bet
        # Otherwise always call for now
        # Raises half the pot then calls 60%
        # Or check-raise-call? 40%
        # If post-flop
        else:
            if is_first_cycle is True:
                # TODO
                # rand check or raise
                rando = random.randint(1, 10)
                # if check
                if rando > 7 and current_top_bid == 0:
                    self.is_checked = True
                    return 0
                # if raise
                else:
                    return int(pot_size / 2)
            else:
                if self.is_checked is True:
                    self.is_checked = False
                    return int(pot_size / 2)
                else:
                    return current_top_bid - self.current_bet

    def decide(self, current_top_bid, pot_size, community_cards, position, number_of_players, is_first_cycle):
        self.print_info(community_cards, current_top_bid, pot_size)
        # Implementing bet and fold for now
        # Implementing check now
        if (current_top_bid == 0 or current_top_bid == self.current_bet) and self.current_bet != self.SMALL_BLIND:
            print('Bet: b, Check: c, Fold: f')
        else:
            print('Bet: b, Fold: f')
        total_value = self.find_total_hand_value(community_cards)
        decision = self.bet_fold_algorithm\
            (current_top_bid, pot_size, community_cards, position, number_of_players, is_first_cycle, total_value)
        if decision == 'b':
            bet = self.amount_algorithm\
                (current_top_bid, pot_size, community_cards, position, number_of_players, is_first_cycle, total_value)
            if bet >= self.stack:
                bet = self.stack
            self.current_bet = bet + self.current_bet
            self.stack -= bet
            if self.stack == 0:
                print('All in for $' + str(bet))
                print('')
            elif bet == 0:
                print('Check')
                print('')
            else:
                print('Bet: $' + str(bet))
                print('')

        elif decision == 'f':
            print('Fold')
            print('')
            bet = 0
            self.is_folded = True
        else:
            print('Check')
            print('')
            # decision == 'c':
            self.check()
            bet = 0
        time.sleep(self.timer)
        return bet

    @staticmethod
    def stat_to_ev(stat):
        hands_to_play = int(stat / 100 * 169)
        if hands_to_play == 0:
            hands_to_play += 1
        hands_to_ev = {1: 2.32,
                       2: 1.67,
                       3: 1.22,
                       4: 0.86,
                       5: 0.78,
                       6: 0.59,
                       7: 0.58,
                       8: 0.51,
                       9: 0.44,
                       10: 0.39,
                       11: 0.38,
                       12: 0.32,
                       13: 0.31,
                       14: 0.29,
                       15: 0.25,
                       16: 0.23,
                       17: 0.20,
                       18: 0.19,
                       19: 0.19,
                       20: 0.17,
                       21: 0.16,
                       22: 0.16,
                       23: 0.15,
                       24: 0.10,
                       25: 0.09,
                       26: 0.08,
                       27: 0.08,
                       28: 0.08,
                       29: 0.08,
                       30: 0.07,
                       31: 0.05,
                       32: 0.05,
                       33: 0.05,
                       34: 0.04,
                       35: 0.03,
                       36: 0.03,
                       37: 0.02,
                       38: 0.02,
                       39: 0.01,
                       40: 0.01
                       }
        for i in range(41, 45):
            hands_to_ev[i] = 0.00
        for i in range(45, 48):
            hands_to_ev[i] = -0.02
        for i in range(48, 53):
            hands_to_ev[i] = -0.03
        for i in range(53, 55):
            hands_to_ev[i] = -0.04
        for i in range(55, 58):
            hands_to_ev[i] = -0.05
        for i in range(58, 59):
            hands_to_ev[i] = -0.06
        for i in range(59, 66):
            hands_to_ev[i] = -0.07
        for i in range(66, 70):
            hands_to_ev[i] = -0.08
        for i in range(70, 77):
            hands_to_ev[i] = -0.09
        for i in range(77, 85):
            hands_to_ev[i] = -0.10
        for i in range(85, 100):
            hands_to_ev[i] = -0.11
        for i in range(100, 137):
            hands_to_ev[i] = -0.12
        for i in range(137, 155):
            hands_to_ev[i] = -0.13
        for i in range(155, 165):
            hands_to_ev[i] = -0.14
        for i in range(165, 170):
            hands_to_ev[i] = -0.15

        return hands_to_ev[hands_to_play]

    # https: // en.wikipedia.org / wiki / Poker_probability

    def agg_to_total_value_cutoff(self):
        # Pair
        if self.agg >= 82.6:
            return Hand.PAIR_VALUE - Hand.HIGH_CARD_VALUE
        elif self.agg >= 38.8:
            return Hand.TWO_PAIR_VALUE - Hand.PAIR_VALUE
        elif self.agg >= 15.3:
            return Hand.THREE_OF_A_KIND_VALUE - Hand.TWO_PAIR_VALUE
        elif self.agg >= 10.4:
            return Hand.STRAIGHT_VALUE - Hand.THREE_OF_A_KIND_VALUE
        elif self.agg >= 5.82:
            return Hand.FLUSH_VALUE - Hand.STRAIGHT_VALUE
        elif self.agg >= 2.80:
            return Hand.FULL_HOUSE_VALUE - Hand.FLUSH_VALUE
        elif self.agg >= 0.199:
            return Hand.FOUR_OF_A_KIND_VALUE - Hand.FULL_HOUSE_VALUE
        elif self.agg >= 0.0311:
            return Hand.STRAIGHT_FLUSH_VALUE - Hand.FOUR_OF_A_KIND_VALUE
        elif self.agg >= 0.0032:
            return Hand.ROYAL_FLUSH_VALUE - Hand.STRAIGHT_FLUSH_VALUE
        else:
            return Hand.ROYAL_FLUSH_VALUE

        return


    # TODO
    # Implement more random factors
