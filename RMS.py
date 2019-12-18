import math
from math import gcd
import copy

# import matplotlib.pyplot as plot
# Will be from task parser: i is iteration
# set1 = {
#     "name": "t0",
#     "c": 1,
#     "p": 8,
#     "i": 0,
#     "active": False
# }
# set2 = {
#     "name": "t1",
#     "c": 2,
#     "p": 6,
#     "i": 0,
#     "active": False
# }
# set3 = {
#     "name": "t2",
#     "c": 4,
#     "p": 24,
#     "i": 0,
#     "active": False
# }
# task_set = [set1, set2, set3]

task_set = {

    0: {"name": "t0",
        "c": 1,
        "p": 8,
        "i": 0,
        "active": False},
    1: {"name": "t1",
        "c": 2,
        "p": 6,
        "i": 0,
        "active": False},
    2: {"name": "t2",
        "c": 4,
        "p": 24,
        "i": 0,
        "active": False}
}


def rms(task_set):
    if rms_utilization(task_set) is True:
        print("Schedulable under utilization test")
        exact_analysis(task_set)
        generate_schedule(task_set)

    else:
        print("Not schedulable under utilization test")
        if exact_analysis(task_set) is True:
            print("Schedulable under exact analysis")
        else:
            print("Not schedulable under exact analysis")


def rms_utilization(task_set):  # Sufficient, but not necessary
    total = 0
    n = len(task_set)
    for i in task_set.keys():
        total += task_set[i]['c'] / task_set[i]['p']
    exp = 2 ** float(1 / n)
    comp = float((n * (exp - 1)))
    if total <= comp:
        return True
    return False


def exact_analysis(task_set):
    sort_set = sorted(task_set.items(), key=lambda i: i[1]['p'], reverse=True)  # sort by period
    sort_set = dict(sort_set)
    for i in task_set.keys():
        dt = sort_set[i]['p']
        # to = sum(sort_set[i]['c'] for task in sort_set)
        to = sum(d['c'] for d in sort_set.values() if d)
        if inner_exact(to, sort_set, dt) is False:
            return False
        else:
            sort_set.pop(i)
        # Work around for last entry
        # dt = sort_set[i]['p']
        # # to = sum(task['c'] for task in task_set)
        # to = sum(d['c'] for d in sort_set.values() if d)
        # if inner_exact(to, task_set, dt) is False:
        #     return False
        # else:
        return True


# recursive method to get exact analysis
def inner_exact(t, task_set, dt):
    total = 0
    for i in task_set:
        total += task_set[i]['c'] * math.ceil(t / task_set[i]['p'])
    if total is t:
        if t <= dt:
            return True
        else:
            return False
    else:
        inner_exact(total, task_set, dt)


# sorted_set = copy.deepcopy(sorted(task_set, key=lambda i: i['p']))
original_set = copy.deepcopy(task_set)


def generate_schedule(task_set):
    lcms = lcm(task_set)
    for i in range(lcms):
        result = priority(task_set)
        if (result != -1):
            task_set[result]['c'] -= 1
            print(task_set[result]['name'])
        else:
            print("IDLE")

        for i in task_set.keys():
            task_set[i]['p'] -= 1
            if (task_set[i]['p'] == 0):
                task_set[i] = copy.deepcopy(original_set[i])
    return


def priority(set):
    temp = 9999999
    active = -1
    for i in task_set.keys():
        if (set[i]['c'] != 0):
            if (temp > set[i]['p'] or temp > original_set[i]['p']):
                temp = set[i]['p']
                active = i

    return active


def lcm(list_period):
    # lcm = list_period[0]['p']
    tmp = []
    for i in range(len(list_period)):
        tmp.append(list_period[i]['p'])
        lcms = list_period[0]['p']
    for i in tmp[1:]:
        lcms = lcms * i // gcd(lcms, i)
    return lcms


if __name__ == "__main__":
    rms(task_set)
