// homework 2 for practicale programming
def resources_vs_time(upgrade_cost_increment, num_upgrade):
    """
    Build function that performs unit upgrades with specified cost increments
    """
    
    upg_value = 1
    speed = 1
    delta = upgrade_cost_increment
    cur_time = 0
    result = []
    value = 0
    for j in range(num_upgrade):
        cur_time = cur_time + upg_value/speed
        value += upg_value
        upg_value += delta
        speed +=1
        result.append((cur_time, value))
        
    return result

def test():
    """
    Testing code for resources_vs_time
    """
    #data1 = resources_vs_time(0.5, 20)
    #data2 = resources_vs_time(1.5, 10)
    data1 = resources_vs_time(0.0, 10)
    data2 = resources_vs_time(1.0, 10)
    print data1
    print data2
    #simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [data1, data2])

test()

'''
results:
[(1, 1), (1.5, 2.0), (1.83333333333, 3.0), (2.08333333333, 4.0), (2.28333333333, 5.0), (2.45, 6.0), (2.59285714286, 7.0), (2.71785714286, 8.0), (2.82896825397, 9.0), (2.92896825397, 10.0)]
[(1, 1), (2.0, 3.0), (3.0, 6.0), (4.0, 10.0), (5.0, 15.0), (6.0, 21.0), (7.0, 28.0), (8.0, 36.0), (9.0, 45.0), (10.0, 55.0)]
'''

Coockies game: http://www.codeskulptor.org/#user34_LfCJkBujSf_0.py

http://www.codeskulptor.org/#user34_LfCJkBujSf_60.py

10923464157.0,
75624738764.6,
0.664867401123,
7.3,
64

10000000000.0,
68975796834.2,
12439360714.3,
7.2,
63

Cursor : Cookies State(time,total,cookies,cps,history_len) 10000000000.0,153308849166.0,6965195661.5,16.1,152

Time: 10000000000.0
	  10923464157.0,
Current Cookies: 6965195661.5

CPS: 16.1
Total Cookies: 153308849166.0


simulate_clicker(
	BuildInfo(
		{'Cursor': [15.0, 0.10000000000000001]}, 1.15), 
		5000, <function strategy_none at 0xfe4ca1b0>) 
		
		expected Time: 5000.0 Current Cookies: 5000.0 CPS: 1.0 Total Cookies: 5000.0 History (length: 1): [(0.0, None, 0.0, 0.0)] 
		but received Cookies State(time,total,cookies,cps,history_len) 10000000000.0,10000000000.0,10000000000.0,1.0,1

[-17.8 pts] simulate_clicker(BuildInfo({'Cursor': [15.0, 0.10000000000000001]}, 1.15), 10, <function strategy_cursor at 0xfb1d71b0>) 
expected Time: 10.0 Current Cookies: 10.0 CPS: 1.0 Total Cookies: 10.0 History (length: 1): [(0.0, None, 0.0, 0.0)] 
but received Cookies State(time,total,cookies,cps,history_len) 15.0,15.0,0.0,1.1,2

[-17.8 pts] simulate_clicker(BuildInfo({'Cursor': [15.0, 0.10000000000000001]}, 1.15), 10, <function strategy_cursor at 0xfaaa8db0>) 
expected Time: 10.0 Current Cookies: 10.0 CPS: 1.0 Total Cookies: 10.0 History (length: 1): [(0.0, None, 0.0, 0.0)] 
but received Cookies State(time,total,cookies,cps,history_len) 15.0,15.0,0.0,1.1,2


simulate_clicker(BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), 16, <function strategy_cursor at 0xfbcb46f0>) 
expected Time: 16.0 Current Cookies: 13.9125 CPS: 151.0 Total Cookies: 66.0 History (length: 4): [(0.0, None, 0.0, 0.0), (15.0, 'Cursor', 15.0, 15.0), ..., (16.0, 'Cursor', 19.837499999999999, 66.0)] 
but received Cookies State(time,total,cookies,cps,history_len) 16.0,66.0,33.75,101.0,3