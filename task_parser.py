import RMS


def read():
    #tasks = dict()
    tasks = {0: {
        "name": "t0",
        "c": 1,
        "p": 8,
        "i": 0,
        "active": False
    },
        1: {
            "name": "t1",
            "c": 2,
            "p": 6,
            "i": 0,
            "active": False
        },
        2: {
            "name": "t2",
            "c": 4,
            "p": 24,
            "i": 0,
            "active": False
        }}
    """
    sp = int(input("Enter number of tasks:"))
    for i in range(sp):
        tasks[i] = {}
        tasks[i]["name"] = "t"+str(i)
        print("Enter C for task T", i)
        c = input()
        tasks[i]['c'] = int(c)
        print("Enter P for task T", i)
        p = input()
        tasks[i]['p'] = int(p)
        tasks[i]['i'] = 0
        tasks[i]["active"] = False
    """
    RMS.rms(tasks)


if __name__ == "__main__":
    read()
