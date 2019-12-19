import math
from math import gcd
import copy


class EDFalgo:

    def edf(self):
        if self.edf_utilization() is True:
            print("Schedulable under utilization test")
            self.generate_schedule(self.task_set)

    def edf_utilization(self):  # Sufficient, but not necessary
        total = 0
        n = len(self.task_set)
        for i in self.task_set.keys():
            total += self.task_set[i]['c'] / self.task_set[i]['p']
        if total <= 1:
            return True
        return False

    def generate_schedule(self, task_set):
        lcms = self.lcm()
        out = []
        for i in range(lcms):
            result = self.priority(task_set)
            if (result != -1):
                task_set[result]['c'] -= 1
                print(task_set[result]['name'])
                out.append(task_set[result]['name'])
            else:
                print("IDLE")
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
                if temp >= set[i]['p'] or temp >= self.original_set[i]['p']:
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
