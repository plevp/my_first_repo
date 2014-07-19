http://www.codeskulptor.org/#user34_LfCJkBujSf_96.py

"""
Cookie Clicker Simulator
"""

import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided
import math

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total = 0.0
        self._coockies = 0.0
        self._current_time = 0.0
        self._cps = 1.0
        self._history = [];
        self._history.append((self._current_time, None,  0.0, self._coockies))
        
    def __str__(self):
        """
        Return human readable state
        """
        return "Cookies State(time,total,cookies,cps,history_len) " + \
        str(self._current_time) + "," + str(self._total) + ","  + str(self._coockies) + ","  + str(self._cps) + ","  + \
        str(len(self._history))
                                                                          
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._coockies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history
        
    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if (self._coockies >= cookies):
            return 0.0
        else:
            #print (cookies - self._coockies) / self._cps
            #print math.ceil((cookies - self._coockies) / self._cps)
            return math.ceil((cookies - self._coockies) / self._cps)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if (time > 0):
            new = time * self._cps
            self._total +=  new
            self._coockies += new
            self._current_time += time 
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if (cost <= self._coockies):
            self._coockies -= cost
            self._cps += additional_cps
            self._history.append((round(self._current_time), item_name, cost, self._total))
   
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    1. Check the current time and break out of the loop 
                if the duration has been passed.
    2. Call the strategy function with the appropriate arguments 
       to determine which item to purchase next. 
       If the strategy function returns None, 
       you should break out of the loop, 
       as that means no more items will be purchased.
    3. Determine how much time must elapse until it is possible 
        to purchase the item. If you would have to wait past the 
        duration of the simulation to purchase the item, 
        you should end the simulation.
    4. Wait until that time.
    5. Buy the item.
    6.Update the build information.
    """

    # Replace with your code
    b_i = build_info.clone()
    c_s = ClickerState()
    
    while (c_s.get_time() <= duration ):
        next_item = strategy(c_s.get_cookies(), c_s.get_cps(), 
                            duration - c_s.get_time(), b_i)
        if next_item == None or \
            ( c_s.get_cookies() + (duration - c_s.get_time()) * c_s.get_cps()) < \
            b_i.get_cost(next_item):
            c_s.wait(duration - c_s.get_time())
            break
        next_cost = b_i.get_cost(next_item)
        n_time = c_s.time_until(next_cost)
        #print "next ", next_cost, n_time
        if (c_s.get_time() + n_time) > duration:
            c_s.wait(duration - c_s.get_time())
            break;
        c_s.wait(n_time)
        #print "status before buy:", c_s
        c_s.buy_item(next_item, next_cost, b_i.get_cps(next_item))
        #print "status after buy:", c_s
        b_i.update_item(next_item)
        #print "status:", c_s
    
    #print c_s
    return c_s        

def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    
    if (cookies + time_left * cps) >= build_info.get_cost("Cursor"):
        return "Cursor"
    else:
        return None
    """
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    return the cheapest item
    """
    items = build_info.build_items()
    
    min_item = reduce(lambda x,y: x if y == None or build_info.get_cost(x) < build_info.get_cost(y) else y,\
        items)	
    #print min_item, build_info.get_cost(min_item)
    if (cookies + time_left * cps) >= build_info.get_cost(min_item):
        return min_item
    else:
        return None

def strategy_expensive(cookies, cps, time_left, build_info):    
    """
    return the most expensive item
    """   
    items = build_info.build_items()
   
    sorted_items = sorted(items, key = lambda x: build_info.get_cost(x), reverse = True)
    for item in sorted_items:
        if (cookies + time_left * cps) >= build_info.get_cost(item):
            #print item;
            return item
    
    return None

def strategy_best(cookies, cps, time_left, build_info):
    """
    return the item the bigest value
    """   

    items = build_info.build_items()
   
    sorted_items = sorted(items, key = lambda x: build_info.get_cps(x)/ build_info.get_cost(x), reverse = True)
    #print sorted_items
    for item in sorted_items:
        if (cookies + time_left * cps) >= build_info.get_cost(item):
            #print item;
            return item
    
    return None 
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)

    
run()

#x = simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), 16, strategy_cursor)
#print x
#print x.get_history()
