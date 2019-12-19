import math
from math import gcd
import copy

# task_set = {
#
#     0: {"name": "t0",
#         "c": 1,
#         "p": 8,
#         },
#     1: {"name": "t1",
#         "c": 2,
#         "p": 6,
#        },
#     2: {"name": "t2",
#         "c": 4,
#         "p": 24,
#         }
# }


class RMSalg:

    def rms(self):
        if self.rms_utilization() is True:
            print("Schedulable under utilization test")
            self.instance.output("Schedulable under utilization test")
            self.generate_schedule(self.task_set)

        else:
            print("Not schedulable under utilization test")
            self.instance.output("Not schedulable under utilization test")
            if self.exact_analysis() is True:
                print("Schedulable under exact analysis")
                self.instance.output("Schedulable under exact analysis")
                self.generate_schedule(self.task_set)
            else:
                print("Not schedulable under exact analysis")
                self.instance.output("Not schedulable under exact analysis")
    def rms_utilization(self):  # Sufficient, but not necessary
        total = 0
        n = len(self.task_set)
        for i in self.task_set.keys():
            total += self.task_set[i]['c'] / self.task_set[i]['p']
        exp = 2 ** float(1 / n)
        comp = float((n * (exp - 1)))
        if total <= comp:
            return True
        return False

    def exact_analysis(self):
        sort_set = sorted(self.task_set.items(), key=lambda i: i[1]['p'], reverse=True)  # sort by period
        sort_set = dict(sort_set)
        for i in self.task_set.keys():
            dt = sort_set[i]['p']
            # to = sum(sort_set[i]['c'] for task in sort_set)
            to = sum(d['c'] for d in sort_set.values() if d)
            if self.inner_exact(to, sort_set, dt) is False:
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
    def inner_exact(self, t, task_set, dt):
        total = 0
        for i in task_set:
            total += task_set[i]['c'] * math.ceil(t / task_set[i]['p'])
        if total is t:
            if t <= dt:
                return True
            else:
                return False
        else:
            self.inner_exact(total, task_set, dt)

    # sorted_set = copy.deepcopy(sorted(task_set, key=lambda i: i['p']))

    def generate_schedule(self, task_set):
        lcms = self.lcm()
        out = []
        for i in range(lcms):
            result = self.priority(task_set)
            if result != -1:
                task_set[result]['c'] -= 1
                print(task_set[result]['name'])
                out.append(task_set[result]['name'])
                # self.instance.output(task_set[result]['name'])
            else:
                print("IDLE")
                # self.instance.output("IDLE")
                out.append("IDLE")

            for j in task_set.keys():
                task_set[j]['p'] -= 1
                if task_set[j]['p'] == 0:
                    task_set[j] = copy.deepcopy(self.original_set[j])
        self.instance.output(out)
        return

    def priority(self, set):
        temp = 9999999
        active = -1
        for i in self.task_set.keys():
            if set[i]['c'] != 0:
                if temp > set[i]['p'] or temp > self.original_set[i]['p']:
                    temp = set[i]['p']
                    active = i

        return active

    def lcm(self):
        # lcm = list_period[0]['p']
        tmp = []
        for i in range(len(self.task_set)):
            tmp.append(self.task_set[i]['p'])
        lcms = self.task_set[0]['p']
        for i in tmp[1:]:
            lcms = lcms * i // gcd(lcms, i)
        return lcms

    def __init__(self, task_set, instance):
        self.task_set = task_set
        self.original_set = copy.deepcopy(task_set)
        self.instance = instance

    # if __name__ == "__main__":
    #     rms(task_set)
