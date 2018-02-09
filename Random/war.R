# war.R
# simulation of the card game of War

# goals: 1) look for patterns in deck size over time
#        2) find the threshold number of cards that leads to defeat 90% of the time

# TODO: Define the set that represents a pack of cards
# 4 repetitions of [1:13]
# These are NOT the numbers on the cards, but represent the cards' rank. 13 = Ace.

# Game routine 
# (can you repeat the whole script to do monte carlo 
# or do you have to write that into a loop in the script?)

# TODO: Generate the 2 players' decks, deckA and deckB
# do this by shuffling or picking without replacement from the card set

# TODO: Recursive turn routine

# warcount = 0

function(turn(warcount)) {
  # this will return the number of cards in deck A at the end of the turn
  # taking warcount as an argument
  
  # cardplayed = 4*warcount + 1
  # if deckA[cardplayed] == deckB[cardplayed] # war
    # warcount <- warcount + 1
    # turn(warcount)
  # if deckA[cardplayed] > deckB[cardplayed] # A wins the turn
    # append deckB cards to the end of deckA
    # the cards appended are [1:4*warcount+2]
  # if deckB[cardplayed] > deckA[cardplayed] # B wins the turn
    # append deckA cards to the end of deckB
    # the cards appended are [1:4*warcount+2]
  # check for loss -- 
  # is the size of the smaller deck  less than 
  # the amount of cards that will be lost? 
  # if (min(len(deckA), len(deckB)) < (4*warcount+2)
    # whoever lost that turn has lost the game.
  # else 
    # take off [1:4*warcount+1] cards from the losing deck (shift function?)
    # shift each deck by 4*warcount+1 (the cards they each played)
}