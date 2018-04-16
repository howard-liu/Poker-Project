from Hand import *

# -------------
# TEST COMPLETE
# -------------
#
cc_hand = []
cccard1 = Card()
cccard2 = Card()
cccard3 = Card()

cccard1.value = 7
cccard2.value = 4
cccard3.value = 6

cccard1.suit = Deck.CLUBS
cccard2.suit = Deck.CLUBS
cccard3.suit = Deck.CLUBS

cc_hand.append(cccard1)
cc_hand.append(cccard2)
cc_hand.append(cccard3)


hand = Hand()
card1 = Card()
card2 = Card()

card1.value = 9
card2.value = 7

card1.suit = Deck.HEARTS
card2.suit = Deck.HEARTS

hand.append(card1)
hand.append(card2)
#
# value = hand.find_hand_value()
# if value == 0:
#     print('through folds')
# else:
#     if value >= Hand.ROYAL_FLUSH_VALUE:
#         print('with a Royal Flush')
#     elif value >= Hand.STRAIGHT_FLUSH_VALUE:
#         print('with a Straight Flush')
#     elif value >= Hand.FOUR_OF_A_KIND_VALUE:
#         print('with a Four of a Kind')
#     elif value >= Hand.FULL_HOUSE_VALUE:
#         print('with a Full House')
#     elif value >= Hand.FLUSH_VALUE:
#         print('with a Flush')
#     elif value >= Hand.STRAIGHT_VALUE:
#         print('with a Straight')
#     elif value >= Hand.THREE_OF_A_KIND_VALUE:
#         print('with a Three of a Kind')
#     elif value >= Hand.TWO_PAIR_VALUE:
#         print('with a Two Pair')
#     elif value >= Hand.PAIR_VALUE:
#         print('with a Pair')
#     else:
#         print('with a High Card')
#

from Alpha_Bot import *

alpha = Nit_Bot(0, 0)

alpha.hand = hand
print(alpha.bet_fold_algorithm(2, 0, [], 0, 2, True, alpha.find_total_hand_value(cc_hand)))
print(Hand.PAIR_VALUE)
print(Hand.HIGH_CARD_VALUE*13)

