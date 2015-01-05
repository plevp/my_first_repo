##################################################################
#### Simchamp
#### This code has some general concepts of lift defined using the lift object
#### EFFICIENT ALLOCATION OF LIFTS
####
####
##################################################################
import numpy as np
from matplotlib import pyplot as plt
import pygame as pg

def time(pplwt, done, floor, dist):
    """

    Time function not used in this code.
    """

def maximum(a):
    '''
    max(a) gives an error if a is empty. hence this work around is used
    '''
    if len(a): return max(a)
    return 0

def minimum(a):
    '''
    min(a) gives an error if a is empty. hence this work around is used
    '''
    if len(a): return min(a)
    return 20

def check_lift(lifts, flr_list):
    '''
    This function is used as a precautionary measure. It comes into play when
    the number of people using the lift is very high which causes some people
    who have been assigned a lift to be left outside the already filled lift.
    '''
    mov = False
    for lift in lifts:
        if lift.dest or lift.pick_up:
            mov = True
            break
    if (not mov) and len(flr_list):
        for lift in lifts:
            for flr in flr_list:
                if flr not in lift.pick_up: lift.pick_up.append(flr)

def dispatch(disp_from, disp_to, lifts, d_lift, done):
    '''
    This will be the intelligent function that will be used in the next part
    to optimise the wait time by proper allocation of lifts.
    '''
    i = 0
    for fr, to in np.c_[disp_from, disp_to]:
        time = 14000
        for lift in lifts:
            if len(lift.dest)==0 and len(lift.pick_up)==0:
                if fr != lift.pos: lift.go_up = np.sign(fr-lift.pos)
            if lift.pos > fr and lift.go_up==1:
                k = 2*max(maximum(lift.dest), maximum(lift.pick_up)) - lift.pos - fr
            elif lift.pos < fr and lift.go_up==-1:
                k = lift.pos + fr - 2*min(minimum(lift.dest), minimum(lift.pick_up))
            else: k = abs(fr - lift.pos)
            T = (len(lift.dest) + 0.5*len(lift.pick_up)) + k
            if time > T:
                time = T
                l = lift
        d_lift[i+done] = l
        i+=1
        l.pick_up.append(fr)

class Person(object):
    '''
    Person object
    Used in storing the time spent inside the lift
    '''
    def __init__(self):
        self.transit_time = 0


class Lift(object):
    '''
    Lift object
    The number of instances of this objects will be the number of lifts in the building
    Some points to note -
    len(lift.dest) gives the number of people inside the lift
    Both load and unload methods increase the waiting time.
    Waiting time if positive decrease (by 5 for now) after each time interval(iteration)
    Each cycle the following steps will take place for every lift -
    - unload, load, begin to move once waiting is over...
    '''
    def __init__(self):
        '''
        each lift initialised with the following attributes
        '''
        self.pos = 0        # position of the lift (floor) but we can make it decimal too for simuation when lift moves from one floor to another
        self.dest = []      # destination of the people inside the lift
        self.wait = 0       # Time for which the lift is stationary. Is positive during loading and unloading of the lift
        self.pick_up = []   # The floors at which the lift is requested by those who want to use the lift
        self.go_up = 1      # Current motion of the lift
        self.persons = []   # Person objects inside the lift

    def unload(self):
        '''
        Exiting of people in that particular elevator
        It also clears its
        '''
        # remove lifts current floor from pick_up array
        while self.pos in self.pick_up:
            self.pick_up.remove(self.pos)
        # remove the people who have reached their destination
        while self.pos in self.dest:
            self.wait += np.random.poisson(3)
            self.dest.remove(self.pos)
        # update the persons in the lift, remove those who have reached
        temp = []
        for person in self.persons:
            if person.dest != self.pos:
                temp.append(person)
            else:
                person.dest = -1
        self.persons = temp

    def load(self, dest, persons):
        '''
        Entering of people in that particular elevator
        '''
        # add persons to the lift
        self.persons.extend(persons)
        # store each person's destination so that the person is removed at its destination
        for i, person in enumerate(persons):
            person.dest = dest[i]
        # remove lifts current floor from pick_up array
        while self.pos in self.pick_up:
            self.pick_up.remove(self.pos)
        # add their destinations to the lifts destination
        self.dest.extend(dest)
        self.wait += np.random.poisson(3, len(dest)).sum()

    def update_pos(self):
        '''
        Update the postion of the lift
        '''
        for person in self.persons:     # increase transit time
            person.transit_time += t
        if self.wait > 0:               # wait till passengers are aboard
            self.wait -= t
        else:
            self.wait = 0
            if self.dest or self.pick_up:
                self.move()             # move the lift or wait in its postion.

    def move(self):
        '''
        Move the lift
        '''
        # change lifts direction if it reaches ground or highest destination
        if self.go_up == 1:
            if max(maximum(self.dest), maximum(self.pick_up)) <= self.pos: self.go_up = -1
        else:
            if self.pos == 0: self.go_up = 1
        self.pos += self.go_up*1
