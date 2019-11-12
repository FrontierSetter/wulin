fileR = open('.\carList', 'r')
fileW = open('.\carListHTML', 'w')

while True:
    curLine = fileR.readline().strip();
    if curLine == '':
        break
    fileW.write('<option value="'+curLine+'">'+curLine+'</option>\n')

fileR.close()
fileW.close()