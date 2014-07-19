"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    
    max_in_list = max(list(hand))
    max_v = 0;
    for val in range(1,max_in_list+1):
        score_r = 0;
        for item in hand:
            if item == val:
                score_r += val
        if score_r > max_v:
            max_v = score_r
    return max_v

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    
    if num_free_dice == 0:
        return float(score(held_dice))
    choices = gen_all_sequences(range(1, num_die_sides+1), num_free_dice)
    summ = 0.0
    #held_list = list(held_dice)
    for choice in choices:
        #new_list = list(choice)
        #new_list.extend(held_list)
        summ += score(held_dice + choice)
        #print new_list, summ
    return summ/len(choices)
 
    
def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer = set([()]);
    if len(hand) == 0:
        return answer
    if len(hand) == 1:
        answer.add(hand)
    else:
        answer = set();
        for idx in range(len(hand)):
            lst = list(hand)
            item = lst.pop(idx);
            tmp_set = gen_all_holds(tuple(lst))
            for elem in tmp_set:
                answer.add(elem);
                elem_list = list(elem)
                elem_list.append(item)
                elem_list.sort()
                answer.add(tuple(elem_list))
    return answer;

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    
    max_score = 0.0;
    max_hold = ();
    for item in gen_all_holds(hand):
        #print item
        exp = expected_value(item, num_die_sides, len(hand) - len(item))
        if exp > max_score:
            max_score = exp
            max_hold = item
    return (max_score, max_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    #hand = (6, 6, 6, 6, 6)
    hand = (1,2)
    hand_score, hold = strategy(hand, num_die_sides)
    
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
#print score((3, 3, 5, 5, 6))
#print score((3, 3, 5, 5, 12))
#print score((3, 3, 5, 5,3,5,5, 16))
#print gen_all_holds((1,))
#print gen_all_holds((2,1,2))
#print gen_all_holds((1,1,1,5,6))

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
#hand = tuple((1, 2, 2))
#print dir(poc_holds_testsuite)

#print dir(poc_holds_testsuite.poc_simpletest) 
#print gen_all_sequences(range(1,3), 2)

#print expected_value((1,1,1,1), 6, 1)
#print expected_value((), 6, 5)

#print expected_value((3, 3), 8, 5) 
#run_example()

print score((3, 3, 5, 5, 6))
print score((3, 3, 5, 5, 12))
print score((3, 3, 5, 5,3,5,5, 16))


print gen_all_holds((1,))
print gen_all_holds((2,1,2))
print gen_all_holds((1,1,1,5,6))

import poc_holds_testsuite
poc_holds_testsuite.run_suite(gen_all_holds)
                                       
hand = tuple((1, 2, 2))
print dir(poc_holds_testsuite)

print dir(poc_holds_testsuite.poc_simpletest)

#print poc_holds_testsuite

#suite.suite.run_test(gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)]), "Test #13:")
    
    
print gen_all_sequences(range(1,3), 2)

print expected_value((1,1,1,1), 6, 1)
print expected_value((), 6, 5)


run_example()

 
    
 #http://www.codeskulptor.org/#user35_bczbXDvqmG_15.py 
    
