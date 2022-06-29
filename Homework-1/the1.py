import time

def probes(txt, probeLen):
    subSeqDict = dict()
    nuc = {'A', 'T', 'G', 'C'}
    dnaSequences = list()
    lengthOfValidSequence = 27000

    for i in open(txt).read().split():
        i = i[:lengthOfValidSequence]
        if set(i).issubset(nuc):
            dnaSequences.append(i)

    dnaSequences = list(set(dnaSequences))

    # dnaSequences = dnaSequences[:250]

    for j in range(len(dnaSequences)):
        tempSet = set()
        for k in range(len(dnaSequences[j]) - probeLen + 1):
            if (dnaSequences[j][k:k + probeLen] in subSeqDict) and (dnaSequences[j][k:k + probeLen] not in tempSet):
                subSeqDict[str(dnaSequences[j][k:k + probeLen])] += 1
            else:
                subSeqDict[str(dnaSequences[j][k:k + probeLen])] = 1
            tempSet.add(dnaSequences[j][k:k + probeLen])
            # if string has same subsequence more than once with this way I use only one time this subsequnce

    maxKeyValue = 1
    for key, result in subSeqDict.items():
        if (result > maxKeyValue):
            maxKeyValue = result

    resultList = list()
    for key, result in subSeqDict.items():
        if (result == maxKeyValue):
            resultList.append(key)

    file = open("muhammedBayram.txt", "w")
    file.write(str(len(dnaSequences)) + " " + str(maxKeyValue))
    file.write("\n" + str(len(resultList)) + "\n")
    for x in range(len(resultList)):
        file.write(str(list(resultList)[x]) + "\n")
    file.close()

start = time.time()
probes('turkey.txt', 100)
end = time.time()
print(end - start)
