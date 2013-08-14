#!/usr/bin/env python

import os

base_dir = os.path.join(os.curdir, 'data')

def get_weeks():
    return [d for d in os.listdir(base_dir)
            if os.path.isdir(os.path.join(base_dir, d))]

def get_days(week):
    return [d for d in os.listdir(os.path.join(base_dir, week))]

if __name__ == "__main__":
    for week in get_weeks():
        print get_days(week)
