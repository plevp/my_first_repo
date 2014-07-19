#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

class Country:
    def __init__(self, country, br):
        self.name = country
        self.brackets = br;
        
    def __str__(self):
        return self.name

    def doit(self, salary):
        tax = 0.0;
        d0 = 0.0

        for (d, p)  in self.brackets:
            if d == -1:
                tax += ((salary - d0) * p)/100
                break;
            elif salary > d: 
                tax += ((d - d0) * p)/100
                d0 = d
                #print tax
            else:
                tax += ((salary - d0) * p)/100
                #print tax
                break;
        return tax;
        

def do_it(input_data, salary):
    lines = input_data.split('\n')
    countries = [];
    items = []
    
    c = ""
    for line  in lines:
        l = line.strip();
        if len(l) > 0:
            if l[0].isalpha():
                if len(c) > 0 and len(items) > 0:
                   countries.append(Country(c, list(items)));
                items = [];
                c = l;
            else:
                parts = line.split()
                items.append((float(parts[0]), float(parts[1])))
                
    if len(c) > 0 and len(items) > 0:
        countries.append(Country(c, list(items)));

    for c in countries:
        #c = Country("Israel", items);
        t = c.doit(salary)
        print "%s: Salary: %d, Tax: %0.1f, Percent: %0.2f" % (c.name, salary, t, t/salary * 100)

    
if __name__ == '__main__':
    if len(sys.argv) > 2:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        do_it(input_data, float(sys.argv[2].strip()))
    else:
        print 'This test requires an input file and salary.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

