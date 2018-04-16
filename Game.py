from Table import *


def check_valid_player_count(actor):
    """
    Asks until give a valid player count
    :param:
    :return:
    """
    print('Insert number of ' + actor + ': ')
    while True:
        try:
            count = int(input())
        except ValueError:
            print('Please enter an integer')
            continue
        else:
            break
    return count


def round_start():
    time.sleep(Table.TIMER)
    table.blinds()
    time.sleep(Table.TIMER)
    table.initialise_deck()
    table.deal_cards()
    print('')
    print('Preflop betting:')
    print('')
    table.pre_flop()
    winner = table.betting_round(0)
    if winner is None:
        winner = table.the_flop()
        if winner is None:
            winner = table.the_turn()
            if winner is None:
                winner = table.the_river()
                if winner is None:
                    table.showdown()
            else:
                table.declare_winner(winner, 0)
        else:
            table.declare_winner(winner, 0)
    else:
        table.declare_winner(winner, 0)
    if table.check_valid_continue() == 'y':
        round_start()
    else:
        print('Thank you for playing')
    return


print('Hi! Welcome to Howard\'s Poker game!')
print('Please insert number of players and bots. Total needs to be 3 or more right now.')

while True:
    nop = check_valid_player_count('players')
    nob = check_valid_player_count('bots')
    if nop + nob < 3:
        print('Sorry table needs to have 3 or more actors')
        continue
    else:
        break
table = Table(nop, nob)
# Round start
round_start()

# TODO
# Uhh can also showdown when ppl are all in
