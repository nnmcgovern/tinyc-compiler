def appendOutput(pathOutput, output):
    fileOutput = open(pathOutput, 'a')
    fileOutput.write(output + '\n')
    fileOutput.close()
