def truckTour(petrolpumps):
    container = start = 0
    for i in range(len(petrolpumps)):
        container += (petrolpumps[i][0] - petrolpumps[i][1])
        if container < 0:
            container = 0
            start = i + 1
    return start
