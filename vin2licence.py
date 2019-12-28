curFile = open('carLicense', 'r')
L2V = open('license2vin', 'w')
V2L = open('vin2license', 'w')

while True:
    curLine = curFile.readline().strip('\n')
    if curLine == '':
        break
    lineArr = curLine.split('\t')
    print(lineArr)
    L2V.write('"'+lineArr[0]+'"' + ' : ' + '"'+lineArr[1]+'"' + ',\n')
    V2L.write('"'+lineArr[1]+'"' + ' : ' + '"'+lineArr[0]+'"' + ',\n')

    