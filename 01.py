def step1():
    with open('01.txt') as file:
        count = 0
        depthList = file.readlines()

        for i in range(1, len(depthList)):
            lastDepth = int(depthList[i - 1])
            newDepth = int(depthList[i])
            if newDepth > lastDepth:
                count = count + 1

    print('Step 1 Increase: ', count)


def step2():
    with open('01.txt') as file:
        count = 0
        depthList = file.readlines()

        for i in range(3, len(depthList)):
            currentDepthSum = int(depthList[i]) + int(depthList[i-1]) + int(depthList[i-2])
            prevDepthSum = int(depthList[i-1]) + int(depthList[i-2]) + int(depthList[i-3])

            if currentDepthSum > prevDepthSum:
                count = count + 1

    print('Step 2 Increase: ', count)

step1()
step2()