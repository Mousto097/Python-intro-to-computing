# Description of game:
# http://www.classicgamesandpuzzles.com/Old-Maid.html

# In this implementaion the computer is always the dealer

# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     
     dealer=[]
     other=[]
     while len(deck)>1:
          other.append(deck.pop())
          dealer.append(deck.pop())
     other.append(deck.pop()) # deal the last remaing card
     return (dealer, other)

# alternative solution:
def del_cards_v2(deck):
    dealer=deck[1::2]
    other=deck[0::2]
    return (dealer, other)


# two soluitons are below:
# 1st is faster, does O(n log n) operations at most (where n=len(l))
# 2nd one is perhaps easier to understand but it can end up doing roughly n^2 operations
# (later I added a 3rd solution based on a question/appoach a student asked me about)
def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    l.sort()
    i=0
    while i<len(l)-1:
        card1=l[i]
        card2=l[i+1]
        if card1[:-1] == card2[:-1]: # compare the rank without suits (the suit is the last char)
            i=i+1           
        else:
            no_pairs.append(l[i])
        i=i+1
    if i==len(l)-1: #this is true if the last card is not a part of a pair
        no_pairs.append(l[i])

    random.shuffle(no_pairs)
    return no_pairs

def remove_pairs_v2(l):
    tmp=[]
    no_pairs=[]

    #create a list without suits
    for item in l:
        tmp.append(item[:-1]) # item[:-1] returns a card without suit i.e. last character

    #use it to determine which cards should stay
    for i in range(len(tmp)):
        if tmp.count(tmp[i]) % 2==1 and i==tmp.index(tmp[i]):
            no_pairs.append(l[i]) 

 
    random.shuffle(no_pairs)
    return no_pairs


# This solution based on a question a student asked me. This one can end up doing n^3 operations
def remove_pairs_v3(l):
    no_pairs=[] # in this solution this line is unnecessary

    no_pairs=l[:] # this copies elements of l into no_pairs
    i=0
    while i<len(no_pairs)-1:
        card1=no_pairs[i]
        print(card1)
        found_pair=False
        j=0
        while j<len(no_pairs) and found_pair==False:
            card2=no_pairs[j]
            if card1[:-1]==card2[:-1] and i!=j: # found two came cards
                print(no_pairs.count(card1))
                no_pairs.remove(card1)
                no_pairs.remove(card2)
                found_pair=True
            j=j+1
        i=i+1
        if found_pair:
            i=0 # have to start from the begininng since we changed the deck

    random.shuffle(no_pairs)
    return no_pairs
                     
                
                

        


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    print()
    for item in deck:
        print(item, end=' ')
    print("\n")

def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     print("I have", n, "cards. If 1 stands for my first card and")
     print(n, "for my last card, which of my cards would you like?")
     position=int(input("Give me an integer between 1 and "+str(n)+": ").strip())
     
     while not(position>=1 and position <=n):
          position=int(input("Invalid number. Please enter integer between 1 and "+str(n)+": ").strip())
     return position

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)
     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     round_parity=0 # Human's turn
     while len(dealer)>0 and len(human)>0:
          if round_parity==0: # dealer offers her cards
               print("***********************************************************")
               print("Your turn.")
               print("\nYour current deck of cards is:")
               print_deck(human)
               
               card_position=get_valid_input(len(dealer))
               item=dealer[card_position-1]
               dealer.remove(item) # this is valid since cards are unique

               # handled the four endings of ordinals in english
               english_ordinals_end=["st", "nd", "rd", "th"]
               if card_position>3:
                   ord_index=3
               else:
                   ord_index=card_position-1
                   
               print("You asked for my "+str(card_position)+english_ordinals_end[ord_index]+" card.")

               print("Here it is. It is", item)

               human.append(item)
               print("\nWith", item, "added, your current deck of cards is:")
               print_deck(human)

               print("And after discarding pairs and shuffling, your deck is:")
               human=remove_pairs(human)
               print_deck(human)

               wait_for_player()
               round_parity=1
          
          else:
               print("***********************************************************")
               print("My turn.\n")
               card_index=random.randint(0,len(human)-1)
               item=human[card_index]
               human.remove(item)
               dealer.append(item)
               dealer=remove_pairs(dealer)

               # handle the four endings of ordinals in English
               english_ordinals_end=["st", "nd", "rd", "th"]
               if card_index>2:
                   ord_index=3
               else:
                   ord_index=card_index

               print("I took your "+str(card_index+1)+english_ordinals_end[ord_index]+" card.")

               wait_for_player()
               round_parity=0
               
          
     if len(dealer)==0:
          print("Ups. I do not have any more cards")
          print("You lost! I, Robot, win")
     else:
          print("***********************************************************")
          print("Ups. You do not have any more cards")
          print("Congratulations! You, Human, win")
	
	 

# main program
play_game()
