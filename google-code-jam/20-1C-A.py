import sys
import time
from time import strftime
import datetime
import itertools
import math

def read_int():
    return int(sys.stdin.readline()[:-1])

def read_2_ints():
    times = sys.stdin.readline().split(" ")
    return int(times[0]), int(times[1])

def read_2_int_1_str():
    sp = sys.stdin.readline().split(" ")
    return int(sp[0]), int(sp[1]), sp[2][:-1]

def read_N_strs(N):
    strs = []
    for i in range(N):
        strs.append(read_str()[::-1])
    return strs

def read_str():
    return sys.stdin.readline()[:-1]

def read_two_times_as_ints():
    times = sys.stdin.readline()[:-1].split(" ")
    t1 = time.strptime(times[0], "%H:%M")
    t2 = time.strptime(times[1], "%H:%M")
    t1 = t1.tm_min + t1.tm_hour*60
    t2 = t2.tm_min + t2.tm_hour*60
    return t1, t2

def print_ans(case_counter, ans):
    print("Case #{case}: {ans}".format(case=case_counter+1, ans=ans))

def print_ans_2(case_counter, ans1, ans2):
    print("Case #{case}: {ans1} {ans2}".format(case=case_counter+1, ans1=ans1, ans2=ans2))

def print_ans_3(case_counter, ans1, ans2, ans3):
    print("Case #{case}: {ans1} {ans2} {ans3}".format(case=case_counter+1, ans1=ans1, ans2=ans2, ans3=ans3))




def main():
    T = read_int()
    for case in range(T):
        N = read_int()
        print("Case #{case}:".format(case=case+1))
        if N < 502:
            under_502(N)
        else:
            above_502(N)

main()