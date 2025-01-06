def runThroughList(list, var):
    num = 0
    for _ in range(len(list)):
        if var == list[num]:
            return True
        else:
            num += 1
