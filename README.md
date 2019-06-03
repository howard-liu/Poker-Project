# Poker-Project
After doing my AI project I was very interested in the power of Python and combined it with my hobby of poker.

## How to play
Run `python3 Game.py` in the terminal, and it will prompt you to insert the number of players and then bots you want on the table. Small Blind of $1 and Big Blind of $2 is fixed for the game, and each individual on the table starts with $200. Use 'b' and 'f' to choose whether to bet of fold. If you bet, you can choose how much you want to bet or to call. The turns goes around the table as real poker rules as cards are revealed. If showdown happens, highest value hand will win the pot. Then dealer changes position.

## The game
I have programmed in all the rules of poker with variable amount of human and AI players in a table. This includes automatically dealing cards and going around accepting bets. It can also correctly identify poker hands at the end of the round during showdown and give the pot to the winner. The game is played on the terminal where all the cards are visible. If need be, this could be adapted to run as a back end of a poker game with a proper UI.

## The AI
I have used metrics that depict a player's aggressiveness (often used by analysis of online poker players) to simulate the "range" of hands that the AI would bet, with a slight random element, just to be unpredictable. In no way is this AI a strong poker player, but I believe it can beat some beginner players.

## Conclusion
This was a fun project that combined my love for Python, poker and AI. Feel free to clone and have a try. P.S. there are a lot of edge cases rules in poker, so I may have missed some when going through and programming it. Sorry :).

Happy Playing!
