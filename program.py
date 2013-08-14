#!/usr/bin/env python

import os

base_dir = os.path.join(os.curdir, 'data')

goals = {
    'Snatch': 60,
    'CJ': 85,
    'BSQ': 150,
    'FSQ': 100,
}

def get_weeks():
    return [d for d in os.listdir(base_dir)
            if os.path.isdir(os.path.join(base_dir, d))]

def get_days(week):
    return [os.path.join(base_dir, week, d) for d in os.listdir(os.path.join(base_dir, week))]

def print_day(d):
    with open(d) as f:
        dat = f.read()
    print dat

if __name__ == "__main__":
    for week in get_weeks():
        for d in get_days(week):
            print_day(d)
