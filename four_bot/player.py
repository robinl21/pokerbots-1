'''
Simple example pokerbot, written in Python.
'''
from skeleton.actions import FoldAction, CallAction, CheckAction, RaiseAction
from skeleton.states import GameState, TerminalState, RoundState
from skeleton.states import NUM_ROUNDS, STARTING_STACK, BIG_BLIND, SMALL_BLIND
from skeleton.bot import Bot
from skeleton.runner import parse_args, run_bot

import random
import eval7

class Player(Bot):
    '''
    A pokerbot.
    '''

    def __init__(self):
        '''
        Called when a new game starts. Called exactly once.
        Arguments:
        Nothing.
        Returns:
        Nothing.
        '''

    def handle_new_round(self, game_state, round_state, active):
        '''
        Called when a new round starts. Called NUM_ROUNDS times.
        Arguments:
        game_state: the GameState object.
        round_state: the RoundState object.
        active: your player's index.
        Returns:
        Nothing.
        '''
        #my_bankroll = game_state.bankroll  # the total number of chips you've gained or lost from the beginning of the game to the start of this round
        #game_clock = game_state.game_clock  # the total number of seconds your bot has left to play this game
        #round_num = game_state.round_num  # the round number from 1 to NUM_ROUNDS
        #my_cards = round_state.hands[active]  # your cards
        #big_blind = bool(active)  # True if you are the big blind
        self.first_raise = True

        self.we_have_firstraised = False

        self.small_blind = False


    # def guess_next_probability(self, my_hand, table_hand, street):
    #     #goal: calculating outs
    #     #generate power of a hand based on next card, see number of "outs" (to guarantee win)
    
    #     #TODO: use HOLE and TABLE_HAND to differentiate hand type scores smartly
    #         #value of a single pair decreases as holes increase (0.7 to lower)
    #         #draw hands decrease in value as holes increase #reds decrease lesss

    #         # if table_hand has pair: pair is now considered 0 (everyone has)
    #         # two pair: if biggest pair is the table one, pair is 0.7 normal. still hard to get
    #         #if nontable pair is bigger, go from 0.7 to 1 based on how much bigger it is than table pair


    #     #TODO: give value to hands close to string (drawing hand)/ close to flush (higher chance for reds)
    #     #make them 0.5, but lower as holes increase (when street is 4, draw hand is 0.2)
        
    #     #hand types: hand value from 0 to 1, intervals of 0.2 for high card, pair, two pair

    #     #initial vals
    #     draw_hand = 0.4 
    #     pair_val = 0.7
    #     two_pair = 0.8

    #     if street >= 3: #on flop, looking at value with 4 cards on table
    #         pair_val = 0.65
    #     if street >= 4: #looking at value with five cards on table
    #         pair_val = 0.6
    #         draw_hand = 0.2
    #     if street >= 5:
    #         pair_val = 0.5
    #         draw_hand = 0.2
        

    #     hand_types = {"High Card": 0, "Pair": pair_val, "Two Pair": two_pair, "Draw Hand": draw_hand, "Trips": 1, "Straight": 1, "Flush": 1,
    #                     "Full House": 1, "Quads": 1, "Straight Flush": 1}
    #     cur_hand_eval = [] #cur_hand held in eval7 Card class
    #     comm_cards = []

    #     probability_sum = 0
    #     count = 0

    #     #initialize deck,removing cards and adding to cur_hand
    #     deck = eval7.Deck()
    #     for card in my_hand:
    #         deck.cards.remove(eval7.Card(card))
    #         cur_hand_eval.append(eval7.Card(card))

    #     for card in table_hand:
    #         cur_hand_eval.append(eval7.Card(card))
    #         comm_cards.append(eval7.Card(card))
    #         deck.cards.remove(eval7.Card(card))

    #     #for each card left in the deck: add to hand, evaluate, then remove from hand
    #     for card in deck.cards:
    #         count += 1
    #         cur_hand_eval.append(card)
    #         comm_cards.append(card)
    #         evaluated_hand = eval7.evaluate(cur_hand_eval)
    #         handtype = eval7.handtype(evaluated_hand)

    #         evaluated_comm = eval7.evaluate(comm_cards)
    #         comm_handtype = eval7.handtype(evaluated_comm)

    #         if comm_handtype in {"Pair"}:
    #             pair_val = 0
    #             two_pair = 0.7

    #         #determine if drawhand or flush hand here
    #         # if drawhands have better value than high card or pair, replace with that value

    #         #evaluate highest card, adjust probability value
    #         if handtype in {"High Card", "Pair", "Two Pair"}:
    #             cur_hand_orig = set()
    #             max_pair = -1
    #             max_high_card = -1

    #             for cur_card in cur_hand_eval:
    #                 rank = cur_card.rank #numerical value 0 to 12, test (2, 3..A)
    #                 #print(rank)
    #                 #bigger card found: update max_high_card value
    #                 if rank > max_high_card:
    #                     max_high_card = rank


    #                 #pair found, already in set: update max_pair value
    #                 if rank in cur_hand_orig:
    #                     #print("Pair found")
    #                     if rank > max_pair: #if bigger pair
    #                         max_pair = rank

    #                 else: #otherwise add to set 
    #                     cur_hand_orig.add(rank)

    #             #based on handtype and rank of card, adjust
    #             if handtype == "High Card":
    #                 #print(hand_types[handtype] + max_high_card * 0.2/12)
    #                 probability_sum += (hand_types[handtype] + max_high_card * 0.2/12) #when max, adds 0.3

    #             else:
    #                 #print(hand_types[handtype] + max_pair * 0.2 / 12)
    #                 probability_sum += (hand_types[handtype] + max_pair * 0.2 / 12)

    #         else:
    #             probability_sum += hand_types[handtype]

    #         cur_hand_eval.remove(card) #remove from hand
    #         comm_cards.remove(card)

            
    #         #reset values
    #         draw_hand = 0.4 
    #         pair_val = 0.7
    #         two_pair = 0.8

    #         if street >= 3: #on flop, looking at value with 4 cards on table
    #             pair_val = 0.65
    #         if street >= 4: #looking at value with five cards on table
    #             pair_val = 0.6
    #             draw_hand = 0.2
    #         if street >= 5:
    #             pair_val = 0.5
    #             draw_hand = 0.2

    #     return probability_sum / count #probability from guessing

    def starting_hand(self, my_hand):
        #return True or False on whether to keep playing this hand
        pass

    def monte_carlo(self, my_hand, iterations, community = []):
        #using code from lecture-ref2 and 3, slightly modified for river of blood
        #probability of winning this round with current hand
        #TODO: consider river of blood. randomly decide 50 percent whether to draw another or not <completed>

        deck = eval7.Deck()
        cur_hand = []
        community_cards = []
        num_red_seen = 0

        #setup cur_hand and deck
        for card in my_hand:
            if card[1] == 'h' or card[1] == 'd':
                num_red_seen += 1
            cur_hand.append(eval7.Card(card))

        for card in cur_hand:
            deck.cards.remove(card)

        #remove community cards from deck
        if community != []:
            for card in community:
                if card[1] == 'h' or card[1] == 'd':
                    num_red_seen += 1
                community_cards.append(eval7.Card(card))

            for card in community_cards:
                deck.cards.remove(card)

        p = 0

        for i in range(iterations):
            deck.shuffle()

            #TODO: generate number of community cards (for now keep 5)

            #simulate red river
            #ratio: 52 total cards. reds: 26
            # (26 - num_red_seen) / (52 - cards_used)
            if len(community) >= 5:
                    if community[-1][1] == 'h' or community[-1][1] == 'd':
                        _COMM = 1 #guaranteed one more community card
                        num_cards_used = 2 + 2 + len(community) + 1 
                
                        red_prob = ((26 - num_red_seen) / (52 - num_cards_used)) * 100
                        
                        #guess whether next one is red or not
                        is_red = random.choices(population = [True, False], weights = [red_prob, 100 - red_prob], k = 1)
                        
                        while is_red[0]: #next guessed to be red
                            #draw additional red card
                            _COMM += 1
                            num_cards_used += 1
                            num_red_seen += 1
                            
                            red_prob = ((26 - num_red_seen) / (52 - num_cards_used)) * 100
                            
                            if red_prob <= 0 or red_prob >= 1:
                                red_prob = 0
                            #reselect
                            is_red = random.choices(population = [True, False], weights = [red_prob, 100 - red_prob], k = 1)

                    else: #last showdown, done flipping
                        _COMM = 0
            
            else:
                _COMM = 5 - len(community) #num of community cards needed to draw
                num_cards_used = 9 
                num_red_seen += int(_COMM / 2)#assume half of those we draw are red

                red_prob = (26 - num_red_seen) / (52 - num_cards_used)
                is_red = random.choices(population = [True, False], weights = [red_prob, 1 - red_prob], k = 1)

                while is_red[0]:
                    print("ADD RED")
                    _COMM += 1
                    num_cards_used += 1
                    num_red_seen += 1
                    red_prob = (26 - num_red_seen) / (52 - num_cards_used)
                            
                    if red_prob <= 0 or red_prob >= 1:
                        red_prob = 0
                    
                    is_red = random.choices(population = [True, False], weights = [red_prob, 1 - red_prob], k = 1)      
                    
            _OPP = 2

            draw = deck.peek(_COMM + _OPP)

            opp_hole = draw[:_OPP] 
            alt_community = draw[_OPP:]

            #generate hands
            our_hand = cur_hand + community_cards + alt_community
            opp_hand = opp_hole + community_cards + alt_community

            our_value = eval7.evaluate(our_hand)
            opp_value = eval7.evaluate(opp_hand)

            if our_value > opp_value:
                p += 2
            
            elif our_value == opp_value:
                p += 1

            else:
                p += 0

        p = p / (2 * iterations)

        return p

        # deck = eval7.Deck()
        # cur_hand = []
        # community_cards = []
        # num_red_seen = 0

        # #setup cur_hand and deck
        # for card in my_hand:
        #     if card[1] == 'h' or card[1] == 'd':
        #         num_red_seen += 1
        #     cur_hand.append(eval7.Card(card))

        # for card in cur_hand:
        #     deck.cards.remove(card)

        # #remove community cards from deck
        # if community != []:
        #     for card in community:
        #         if card[1] == 'h' or card[1] == 'd':
        #             num_red_seen += 1
        #         community_cards.append(eval7.Card(card))

        #     for card in community_cards:
        #         deck.cards.remove(card)

        # z = 0

        # for i in range(iterations):
        #     deck.shuffle()

        #     #TODO: generate number of community cards (for now keep 5)

        #     #simulate red river
        #     #ratio: 52 total cards. reds: 26
        #     # (26 - num_red_seen) / (52 - cards_used)
        #     if len(community) >= 5:
        #             if community[-1][1] == 'h' or community[-1][1] == 'd':

        #                 alt_community_cards = []

        #                 #peek at next
        #                 next_card = deck.deal(1)[0]
        #                 alt_community_cards.append(next_card)


        #                 #keep drawing
        #                 while next_card.suit in {1, 2}:
        #                     next_card = deck.deal(1)[0] #just want card, add to list
        #                     alt_community_cards.append(next_card)

        #                 #done: showdown
        #                 opp_hole = deck.deal(2) #list of 2

        #                 our_hand = cur_hand + community_cards + alt_community_cards
                        
        #                 opp_hand = opp_hole + community_cards + alt_community_cards

        #                 our_value = eval7.evaluate(our_hand)
        #                 opp_value = eval7.evaluate(opp_hand)


        #                 if our_value > opp_value:
        #                     z += 2
                        
        #                 elif our_value == opp_value:
        #                     z += 1

        #                 else:
        #                     z += 0

                        
        #                 #add all drawn back in (alt community and op hole)
                        
        #                 for card in alt_community_cards:
        #                     deck.cards.append(card)

        #                 for card in opp_hole:
        #                     deck.cards.append(card)

                        
        #             else: #last showdown, done flipping
        #                 _COMM = 0
        #                 _OPP = 2

        #                 draw = deck.peek(_COMM + _OPP)

        #                 opp_hole = draw[:_OPP] 
        #                 alt_community = draw[_OPP:]

        #                 #generate hands
        #                 our_hand = cur_hand + community_cards + alt_community
        #                 opp_hand = opp_hole + community_cards + alt_community

        #                 our_value = eval7.evaluate(our_hand)
        #                 opp_value = eval7.evaluate(opp_hand)

        #                 if our_value > opp_value:
        #                     z += 2
                        
        #                 elif our_value == opp_value:
        #                     z += 1

        #                 else:
        #                     z += 0


                        
        #     else:
        #         _COMM = 5 - len(community) #num of community cards needed to draw

        #         alt_community_cards = deck.deal(_COMM)
        #         opp_hole = deck.deal(2)

        #         next_card = alt_community_cards[-1]

                
        #         while next_card.suit in {1, 2}:
        #             next_card = deck.deal(1)[0] #draw one
        #             alt_community_cards.append(next_card)
                


        #         our_hand = cur_hand + community_cards + alt_community_cards
        #         opp_hand = opp_hole + community_cards + alt_community_cards

                

        #         our_value = eval7.evaluate(our_hand)
        #         opp_value = eval7.evaluate(opp_hand)

        #         if our_value > opp_value:
        #             z += 2

        #         elif our_value == opp_value:
        #             z += 1
        #         else:
        #             z += 0


        #         #add all drawn back in (alt community and op hole)
                        
        #         for card in alt_community_cards:
        #             deck.cards.append(card)

        #         for card in opp_hole:
        #             deck.cards.append(card)

        # z = z / (2 * iterations)
        
        # #print("results", p, z)
        # return z


    def handle_round_over(self, game_state, terminal_state, active):
        '''
        Called when a round ends. Called NUM_ROUNDS times.
        Arguments:
        game_state: the GameState object.
        terminal_state: the TerminalState object.
        active: your player's index.
        Returns:
        Nothing.
        '''
        #my_delta = terminal_state.deltas[active]  # your bankroll change from this round
        #previous_state = terminal_state.previous_state  # RoundState before payoffs
        #street = previous_state.street  # int of street representing when this round ended
        #my_cards = previous_state.hands[active]  # your cards
        #opp_cards = previous_state.hands[1-active]  # opponent's cards or [] if not revealed
        self.we_have_first_raised = False
        pass

    def hand_convert(self, card1, card2):
        '''
        Converts two cards 'rank+suite' into (biggest, smaller card + (s, o,))
        '''
        value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        rank1, rank2 = card1[0], card2[0]
        rank1, rank2 = value[rank1], value[rank2]

        suite1, suite2 = card1[1], card2[1]

        #number, suite, card
        card1 = (rank1, suite1, card1)
        card2 = (rank2, suite2, card2)

        if card1[0] == card2[0]: #same rank
            to_return = (card1[2][0], card2[2][0]) #pair
        elif card1[0] > card2[0]: #card1 bigger
            if card1[1] == card2[1]: #same suite
                to_return = (card1[2][0], card2[2][0] + 's')
            else:
                to_return = (card1[2][0], card2[2][0] + 'o')
        elif card1[0] < card2[0]:
            if card1[1] == card2[1]: #same suite
                to_return = (card2[2][0], card1[2][0] + 's')
            else:
                to_return = (card2[2][0], card1[2][0] + 'o')
        print(to_return)
        return to_return


    def legalize_raise(self, raise_amount, min_raise, max_raise, my_pip, continue_cost, my_stack, legal_actions):
        '''
        Legalizes raise action. raise -> call > check -> flop
        '''
        # temp_action: best we can do if we want to raise

        #get legal raise amount
        raise_amount = max([min_raise, raise_amount])
        if raise_amount > max_raise:
            raise_amount = max_raise

        if raise_amount == 400:
            raise_amount = max_raise
    
        raise_cost = raise_amount - my_pip

        print("Raise cost", raise_cost, my_stack)

        if (RaiseAction in legal_actions and (raise_cost <= my_stack)): #raise legal
            temp_action = RaiseAction(raise_amount)

        elif (CallAction in legal_actions and (continue_cost <= my_stack)): #continue legal
            temp_action = CallAction()

        elif CheckAction in legal_actions: 
            temp_action = CheckAction()
        else:
            temp_action = FoldAction()

        return temp_action


    def get_action(self, game_state, round_state, active):
        '''
        Where the magic happens - your code should implement this function.
        Called any time the engine needs an action from your bot.
        Arguments:
        game_state: the GameState object.
        round_state: the RoundState object.
        active: your player's index.
        Returns:
        Your action.
        '''
        #borrows some code from lecture 2 reference (logic for actions)
        legal_actions = round_state.legal_actions()  # the actions you are allowed to take
        street = round_state.street  # int representing pre-flop, flop, turn, or river respectively
        my_cards = round_state.hands[active]  # your cards
        board_cards = round_state.deck[:street]  # the board cards
        my_pip = round_state.pips[active]  # the number of chips you have contributed to the pot this round of betting
        opp_pip = round_state.pips[1-active]  # the number of chips your opponent has contributed to the pot this round of betting
        my_stack = round_state.stacks[active]  # the number of chips you have remaining
        opp_stack = round_state.stacks[1-active]  # the number of chips your opponent has remaining
        continue_cost = opp_pip - my_pip  # the number of chips needed to stay in the pot
        my_contribution = STARTING_STACK - my_stack  # the number of chips you have contributed to the pot
        opp_contribution = STARTING_STACK - opp_stack  # the number of chips your opponent has contributed to the pot
        
        #0 index - 2 index: 70 percent, 82.5 percent hand, 91 percent hand
        #3 index - 4 index: value hands (tight), polarized (loose)
        ranges = {
            'A': {'A': ['Raise', 'Raise', 'Raise', 'Raise'], 
                    'Ko': ['Raise', 'Raise', 'Raise', 'Raise'], 'Qo': ['Raise', 'Raise', 'Raise', 'Raise'], 'Jo': ['Raise', 'Raise', 'Raise', 'Raise'], 'To': ['Raise', 'Raise', 'Raise', 'Raise'], '9o': ['Raise', 'Raise', 'Raise', 'Fold'],
                    '8o': ['Raise', 'Raise', 'Raise', 'Fold'], '7o': ['Raise', 'Raise', 'Raise', 'Fold'], '6o': ['Raise', 'Raise', 'Raise', 'Fold'], '5o': ['Raise', 'Raise', 'Raise', 'Fold'], '4o': ['Raise', 'Raise', 'Raise', 'Fold'], '3o': ['Raise', 'Raise', 'Raise', 'Fold'], '2o': ['Raise', 'Raise', 'Raise', 'Fold'], 
                    'Ks': ['Raise', 'Raise', 'Raise', 'Raise'], 'Qs': ['Raise', 'Raise', 'Raise', 'Raise'], 'Js': ['Raise', 'Raise', 'Raise', 'Raise'], 'Ts': ['Raise', 'Raise', 'Raise', 'Raise'], '9s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '8s': ['Raise', 'Raise', 'Raise', 'Call'], '7s': ['Raise', 'Raise', 'Raise', 'Call'], '6s': ['Raise', 'Raise', 'Raise', 'Call'], '5s': ['Raise', 'Raise', 'Raise', 'Call'], '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '2s': ['Raise', 'Raise', 'Raise', 'Call'], 
            },

            'K': {'K': ['Raise', 'Raise', 'Raise', 'Raise'], 'Qo': ['Raise', 'Raise', 'Raise', 'Raise'], 'Jo': ['Raise', 'Raise', 'Raise', 'Raise'], 'To': ['Raise', 'Raise', 'Raise', 'Raise'], '9o': ['Raise', 'Raise', 'Raise', 'Fold'],
                    '8o': ['Raise', 'Raise', 'Raise', 'Fold'], '7o': ['Raise', 'Raise', 'Raise', 'Fold'], '6o': ['Raise', 'Raise', 'Raise', 'Fold'], '5o': ['Raise', 'Raise', 'Raise', 'Fold'], '4o': ['Raise', 'Raise', 'Raise', 'Fold'], '3o': ['Raise', 'Raise', 'Raise', 'Fold'],
                    '2o': ['Raise', 'Raise', 'Raise', 'Fold'], 'Qs': ['Raise', 'Raise', 'Raise', 'Raise'], 'Js': ['Raise', 'Raise', 'Raise', 'Raise'], 'Ts': ['Raise', 'Raise', 'Raise', 'Raise'], '9s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '8s': ['Raise', 'Raise', 'Raise', 'Call'], '7s': ['Raise', 'Raise', 'Raise', 'Call'], '6s': ['Raise', 'Raise', 'Raise', 'Call'], '5s': ['Raise', 'Raise', 'Raise', 'Call'], '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '2s': ['Raise', 'Raise', 'Raise', 'Call'], 
            },

            'Q': {'Q': ['Raise', 'Raise', 'Raise', 'Raise'], 'Jo': ['Raise', 'Raise', 'Raise', 'Raise'], 'To': ['Raise', 'Raise', 'Raise', 'Fold'], '9o': ['Raise', 'Raise', 'Raise', 'Fold'],
                    '8o': ['Raise', 'Raise', 'Raise', 'Fold'], '7o': ['Raise', 'Raise', 'Raise', 'Fold'], '6o': ['Raise', 'Raise', 'Raise', 'Fold'], '5o': ['Raise', 'Raise', 'Raise', 'Fold'], '4o': ['Raise', 'Raise', 'Raise', 'Fold'], '3o': ['Raise', 'Raise', 'Raise', 'Fold'],
                    '2o': ['Fold', 'Raise', 'Raise', 'Fold'], 'Js': ['Raise', 'Raise', 'Raise', 'Raise'], 'Ts': ['Raise', 'Raise', 'Raise', 'Raise'], '9s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '8s': ['Raise', 'Raise', 'Raise', 'Call'], '7s': ['Raise', 'Raise', 'Raise', 'Call'], '6s': ['Raise', 'Raise', 'Raise', 'Call'], '5s': ['Raise', 'Raise', 'Raise', 'Call'], '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '2s': ['Raise', 'Raise', 'Raise', 'Call'], 
            },

            'J': {'J': ['Raise', 'Raise', 'Raise', 'Raise'], 'To': ['Raise', 'Raise', 'Raise', 'Fold'], '9o': ['Raise', 'Raise', 'Raise', 'Fold'],
                    '8o': ['Raise', 'Raise', 'Raise', 'Fold'], '7o': ['Raise', 'Raise', 'Raise', 'Fold'], '6o': ['Raise', 'Raise', 'Raise', 'Fold'], '5o': ['Raise', 'Raise', 'Raise', 'Fold'], '4o': ['Fold', 'Raise', 'Raise', 'Fold'], '3o': ['Fold', 'Raise', 'Raise', 'Fold'],
                    '2o': ['Fold', 'Raise', 'Raise', 'Fold'], 'Ts': ['Raise', 'Raise', 'Raise', 'Raise'], '9s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '8s': ['Raise', 'Raise', 'Raise', 'Call'], '7s': ['Raise', 'Raise', 'Raise', 'Call'], '6s': ['Raise', 'Raise', 'Raise', 'Call'], '5s': ['Raise', 'Raise', 'Raise', 'Call'], '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '2s': ['Raise', 'Raise', 'Raise', 'Call'], 
            },

            'T': {'T': ['Raise', 'Raise', 'Raise', 'Raise'], '9o': ['Raise', 'Raise', 'Raise', 'Fold'],
                    '8o': ['Raise', 'Raise', 'Raise', 'Fold'], '7o': ['Raise', 'Raise', 'Raise', 'Fold'], '6o': ['Raise', 'Raise', 'Raise', 'Fold'], '5o': ['Fold', 'Raise', 'Raise', 'Fold'], '4o': ['Fold', 'Raise', 'Raise', 'Fold'], '3o': ['Fold', 'Fold', 'Raise', 'Fold'],
                    '2o': ['Fold', 'Fold', 'Raise', 'Fold'], '9s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '8s': ['Raise', 'Raise', 'Raise', 'Call'], '7s': ['Raise', 'Raise', 'Raise', 'Call'], '6s': ['Raise', 'Raise', 'Raise', 'Call'], '5s': ['Raise', 'Raise', 'Raise', 'Call'], '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '2s': ['Raise', 'Raise', 'Raise', 'Call'], 

            },

            '9': {'9': ['Raise', 'Raise', 'Raise', 'Raise'],
                    '8o': ['Raise', 'Raise', 'Raise', 'Fold'], '7o': ['Raise', 'Raise', 'Raise', 'Fold'], '6o': ['Raise', 'Raise', 'Raise', 'Fold'], '5o': ['Fold', 'Raise', 'Raise', 'Fold'], '4o': ['Fold', 'Fold', 'Raise', 'Fold'], '3o': ['Fold', 'Fold', 'Raise', 'Fold'],
                    '2o': ['Fold', 'Fold', 'Fold', 'Fold'],
                    '8s': ['Raise', 'Raise', 'Raise', 'Call'], '7s': ['Raise', 'Raise', 'Raise', 'Call'], '6s': ['Raise', 'Raise', 'Raise', 'Call'], '5s': ['Raise', 'Raise', 'Raise', 'Call'], '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '2s': ['Call', 'Raise', 'Raise', 'Call']

            },

            '8': {'8': ['Raise', 'Raise', 'Raise', 'Raise'],
                 '7o': ['Raise', 'Raise', 'Raise', 'Fold'], '6o': ['Raise', 'Raise', 'Raise', 'Fold'], '5o': ['Fold', 'Raise', 'Raise', 'Fold'], '4o': ['Fold', 'Fold', 'Raise', 'Fold'], '3o': ['Fold', 'Fold', 'Fold', 'Fold'],
                    '2o': ['Fold', 'Fold', 'Fold', 'Fold'],
                    '7s': ['Raise', 'Raise', 'Raise', 'Call'], '6s': ['Raise', 'Raise', 'Raise', 'Call'], '5s': ['Raise', 'Raise', 'Raise', 'Call'], '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Call', 'Raise', 'Raise', 'Call'],
                    '2s': ['Call', 'Raise', 'Raise', 'Call'], 

            },

            '7': {'7': ['Raise', 'Raise', 'Raise', 'Call'],
                 '6o': ['Raise', 'Raise', 'Raise', 'Fold'], '5o': ['Fold', 'Raise', 'Raise', 'Fold'], '4o': ['Fold', 'Fold', 'Raise', 'Fold'], '3o': ['Fold', 'Fold', 'Fold', 'Fold'],
                    '2o': ['Fold', 'Fold', 'Fold', 'Fold'],
                    '6s': ['Raise', 'Raise', 'Raise', 'Call'], '5s': ['Raise', 'Raise', 'Raise', 'Call'], '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Call', 'Raise', 'Raise', 'Call'],
                    '2s': ['Call', 'Raise', 'Raise', 'Call'], 

            },

            '6': {'6': ['Raise', 'Raise', 'Raise', 'Call'],
                 '5o': ['Fold', 'Raise', 'Raise', 'Fold'], '4o': ['Fold', 'Fold', 'Raise', 'Fold'], '3o': ['Fold', 'Fold', 'Raise', 'Fold'],
                    '2o': ['Fold', 'Fold', 'Fold', 'Fold'],
                   '5s': ['Raise', 'Raise', 'Raise', 'Call'], '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '2s': ['Call', 'Raise', 'Raise', 'Call'], 

            },

            '5': {'5': ['Raise', 'Raise', 'Raise', 'Call'],
                 '4o': ['Fold', 'Raise', 'Raise', 'Fold'], '3o': ['Fold', 'Fold', 'Raise', 'Fold'],
                    '2o': ['Fold', 'Fold', 'Fold', 'Fold'],
                 '4s': ['Raise', 'Raise', 'Raise', 'Call'], '3s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '2s': ['Call', 'Raise', 'Raise', 'Call'], 
            },

            '4': {'4': ['Raise', 'Raise', 'Raise', 'Call'],
                 '3o': ['Fold', 'Fold', 'Fold', 'Fold'],
                    '2o': ['Fold', 'Fold', 'Fold', 'Fold'],
                   '3s': ['Raise', 'Raise', 'Raise', 'Call'],
                    '2s': ['Call', 'Raise', 'Raise', 'Call'], 
            },

            '3': {'3': ['Raise', 'Raise', 'Raise', 'Call'], 
                    '2o': ['Fold', 'Fold', 'Fold', 'Fold', 'Fold'],
                    '2s': ['Call', 'Call', 'Raise', 'Call']},

            '2': {'2': ['Raise', 'Raise', 'Raise', 'Call']
            }
        
        }
        
        if my_pip == 1:
            print("I AM SMALL BLIND")
            self.small_blind = True #sets true at beginning of round

        min_raise, max_raise = round_state.raise_bounds() 
        my_action = None
        

        pot_total = my_contribution + opp_contribution

        #calculate p of cards
        monte_carlo_p = self.monte_carlo(my_cards, 100, board_cards)
        #guess_p = self.guess_next_probability(my_cards, board_cards, street)
        print(my_cards)
        print(board_cards)
        print("monte", monte_carlo_p)

        p = monte_carlo_p

        scary = 0
        #TODO: try to consider opponent range and raises from previous rounds
        #fix p based on opponent's bets (keep low since don't want to kill too early)
        if continue_cost > 0:
            scary = 0

            if continue_cost > 6:
                scary = 0.1

            if continue_cost > 12:
                scary = 0.2

            if continue_cost > 50:
                scary= 0.35

        print("p", p)
        prefix_p = p #before scary modification
        p = max([0, p - scary])
        print("fixed p", p)

        pot_odds = continue_cost / (pot_total + continue_cost) #p*pot_total + (1-p)*cost_to_continue (don't care about previous sunk costs)
        print("pot odds", pot_odds)

        #temporary raise_amount logic
                # raise logic: kill early, raise higher (TAG)
                #kill preflop if nothing raised this round
        print(my_pip)

        if self.small_blind:
            if street < 3: #preflop: implement folding early via bill chen formula
                card1 = my_cards[0]
                card2 = my_cards[1]
                if continue_cost > 0: #raise
                    #opening raise from small blind: continue_cost = 1, my_pip = 1
                    #adjust later: currently 2.5 x BB
                    if continue_cost == 1 and my_pip == 1: 
                        print("SMALL BLIND INITIAL")
                        hand = self.hand_convert(card1, card2)
                        decision = ranges[hand[0]][hand[1]][2] #open most from small blind
                    
                        if decision == "Raise":
                            self.we_have_firstraised = True
                            raise_amount = 5
                            return self.legalize_raise(raise_amount, min_raise, max_raise, my_pip, continue_cost, my_stack, legal_actions)
                        
                        elif decision == "Call": #only call available
                            return CallAction()

                        elif decision == "Fold":
                            return FoldAction()

                    #three-bet: our first raise encountered this game (non-including small blind)
                    #adjust to opponents!! 
                    elif self.first_raise:
                        
                        self.first_raise = False
                        #three-betting
                        hand = self.hand_convert(card1, card2)

                        print("WADADA")

                        print("Prepare to 3-BET")
                        decision = ranges[hand[0]][hand[1]][3]

                        # if self.we_have_firstraised:
                        #     print("WE RECEIVE 3BET, 4BET decision")
                        #     raise_amount = opp_pip * 2
                        #     join_hand = hand[0] + hand[1]

                        #     to_raise = {'AA', 'AKs', 'AQs', 'AJs', 'AKo', 'KK', 'KQs', 'AQo', 'QQ', 'JJ', 'TT'}
                        #     to_call = {'99', '88', '77', '66', '55', '44', '33', '22'}

                        #     if join_hand in to_raise:
                        #         decision = "Raise"
                        #     elif join_hand in to_call or hand[1][-1] == 's':
                        #         decision = "Call"
                        #     else:
                        #         decision = "Fold"

                            
                        #     print("OUR DECISION", decision)

                        #     if decision == "Raise":
                        #         return self.legalize_raise(raise_amount, min_raise, max_raise, my_pip, continue_cost, my_stack, legal_actions)
                        #     elif decision == "Call":
                        #         return CallAction()
                        #     elif decision == "Fold":
                        #         #if we would 3-bet this, occassionally call
                        #         if ranges[hand[0]][hand[1]][3] == "Raise" and p > pot_odds and p > 0.5:
                        #             print("SAVE!")
                        #             return CallAction()
                        #         return FoldAction()
                            
                            
                        # else:
                        
                        print("3BET NOW, meaning we called earlier")
                        raise_amount = 3 * opp_pip
                        decision = ranges[hand[0]][hand[1]][3]
                        if decision == "Raise":
                            #raise 3x amount of continue cost
                            if self.we_have_firstraised is False:
                                self.we_have_firstraised = True
                            return self.legalize_raise(raise_amount, min_raise, max_raise, my_pip, continue_cost, my_stack, legal_actions)
                        
                        elif decision == "Call": #only call available
                            return CallAction()

                        elif decision == "Fold": #don't always fold
                            if p > pot_odds and p > 0.5:
                                return CallAction()
                            return FoldAction()
                                

                    else:
                        #raise beyond first raise
                        print("CONTINUED RAISE")
                        raise_amount = int(my_pip + continue_cost + 0.4*(pot_total + continue_cost))
                    
                        raise_amount = max([min_raise, raise_amount]) #biggest one out of min/calculated raise
                
                        if raise_amount > max_raise: #out of bounds (min > max or calculated > max), do max raise
                            raise_amount = max_raise #all-in
                        
                        raise_cost = raise_amount - my_pip #cost to raise

                        #legalize action here: Func

                        # temp_action: best we can do if we want to raise/continue
                        if (RaiseAction in legal_actions and (raise_cost <= my_stack)): #raise legal
                            temp_action = RaiseAction(raise_amount)

                        elif (CallAction in legal_actions and (continue_cost <= my_stack)): #continue legal
                            temp_action = CallAction()

                        elif CheckAction in legal_actions: 
                            temp_action = CheckAction()
                        else:
                            temp_action = FoldAction()

                        
                        #if pay to keep playing: raise, call, or fold
                        if continue_cost > 0: 
                            
                            if p > pot_odds: #call or raise, don't fold
                                if p > 0.5 and  random.random() < p: #bigger p is, more likely to raise
                                    my_action = temp_action #best we can do if want to raise

                                else:
                                    my_action = CallAction()
                            else: 
                            #   Fold
                                my_action = FoldAction()
                        
                        else: #pay 0 to play, want to either raise or check
                            if random.random() < p:
                                my_action = temp_action
                            else:
                                my_action = CheckAction()
                        

                        return my_action

                else: #continue_cost == 0:
                    print("DO I EXIST?")
                    #big blind first opening raise: same logic as small blind opening raise, except only raise/check
                    hand = self.hand_convert(card1, card2)
                    decision = ranges[hand[0]][hand[1]][1]
                
                    if decision == "Raise":
                        self.we_have_firstraised = True
                        raise_amount = 5
                        temp_action = self.legalize_raise(raise_amount, min_raise, max_raise, my_pip, continue_cost, my_stack, legal_actions)
                        print(temp_action)
                        return temp_action
                    else:
                        return CheckAction()

            
            else: #postflop, 66 percent of pot. normal play
                raise_amount = int(my_pip + continue_cost + (0.75)*(pot_total + continue_cost))
            
                raise_amount = max([min_raise, raise_amount]) #biggest one out of min/calculated raise
        
                if raise_amount > max_raise: #out of bounds (min > max or calculated > max), do max raise
                    raise_amount = max_raise #all-in
                
                raise_cost = raise_amount - my_pip #cost to raise

                #legalize action here: Func

                # temp_action: best we can do if we want to raise/continue
                if (RaiseAction in legal_actions and (raise_cost <= my_stack)): #raise legal
                    if p < 0.7:
                        raise_amount = int(my_pip + continue_cost + (2/3)*(pot_total + continue_cost))
                    temp_action = RaiseAction(raise_amount)

                elif (CallAction in legal_actions and (continue_cost <= my_stack)): #continue legal
                    temp_action = CallAction()

                elif CheckAction in legal_actions: 
                    temp_action = CheckAction()
                else:
                    temp_action = FoldAction()

                
                #if pay to keep playing: raise, call, or fold
                if continue_cost > 0: 
                    
                    if p > pot_odds: #call or raise, don't fold
                        if p > 0.5 and  random.random() < p: #bigger p is, more likely to raise
                            my_action = temp_action #best we can do if want to raise

                        else: #we are smallblind:
                            my_action = CallAction()
                    else: 
                    #   Fold
                        my_action = FoldAction()
                
                else: #pay 0 to play, want to either raise or check
                    if random.random() < p:
                        my_action = temp_action
                    else:
                        my_action = CheckAction()
                

                return my_action


        else:
            if street < 3: #preflop: implement folding early via bill chen formula
                card1 = my_cards[0]
                card2 = my_cards[1]
                if continue_cost > 0: #raise
                    #opening raise from small blind: continue_cost = 1, my_pip = 1
                    #adjust later: currently 2.5 x BB
                    if continue_cost == 1 and my_pip == 1: 
                        print("SMALL BLIND INITIAL")
                        hand = self.hand_convert(card1, card2)
                        decision = ranges[hand[0]][hand[1]][0] #make this 45 percent of hands
                    
                        if decision == "Raise":
                            self.we_have_firstraised = True
                            raise_amount = 5
                            return self.legalize_raise(raise_amount, min_raise, max_raise, my_pip, continue_cost, my_stack, legal_actions)
                        
                        elif decision == "Call": #only call available
                            return CallAction()

                        elif decision == "Fold":
                            return FoldAction()

                    #three-bet: our first raise encountered this game (non-including small blind)
                    #adjust to opponents!! 
                    elif self.first_raise:
                        
                        print("3 BET")
                        self.first_raise = False
                        #three-betting
                        hand = self.hand_convert(card1, card2)

                        decision = ranges[hand[0]][hand[1]][3] #make this 15 percent of hands

                        if self.we_have_firstraised:
                            print("WE RECEIVE 3BET")

                        else:
                            print("DECIDE 3BET")

                        if decision == "Raise":
                            #raise 3x amount of continue cost
                            raise_amount = opp_pip * 3
                            if self.we_have_firstraised is False:
                                self.we_have_firstraised = True
                            return self.legalize_raise(raise_amount, min_raise, max_raise, my_pip, continue_cost, my_stack, legal_actions)
                        
                        elif decision == "Call": #only call available
                            return CallAction()

                        elif decision == "Fold": #don't always fold
                            # if p > pot_odds and p > 0.5:
                            #     return CallAction()
                            # else:
                            return FoldAction()
                            

                    else:
                        #raise beyond first raise
                        print("CONTINUED RAISE")
                        raise_amount = int(my_pip + continue_cost + 0.4*(pot_total + continue_cost))
                    
                        raise_amount = max([min_raise, raise_amount]) #biggest one out of min/calculated raise
                
                        if raise_amount > max_raise: #out of bounds (min > max or calculated > max), do max raise
                            raise_amount = max_raise #all-in
                        
                        raise_cost = raise_amount - my_pip #cost to raise

                        #legalize action here: Func

                        # temp_action: best we can do if we want to raise/continue
                        if (RaiseAction in legal_actions and (raise_cost <= my_stack)): #raise legal
                            temp_action = RaiseAction(raise_amount)

                        elif (CallAction in legal_actions and (continue_cost <= my_stack)): #continue legal
                            temp_action = CallAction()

                        elif CheckAction in legal_actions: 
                            temp_action = CheckAction()
                        else:
                            temp_action = FoldAction()

                        
                        #if pay to keep playing: raise, call, or fold
                        if continue_cost > 0: 
                            
                            if p > pot_odds: #call or raise, don't fold
                                if p > 0.5 and  random.random() < p: #bigger p is, more likely to raise
                                    my_action = temp_action #best we can do if want to raise

                                else:
                                    my_action = CallAction()
                            else: 
                            #   Fold
                                my_action = FoldAction()
                        
                        else: #pay 0 to play, want to either raise or check
                            if random.random() < p:
                                my_action = temp_action
                            else:
                                my_action = CheckAction()
                        

                        return my_action

                else: #continue_cost == 0:
                    print("BIG BLIND OPENING RAISE")
                    #big blind first opening raise: same logic as small blind opening raise, except only raise/check
                    hand = self.hand_convert(card1, card2)
                    decision = ranges[hand[0]][hand[1]][1]
                
                    if decision == "Raise":
                        self.we_have_firstraised = True
                        raise_amount = 5
                        temp_action = self.legalize_raise(raise_amount, min_raise, max_raise, my_pip, continue_cost, my_stack, legal_actions)
                        print(temp_action)
                        return temp_action
                    else:
                        return CheckAction()

            
            else: #postflop, 66 percent of pot. normal play straightforward
                raise_amount = int(my_pip + continue_cost + (0.5)*(pot_total + continue_cost))
            
                raise_amount = max([min_raise, raise_amount]) #biggest one out of min/calculated raise
        
                if raise_amount > max_raise: #out of bounds (min > max or calculated > max), do max raise
                    raise_amount = max_raise #all-in
                
                raise_cost = raise_amount - my_pip #cost to raise

                #legalize action here: Func

                # temp_action: best we can do if we want to raise/continue
                if (RaiseAction in legal_actions and (raise_cost <= my_stack)): #raise legal
                    if p >= 0.7:
                        raise_amount = int(my_pip + continue_cost + (2/3)*(pot_total + continue_cost))
                    temp_action = RaiseAction(raise_amount)

                elif (CallAction in legal_actions and (continue_cost <= my_stack)): #continue legal
                    temp_action = CallAction()

                elif CheckAction in legal_actions: 
                    temp_action = CheckAction()
                else:
                    temp_action = FoldAction()

                
                #if pay to keep playing: raise, call, or fold
                if continue_cost > 0: 
                    
                    if p > pot_odds: #call or raise, don't fold
                        if p > 0.5 and  random.random() < p: #bigger p is, more likely to raise
                            my_action = temp_action #best we can do if want to raise

                        else:
                            my_action = CallAction()
                    else: 
                    #   Fold
                        my_action = FoldAction()
                
                else: #pay 0 to play, want to either raise or check
                    if random.random() < p:
                        my_action = temp_action
                    else:
                        my_action = CheckAction()
                

                return my_action



if __name__ == '__main__':
    run_bot(Player(), parse_args())