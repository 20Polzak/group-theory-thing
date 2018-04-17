banned = ['o','(',')',',',' ']

def deconstructInput(input):
    permutationSet = []
    cycleSet = []
    for n in input:
        if n == '(':
            currentCycle = []
        if n == ')':
            cycleSet.append(currentCycle)
        if n not in banned:
            currentCycle.append(n)
        if n == 'o':
            permutationSet.append(cycleSet)
            cycleSet = []
    permutationSet.append(cycleSet)
    return permutationSet

def deconstructCycleSet(cycleSet):
    map = {}
    for cycle in cycleSet:
        for k in range(len(cycle)):
            if cycle[k] in map.keys():
                return 'invalid permutation: double-mapping'
            else:
                map[cycle[k]] = cycle[(k + 1) % len(cycle)]
    return map

def getDeepest(map2,map1,n):
    try:
        return map1[map2[n]]
    except:
        try:
            return map2[n]
        except:
            print('broke')
            return str(n)

def composeCycles(map2, map1):
    basicComp = {}
    for i in range(1,len(map2)+1):
        n = list(map2.keys())[-i]
        basicComp[n] = getDeepest(map2, map1, n)
    for k in map1:
        if k not in map2:
            basicComp[k] = map1[k]
    print(basicComp)
    return basicComp

def fullyCycle(basicComp):
    fullCyclic = []
    while len(basicComp) > 0:
        currentCycle = []
        key = str(list(basicComp.keys())[0])
        currentCycle.append(key)
        currVal = basicComp.pop(key)
        while currVal != currentCycle[0]:
            currentCycle.append(currVal)
            currVal = basicComp.pop(currVal)
        fullCyclic.append(currentCycle)
    return fullCyclic

def displayPermutation(fullCyclic):
    permutation = ''
    for cycle in fullCyclic:
        permutation += '(' + ' '.join(cycle) + ')'
    return permutation

def main():
    print('Composes in cyclic permutation notation. Separate the things being composed with \'o\'. Separate cycles with parenthesis. Input \'q\' to quit')
    entry = ''
    while entry != 'q':
        entry = input('Enter permutation => ')
        cycleSet1, cycleSet2 = deconstructInput(entry)
        print('Result:', displayPermutation(fullyCycle(composeCycles(deconstructCycleSet(cycleSet2), deconstructCycleSet(cycleSet1)))))


if __name__ == '__main__':
    main()