#!/usr/bin/env python

import os
import csv

base_dir = os.path.join(os.curdir, 'data')

goals = {
    'snatch': 60,
    'cj': 85,
    'bsq': 150,
    'fsq': 100,
}

def get_weeks():
    return [d for d in os.listdir(base_dir)
            if os.path.isdir(os.path.join(base_dir, d))]

def get_days(week):
    return [d for d in os.listdir(os.path.join(base_dir, week))]

def print_day(week, day, file):
    print "{} day{}\n===============".format(week, day)
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0].strip()
            base = row[1].strip().lower()
            base_weight = goals[base] if base != 'x' else '?'
            print "\n",name
            for i in range(2, len(row)):
                # if it's a percentage)
                if i%2 == 0:
                    if row[i].lower() == 'x':
                        print "___",
                    else:
                        percentage = float(row[i]) / 100.0
                        print "{}kg".format(percentage * base_weight),
                else:
                    print row[i]
        print "\n"

if __name__ == "__main__":
    for week in get_weeks():
        i = 0
        for d in get_days(week):
            i += 1
            print_day(week, i, os.path.join(base_dir, week, d))
