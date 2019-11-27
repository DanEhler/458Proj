import math

# Will be from task parser
set1 = {
    "c": 1,
    "p": 8
}
set2 = {
    "c": 2,
    "p": 6
}
set3 = {
    "c": 4,
    "p": 24
}
task_set = [set1, set2, set3]


def rms(task_set):
    if rms_utilization(task_set) is True:
        print("Schedulable under utilization test")
    else:
        print("Not schedulable under utilization test")
    if exact_analysis(task_set) is True:
        print ("Schedulable under exact analysis")
    else:
        print("Not schedulable under exact analysis")


def rms_utilization(task_set):
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


if __name__ == "__main__":
    rms(task_set)