t = 5
def main(PPL = 5500, NO_OF_LIFTS = 4, FPS = 30, screen = None):
    #PPL = 500                       # number of people using the lift
    #t = 5                           # number of seconds passed in each iteration
    m_hr_range = 3                  # assuming people enter office from 7 am to 10 am
    e_hr_range = 3                  # assuming people leave office between 4 pm and 7 pm
    l_hr_range = 3                  # time during which people will have lunch
    #NO_OF_LIFTS = 4
    m_size_t = int(m_hr_range*60*60/t)  # Sample the time into packets of t seconds
    l_size_t = int(l_hr_range*60*60/t)  # sample the time during lunch
    e_size_t = int(e_hr_range*60*60/t)  # sample the time during lunch
    SIMULATE = True

    if SIMULATE:
        black = ( 0, 0, 0)                              # define colors
        white = ( 255, 255, 255)
        green = ( 0, 255, 0)
        red = ( 255, 0, 0)
        if not screen:
            pg.init()                                       # initialise pygame
            pg.mixer.quit()  # LP
            #FPS = 100                                    # frames per second in our simulation
            size=[700,500]                                  # size of screen
            if not screen: screen=pg.display.set_mode(size)
            #pg.display.set_caption("Elevator Simulation")
        myfont = pg.font.SysFont("Comic Sans MS", 30)
        clock=pg.time.Clock()
        rect_x_l = np.linspace(0, 400, NO_OF_LIFTS)     # used in drawing lifts
        rect_y = 50

    # generating the floor distribution and eating preferance of the office goers
    flr = np.array([0,0.06,0.12,0.10,0.29,0.20,0.13,0.04,0.06])     # floor distribution
    flr = flr.cumsum()
    floor = np.ones(PPL)                                # each index will correspond to that person's floor
    eat = np.ones(PPL)                                  # each index will correspond to the person's lunch place
    for i in range(len(flr)-1):
        floor[PPL*flr[i]:PPL*flr[i+1]] = i+1            # assign floors
        eat[PPL*flr[i]:PPL*(flr[i]+0.3*(flr[i+1]-flr[i]))] = 0  # assign eating preference

    data = np.r_['1,2,0', floor, eat]

    # following will generate the person's schedule
    # arrival
    mor = np.random.normal(loc = m_hr_range/2, scale = m_hr_range/2, size = PPL*2)   # size is slightly more than number of people coz some values given by the distribution will be invalid
    mor = mor[np.where((0<mor) & (mor<m_hr_range))][:PPL]
    np.random.shuffle(mor)

    # people leave for lunch strictly between 11 and 1 and return before 2
    lun = np.random.normal(loc = l_hr_range/3, scale = l_hr_range/3, size = PPL*2)   # size is slightly more than number of people coz some values given by the distribution will be invalid
    lun = lun[np.where((0<lun) & (lun<l_hr_range*2/3))][:PPL]
    np.random.shuffle(lun)
    # assuming people return after 30 minutes on an average
    lun_ret = lun + np.random.poisson(30, size = PPL)/60.0/3.0

    eve = np.random.normal(loc = e_hr_range/2, scale = e_hr_range/2, size = PPL*2)   # size is slightly more than number of people coz some values given by the distribution will be invalid
    eve = eve[np.where((0<eve) & (eve<e_hr_range))][:PPL]
    np.random.shuffle(eve)

    np.random.shuffle(data)    # shuffling the floors for randomness

    data = np.r_['1,2,0', data, mor, lun, lun_ret, eve]

    mor_data = data[data[:,2].argsort()]
    lun_data = data[data[:,3].argsort()]
    jj = np.where((lun_data[:,0]==1)&(lun_data[:,1]==1))
    lun_data = np.r_['1,2,0', np.delete(lun_data[:,0], jj[0]), np.delete(lun_data[:,1], jj[0]), np.delete(lun_data[:,2], jj[0]), np.delete(lun_data[:,3], jj[0]), np.delete(lun_data[:,4], jj[0]), np.delete(lun_data[:,5], jj[0])]
    #return lun_data
    ret_lun_data = data[data[:,4].argsort()]
    jj = np.where((ret_lun_data[:,0]==1)&(ret_lun_data[:,1]==1))
    ret_lun_data = np.r_['1,2,0', np.delete(ret_lun_data[:,0], jj[0]), np.delete(ret_lun_data[:,1], jj[0]), np.delete(ret_lun_data[:,2], jj[0]), np.delete(ret_lun_data[:,3], jj[0]), np.delete(ret_lun_data[:,4], jj[0]), np.delete(ret_lun_data[:,5], jj[0])]
    eve_data = data[data[:,5].argsort()]

    lifts = np.array([Lift() for i in range(NO_OF_LIFTS)], dtype=object)    # initialise the lifts.
    persons = np.array([Person() for i in range(4*PPL)], dtype=object)      # initialise persons to store transit times


    # generates an array of length equal to the number of iterations where each iteration stores the number of ppl entering the simulation
    mor_ppl = np.histogram(mor_data[:,2], bins = np.linspace(0, m_hr_range, m_size_t+1))[0]
    lun_ppl = np.histogram(lun_data[:,3], bins = np.linspace(0, l_hr_range, l_size_t+1))[0]
    ret_ppl = np.histogram(ret_lun_data[:,4], bins = np.linspace(0, l_hr_range, l_size_t+1))[0]
    eve_ppl = np.histogram(eve_data[:,3], bins = np.linspace(0, e_hr_range, e_size_t+1))[0]

    pplwt = 0
    done = 0
    retwt = 0
    retdone = 0
    flr_list = []

    mor_wait_time = np.zeros(PPL)       # time a person waits
    lun_wait_time = np.zeros(lun_data.size/6)
    ret_wait_time = np.zeros(lun_data.size/6)
    eve_wait_time = np.zeros(PPL)

    ground_floor = np.zeros(PPL)        # will be used as ground floor during morning and evening loops

    # begin simulation of morning hours
    mor_disp_done = 0
    mor_to_disp = 0
    mor_d_lift = np.array([Lift() for i in range(PPL)], dtype=object)
    mor_data1 = mor_data[:,0]

    print len(mor_ppl), type(mor_ppl)
    for ppl in mor_ppl:
        if SIMULATE:
            for event in pg.event.get(): # User did something
                if event.type == pg.QUIT: # If user clicked close
                    SIMULATE = False
                    pg.quit()

        pplwt += ppl                        # ppl enter simulation environment
        mor_to_disp = ppl                   # each of them will be fed to the dispatch algorithm
        # get_data for dispatching
        mor_disp_from, mor_disp_to = mor_data[mor_disp_done:mor_disp_done+mor_to_disp,0], ground_floor[mor_disp_done:mor_disp_done+mor_to_disp]
        for lift in lifts:                  # all lifts must return back to ground floor
            if 0 not in lift.pick_up: lift.pick_up.append(0)
        if mor_disp_from.size:              # use dispatching algorithm to assign an elevator
            dispatch(mor_disp_from, mor_disp_to, lifts, mor_d_lift, mor_disp_done)
            mor_disp_done += mor_to_disp
        # get data on those who are waiting
        flr_waiting, dest_waiting = ground_floor[done:done+pplwt], mor_data1[:pplwt]
        if SIMULATE:
            screen.fill(black)
            for lift, rect_x in np.c_[lifts, rect_x_l]:
                pg.draw.rect(screen,white,[30+rect_x, 500-rect_y*(1+lift.pos),30,30])
                for i,per in enumerate(lift.persons):
                    pg.draw.line(screen, red, (30+rect_x+i*5 , 500-rect_y*(1+lift.pos)+15), (30+rect_x+i*5 , 500-rect_y*(1+lift.pos)+30), 2)
            flr_list = flr_waiting.tolist()
            for flr in range(0,9):
                for i in range(flr_list.count(flr)+flr_list.count([flr])):
                    pg.draw.line(screen, red, (i*5 , 500-rect_y*(1+flr)+15), (i*5 , 500-rect_y*(1+flr)+30), 2)
            label = myfont.render("Morning", 1, white)
            screen.blit(label, (550, 100))
            clock.tick(FPS)
            pg.display.flip()
        if not pplwt:
            for lift in lifts:              # if no person is waiting, continue lift's normal operation
                lift.unload()
                lift.update_pos()
            if SIMULATE:
                clock.tick(FPS)
                pg.display.flip()
            continue
        mor_lifts = mor_d_lift[done:done+pplwt]
        jj = []
        # for each lift, unload those who reached,
        # load with those who are on that floor and are assigned that lift
        # update position and move
        for lift in lifts:
            lift.unload()
            # get those who are on the lift's floor and who have been assigned that lift
            kk = np.where((flr_waiting == lift.pos)&(mor_lifts == lift))
            if kk[0].size == 0:
                lift.update_pos()
                continue
            cap = 8 - len(lift.dest)
            lift.load(dest_waiting[kk[0][:cap]], persons[done:done+len(kk[0][:cap])])
            pplwt -= len(kk[0][:cap])
            done += len(kk[0][:cap])
            jj.append([kk, cap])
            lift.update_pos()
        for kk, c in jj:         # update waiting data
            flr_waiting = np.delete(flr_waiting, kk[0][:c])
            mor_lifts = np.delete(mor_lifts, kk[0][:c])
            dest_waiting = np.delete(dest_waiting, kk[0][:c])
        if pplwt:
            for lift in lifts:
                lift.pick_up.extend(flr_waiting)
        check_lift(lifts, flr_list)
        mor_wait_time[done:done+pplwt] += t     # increase waiting time of those who havent boarded

    # begin simulation of lunch hours
    pplwt, done = 0, 0
    lun_disp_done, lun_to_disp = 0, 0
    ret_disp_done, ret_to_disp = 0, 0
    lun_d_lift = np.array([Lift() for i in range(lun_data.size/6)], dtype=object)
    ret_d_lift = np.array([Lift() for i in range(lun_data.size/6)], dtype=object)
    lun_data1, lun_data2 = lun_data[:,0], lun_data[:,1]
    ret_data1, ret_data2 = lun_data[:,1], lun_data[:,0]

    for ppl, ret in np.c_[lun_ppl, ret_ppl]:
        if SIMULATE:
            for event in pg.event.get(): # User did something
                if event.type == pg.QUIT: # If user clicked close
                    SIMULATE = False
                    pg.quit()
        if SIMULATE:
            screen.fill(black)
            for lift, rect_x in np.c_[lifts, rect_x_l]:
                pg.draw.rect(screen,white,[30+rect_x, 500-rect_y*(1+lift.pos),30,30])
                for i,per in enumerate(lift.persons):
                    pg.draw.line(screen, red, (30+rect_x+i*5 , 500-rect_y*(1+lift.pos)+15), (30+rect_x+i*5 , 500-rect_y*(1+lift.pos)+30), 2)

        pplwt += ppl
        retwt += ret
        lun_to_disp = ppl
        ret_to_disp = ret
        lun_disp_from, lun_disp_to = np.hsplit(lun_data[lun_disp_done:lun_disp_done+lun_to_disp,0:2], 2)
        ret_disp_to, ret_disp_from = np.hsplit(ret_lun_data[ret_disp_done:ret_disp_done+ret_to_disp,0:2], 2)
        if lun_disp_from.size > 1: lun_disp_from, lun_disp_to = np.squeeze(lun_disp_from), np.squeeze(lun_disp_to)
        if ret_disp_from.size > 1: ret_disp_from, ret_disp_to = np.squeeze(ret_disp_from), np.squeeze(ret_disp_to)
        if lun_disp_from.size:
            dispatch(lun_disp_from, lun_disp_to, lifts, lun_d_lift, lun_disp_done)
            lun_disp_done += lun_to_disp
        if ret_disp_from.size:
            dispatch(ret_disp_from, ret_disp_to, lifts, ret_d_lift, ret_disp_done)
            ret_disp_done += ret_to_disp
        flr_waiting, dest_waiting = lun_data1[:pplwt], lun_data2[:pplwt]
        ret_flr_waiting, ret_dest_waiting = ret_data1[:retwt], ret_data2[:retwt]
        if SIMULATE:
            flr_list = flr_waiting.tolist()
            flr_list.extend(ret_flr_waiting.tolist())
            for flr in range(0,9):
                for i in range(flr_list.count(flr)):
                    pg.draw.line(screen, red, (i*5 , 500-rect_y*(1+flr)+15), (i*5 , 500-rect_y*(1+flr)+30), 2)
            label = myfont.render("Lunch", 1, white)
            screen.blit(label, (550, 100))
            clock.tick(FPS)
            pg.display.flip()
        if not (pplwt or retwt):
            for lift in lifts:
                lift.unload()
                lift.update_pos()
            if SIMULATE:
                clock.tick(FPS)
                pg.display.flip()
            continue
        lun_lifts = lun_d_lift[done:done+pplwt]
        ret_lifts = ret_d_lift[retdone:retdone+retwt]
        jj, retjj = [], []
        for lift in lifts:
            lift.unload()
            kk = np.where((flr_waiting == lift.pos)&(lun_lifts == lift))
            retkk = np.where((ret_flr_waiting==lift.pos)&(ret_lifts == lift))
            if kk[0].size == 0 and retkk[0].size == 0:
                lift.update_pos()
                continue
            if kk[0].size:
                cap = 8 - len(lift.dest)
                lift.load(dest_waiting[kk[0][:cap]], persons[1*PPL+done:1*PPL+done+len(kk[0][:cap])])
                pplwt -= len(kk[0][:cap])
                done += len(kk[0][:cap])
                jj.append([kk, cap])
            if retkk[0].size:
                cap = 8 - len(lift.dest)
                lift.load(ret_dest_waiting[retkk[0][:cap]], persons[2*PPL+retdone:2*PPL+retdone+len(retkk[0][:cap])])
                retwt -= len(retkk[0][:cap])
                retdone += len(retkk[0][:cap])
                retjj.append([retkk, cap])
            lift.update_pos()
        for kk, c in jj:
            flr_waiting = np.delete(flr_waiting, kk[0][:c])
            lun_lifts = np.delete(lun_lifts, kk[0][:c])
            dest_waiting = np.delete(dest_waiting, kk[0][:c])
        for retkk, c in retjj:
            ret_flr_waiting = np.delete(ret_flr_waiting, retkk[0][:c])
            ret_lifts = np.delete(ret_lifts, retkk[0][:c])
            ret_dest_waiting = np.delete(ret_dest_waiting, retkk[0][:c])
        if pplwt:
            for lift in lifts:
                lift.pick_up.extend(flr_waiting)
                lift.pick_up.extend(ret_flr_waiting)
        check_lift(lifts, flr_list)
        lun_wait_time[done:done+pplwt] += t
        ret_wait_time[retdone:retdone+retwt] += t

    pplwt, done = 0, 0
    eve_disp_done = 0
    eve_to_disp = 0
    eve_d_lift = np.array([Lift() for i in range(PPL)], dtype=object)
    eve_data1 = eve_data[:,0]
    for ppl in eve_ppl:
        if SIMULATE:
            for event in pg.event.get(): # User did something
                if event.type == pg.QUIT: # If user clicked close
                    SIMULATE = False
                    pg.quit()

        pplwt += ppl
        eve_to_disp = ppl
        eve_disp_from, eve_disp_to = eve_data[eve_disp_done:eve_disp_done+eve_to_disp,0], ground_floor[eve_disp_done:eve_disp_done+eve_to_disp]
        if eve_disp_from.size:
            dispatch(eve_disp_from, eve_disp_to, lifts, eve_d_lift, eve_disp_done)
            eve_disp_done += eve_to_disp

        if SIMULATE:
            screen.fill(black)
            for lift, rect_x in np.c_[lifts, rect_x_l]:
                pg.draw.rect(screen,white,[30+rect_x, 500-rect_y*(1+lift.pos),30,30])
                for i,per in enumerate(lift.persons):
                    pg.draw.line(screen, red, (30+rect_x+i*5 , 500-rect_y*(1+lift.pos)+15), (30+rect_x+i*5 , 500-rect_y*(1+lift.pos)+30), 2)
            flr_list = flr_waiting.tolist()
            for flr in range(0,9):
                for i in range(flr_list.count(flr)+flr_list.count([flr])):
                    pg.draw.line(screen, red, (i*5 , 500-rect_y*(1+flr)+15), (i*5 , 500-rect_y*(1+flr)+30), 2)
            label = myfont.render("Evening", 1, white)
            screen.blit(label, (550, 100))
            clock.tick(FPS)
            pg.display.flip()
        if not pplwt:
            for lift in lifts:
                lift.unload()
                lift.update_pos()
            if SIMULATE:
                    clock.tick(FPS)
                    pg.display.flip()
            continue
        flr_waiting, dest_waiting = eve_data1[:pplwt], ground_floor[done:done+pplwt]
        eve_lifts = eve_d_lift[done:done+pplwt]
        jj = []
        for lift in lifts:
            lift.unload()
            kk = np.where((flr_waiting == lift.pos)&(eve_lifts == lift))
            if kk[0].size == 0:
                lift.update_pos()
                continue
            cap = 8 - len(lift.dest)
            lift.load(dest_waiting[kk[0][:cap]], persons[3*PPL+done:3*PPL+done+len(kk[0][:cap])])
            pplwt -= len(kk[0][:cap])
            done += len(kk[0][:cap])
            jj.append([kk, cap])
            lift.update_pos()
        for kk, c in jj:
            flr_waiting = np.delete(flr_waiting, kk[0][:c])
            eve_lifts = np.delete(eve_lifts, kk[0][:c])
            dest_waiting = np.delete(dest_waiting, kk[0][:c])
        if pplwt:
            for lift in lifts:
                lift.pick_up.extend(flr_waiting)
        check_lift(lifts, flr_list)
        eve_wait_time[done:done+pplwt] += t

    if SIMULATE:
        pg.quit()
    mor_transit_time = np.array([person.transit_time for person in persons[0*PPL:1*PPL]])
    lun_transit_time = np.array([person.transit_time for person in persons[1*PPL:1*PPL+lun_data.size/6]])
    ret_transit_time = np.array([person.transit_time for person in persons[2*PPL:2*PPL+lun_data.size/6]])
    eve_transit_time = np.array([person.transit_time for person in persons[3*PPL:4*PPL]])

    return np.average(mor_wait_time),np.average(mor_transit_time),np.average(lun_wait_time),np.average(lun_transit_time),np.average(ret_wait_time),np.average(ret_transit_time),np.average(eve_wait_time),np.average(eve_transit_time)
    #return mor_wait_time,mor_transit_time,lun_wait_time,lun_transit_time,ret_wait_time,ret_transit_time,eve_wait_time,eve_transit_time

