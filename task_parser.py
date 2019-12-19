from RMS import RMSalg


def read(list):
    tasks = dict()
    # tasks = {0: {
    #     "name": "t0",
    #     "c": 1,
    #     "p": 8,
    #     "i": 0,
    #     "active": False
    # },
    #     1: {
    #         "name": "t1",
    #         "c": 2,
    #         "p": 6,
    #         "i": 0,
    #         "active": False
    #     },
    #     2: {
    #         "name": "t2",
    #         "c": 4,
    #         "p": 24,
    #         "i": 0,
    #         "active": False
    #     }}
    #
    taskList = list.split(",")
    count = 0
    taski = 0
    for i in taskList:
        if (count % 2) == 0:
            tasks[taski] = {}
            tasks[taski]["name"] = "t"+str(taski)
            tasks[taski]['c'] = int(i)
        else:
            tasks[(taski)]['p'] = int(i)
            taski += 1
        count += 1

    startRMS = RMSalg(tasks)
    startRMS.rms()


# if __name__ == "__main__":
#     read()
