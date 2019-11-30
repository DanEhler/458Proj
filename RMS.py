import math
from math import gcd

# import matplotlib.pyplot as plot
# Will be from task parser: i is iteration
set1 = {
    "name": "t0",
    "c": 1,
    "p": 8,
    "i": 1
}
set2 = {
    "name": "t1",
    "c": 2,
    "p": 6,
    "i": 1
}
set3 = {
    "name": "t2",
    "c": 4,
    "p": 24,
    "i": 1
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
    sorted_set = sorted(task_set, key=lambda i: i['p'])
    lcms = lcm(task_set)
    fluid_set = task_set
    flow = []
    for t in range(lcms):
        tn = priority(fluid_set)

        test = next(task for task in fluid_set if task["name"] == tn)
        flow.append({"name": tn, "start": [t], "end": [t + 1]})
        print("here")
    ###
    """
    fig, gnt = plot.subplots()
    gnt.set_xlim(0, lcms)
    gnt.set_ylim(0, len(task_set))
    plot.show()
    """


def priority(task_set):
    tmpP = 999
    active_task = ""
    for task in task_set:
        if task['p'] * task['i'] < tmpP:
            tmpP = task['p']
            active_task = task['name']

    return active_task


def lcm(list_period):
    lcm = list_period[0]['p']
    for i in list_period[1:]:
        i = i['p']
        lcm = lcm * i // gcd(lcm, i)
    return lcm


if __name__ == "__main__":
    rms(task_set)
