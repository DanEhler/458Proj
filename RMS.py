set1 = {
    "c": 5,
    "p": 10
}
set2 = {
    "c": 6,
    "p": 10
}
task_set = [set1, set2]


def rms(task_set):
    print(rms_utilization(set))


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
    return


if __name__ == "__main__":
    rms(task_set)