#for single cases and to see simulation


if __name__ == '__main__':
    returned_data = main(PPL = 1000, NO_OF_LIFTS = 6)


#for the graphs and to consider all the cases

morning = []
morning_transit = []
lunch = []
lunch_transit = []
lunch_return = []
lunch_return_transit = []
leave = []
leave_transit = []

for j in range(1,4):
    for i in range(1, 4):
        if __name__ == '__main__':
            returned_data = main(PPL = 1200, NO_OF_LIFTS = 6)
            morning.append(returned_data[0])
            morning_transit.append(returned_data[1])
            lunch.append(returned_data[2])
            lunch_transit.append(returned_data[3])
            lunch_return.append(returned_data[4])
            lunch_return_transit.append(returned_data[5])
            leave.append(returned_data[6])
            leave_transit.append(returned_data[7])
            #print i,j
print np.average(morning),np.average(morning_transit),np.average(lunch),np.average(lunch_transit),np.average(lunch_return),np.average(lunch_return_transit),np.average(leave),np.average(leave_transit)
'''
morning = np.reshape(np.asarray(morning),(6,-1))
morning_transit = np.reshape(np.asarray(morning_transit),(6,-1))

lunch = np.reshape(np.asarray(lunch),(6,-1))
lunch_transit = np.reshape(np.asarray(lunch_transit),(6,-1))

lunch_return = np.reshape(np.asarray(lunch_return),(6,-1))
lunch_return_transit = np.reshape(np.asarray(lunch_return_transit),(6,-1))

leave = np.reshape(np.asarray(leave),(6,-1))
leave_transit = np.reshape(np.asarray(leave_transit),(6,-1))

morning_total = morning + morning_transit
lunch_total = lunch + lunch_transit
lunch_return_total = lunch_return + lunch_return_transit
leave_total = leave + leave_transit

total_time = morning_total + lunch_total + lunch_return_total + leave_total
''''''
for i in range(6):
    plt.figure(1)
    plt.plot(range(50,1250,50),morning[i])
    plt.figure(2)
    plt.plot(range(50,1250,50),morning_transit[i])
    plt.figure(3)
    plt.plot(range(50,1250,50),lunch[i])
    plt.figure(4)
    plt.plot(range(50,1250,50),lunch_transit[i])
    plt.figure(5)
    plt.plot(range(50,1250,50),lunch_return[i])
    plt.figure(6)
    plt.plot(range(50,1250,50),lunch_return_transit[i])
    plt.figure(7)
    plt.plot(range(50,1250,50),leave[i])
    plt.figure(8)
    plt.plot(range(50,1250,50),leave_transit[i])
    plt.figure(9)
    plt.plot(range(50,1250,50),morning_total[i])
    plt.figure(10)
    plt.plot(range(50,1250,50),lunch_total[i])
    plt.figure(11)
    plt.plot(range(50,1250,50),lunch_return_total[i])
    plt.figure(12)
    plt.plot(range(50,1250,50),leave_total[i])
    plt.figure(13)
    plt.plot(range(50,1250,50),total_time[i])
    plt.legend(['1','2','3','4','5','6'])
'''
