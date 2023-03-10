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
        pass


    def guess_next_probability(self, my_hand, table_hand, hole):
        #need current hand and table's hand
        #remove all in my_hand and table_hand from eval7 deck
        #hole: # rounds so far
    
        #TODO: use HOLE and TABLE_HAND to differentiate hand type scores smartly
        #TODO: give value to hands close to string (drawing hand)
        
        #hand types: hand value from 0 to 1, intervals of 0.2 for high card, pair, two pair
        hand_types = {"High Card": 0, "Pair": 0.7, "Two Pair": 0.8, "Trips": 1, "Straight": 1, "Flush": 1,
                        "Full House": 1, "Quads": 1, "Straight Flush": 1}
        cur_hand_eval = [] #cur_hand held in eval7 Card class

        probability_sum = 0
        count = 0

        #initialize deck,removing cards and adding to cur_hand
        deck = eval7.Deck()
        for card in my_hand:
            deck.cards.remove(eval7.Card(card))
            cur_hand_eval.append(eval7.Card(card))

        for card in table_hand:
            cur_hand_eval.append(eval7.Card(card))
            deck.cards.remove(eval7.Card(card))

        #for each card left in the deck: add to hand, evaluate, then remove from hand
        for card in deck.cards:
            count += 1
            cur_hand_eval.append(card)
            evaluated_hand = eval7.evaluate(cur_hand_eval)
            handtype = eval7.handtype(evaluated_hand)

            #evaluate highest card, adjust probability value
            if handtype in {"High Card", "Pair", "Two Pair"}:
                cur_hand_orig = set()
                max_pair = -1
                max_high_card = -1

                for cur_card in cur_hand_eval:
                    rank = cur_card.rank #numerical value 0 to 12, test (2, 3..A)
                    #print(rank)
                    #bigger card found: update max_high_card value
                    if rank > max_high_card:
                        max_high_card = rank


                    #pair found, already in set: update max_pair value
                    if rank in cur_hand_orig:
                        #print("Pair found")
                        if rank > max_pair: #if bigger pair
                            max_pair = rank

                    else: #otherwise add to set 
                        cur_hand_orig.add(rank)

                #based on handtype and rank of card, adjust
                if handtype == "High Card":
                    #print(hand_types[handtype] + max_high_card * 0.2/12)
                    probability_sum += (hand_types[handtype] + max_high_card * 0.2/12) #when max, adds 0.3

                else:
                    #print(hand_types[handtype] + max_pair * 0.2 / 12)
                    probability_sum += (hand_types[handtype] + max_pair * 0.2 / 12)

            else:
                probability_sum += hand_types[handtype]

            cur_hand_eval.remove(card) #remove from hand
        
        return probability_sum / count #probability from guessing

    def monte_carlo(self, my_hand, iterations):
        #using code from lecture-ref2, slightly modified for river of blood
        #probability of winning this round with current hand
        #TODO: consider river of blood. randomly decide 50 percent whether to draw another or not

        deck = eval7.Deck()
        cur_hand = []

        #setup cur_hand and deck
        for card in my_hand:
            cur_hand.append(eval7.Card(card))

        for card in cur_hand:
            deck.cards.remove(card)

        p = 0

        for i in range(iterations):
            deck.shuffle()

            #TODO: generate number of community cards (for now keep 5)

            _COMM = 5 #num of community cards
            _OPP = 2

            draw = deck.peek(_COMM + _OPP)

            opp_hole = draw[:_OPP] 
            community = draw[_OPP:]

            our_hand = cur_hand +  community
            opp_hand = opp_hole +  community

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
        pass

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
        
        
        min_raise, max_raise = round_state.raise_bounds() 
        my_action = None

        pot_total = my_contribution + opp_contribution

        #calculate p of cards
        monte_carlo_p = self.monte_carlo(my_cards, 100)
        guess_p = self.guess_next_probability(my_cards, board_cards, street)
        print("monte", monte_carlo_p)
        print("guess", guess_p)
        p = (monte_carlo_p + guess_p) / 2 #average

        scary = 0
        #fix p based on opponent's bets
        if continue_cost > 0:
            scary = 0

            if continue_cost > 6:
                scary = 0.15

            if continue_cost > 12:
                scary = 0.25

            if continue_cost > 50:
                scary= 0.35

        print("p", p)
        p = max([0, p - scary])
        print("fixed p", p)

        #generate raise amount accordingly from p and street to 2:1 odds, or 33 percent
        raise_amount = 3 * opp_pip + (pot_total - my_pip - opp_pip) #3*opponents bet + pot before bets
        raise_amount = max([min_raise, raise_amount]) #biggest one out of min/calculated raise
        
        if raise_amount > max_raise: #out of bounds (min > max or calculated > max), do max raise
            raise_amount = max_raise #all-in
        
        raise_cost = raise_amount - my_pip #cost to raise

        # temp_action: best we can do if we want to raise/continue
        if (RaiseAction in legal_actions and (raise_cost <= my_stack)): #raise legal
            temp_action = RaiseAction(raise_amount)

        elif (CallAction in legal_actions and (continue_cost <= my_stack)): #continue legal
            temp_action = CallAction()

        elif CheckAction in legal_actions: 
            temp_action = CheckAction()
        else:
            temp_action = FoldAction()

        #based on opponent's bet this round, p > this then positive expected value

        pot_odds = continue_cost / (pot_total + continue_cost) #p*pot_total + (1-p)*cost_to_continue (don't care about previous sunk costs)
        print(pot_odds)
        
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
