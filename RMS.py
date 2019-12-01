import math
from math import gcd
import copy
# import matplotlib.pyplot as plot
# Will be from task parser: i is iteration
set1 = {
    "name": "t0",
    "c": 1,
    "p": 8,
    "i": 0,
    "active": False
}
set2 = {
    "name": "t1",
    "c": 2,
    "p": 6,
    "i": 0,
    "active": False
}
set3 = {
    "name": "t2",
    "c": 4,
    "p": 24,
    "i": 0,
    "active": False
}
task_set = [set1, set2, set3]


def rms(task_set):
    if rms_utilization(task_set) is True:
        print("Schedulable under utilization test")
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
    for task in task_set:
        total += task['c'] / task['p']
    exp = 2 ** float(1 / n)
    comp = float((n * (exp - 1)))
    if total <= comp:
        return True
    return False


def exact_analysis(task_set):
    task_set = sorted(task_set, key=lambda i: i['p'], reverse=True)  # sort by period
    for task in task_set:
        dt = task['p']
        to = sum(task['c'] for task in task_set)
        if inner_exact(to, task_set, dt) is False:
            return False
        else:
            task_set.pop(0)
    # Work around for last entry
    dt = task['p']
    to = sum(task['c'] for task in task_set)
    if inner_exact(to, task_set, dt) is False:
        return False
    else:
        return True


# recursive method to get exact analysis
def inner_exact(t, task_set, dt):
    total = 0
    for task in task_set:
        total += task['c'] * math.ceil(t / task['p'])
    if total is t:
        if t <= dt:
            return True
        else:
            return False
    else:
        inner_exact(total, task_set, dt)


def generate_schedule(task_set):
    lcms = lcm(task_set)

    sorted_set = copy.deepcopy(sorted(task_set, key=lambda i: i['p']))
    for task in sorted_set:  # Initialize p for first instance in same order
        task['p'] = 0

    #fluid_set = task_set
    flow = []
    for t in range(lcms):
        tn = priority(sorted_set, t)

        #test = next(task for task in sorted_set if task["name"] == tn)
        if tn in '':
            print("IDLE")
        else:
            task = next(task for task in sorted_set if task["name"] == tn)
            task['c'] -= 1
            if task['c'] == 0:
                tmp = next(task for task in sorted_set if task["name"] == tn)
                i = tmp['i']
                sorted_set.remove(next(task for task in sorted_set if task["name"] == tn))
                nextiter = next(task for task in copy.deepcopy(task_set) if task["name"] == tn)

                nextiter['i'] = i + 1
                nextiter['p'] = nextiter['p']*nextiter['i']
                nextiter["active"] = False
                sorted_set.append(nextiter)
            flow.append({"name": tn})  # , "start": t, "end": t + 1
        print(tn)

    print("here")
    ###
    """
    fig, gnt = plot.subplots()
    gnt.set_xlim(0, lcms)
    gnt.set_ylim(0, len(task_set))
    plot.show()
    """


def priority(task_sets, t):
    tmpP = 999
    active_task = ""
    for task in task_sets:
        if task['p'] == t:
            active_task = task['name']
            task["active"] = True
            return active_task
        elif task['p'] < tmpP or task['p'] == t or task["active"] is True:
            tmpP = task['p']
            #task["active"] = True
            active_task = task['name']

    if active_task != '':
        task = next(task for task in task_sets if task["name"] == active_task)
        task["active"] = True

    return active_task


def lcm(list_period):
    lcm = list_period[0]['p']
    for i in list_period[1:]:
        i = i['p']
        lcm = lcm * i // gcd(lcm, i)
    return lcm


if __name__ == "__main__":
    rms(task_set)
