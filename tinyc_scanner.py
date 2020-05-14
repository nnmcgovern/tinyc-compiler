import sys
import os
from tinyc_output import appendOutput

def switchTokens(ch):
    switcher = {
        '(':'LP',
        ')':'RP',
        '=':'ASGN',
        ';':'SC',
        '+':'ADD',
        '-':'SUB',
        '<':'COMPARE'
        }
    return switcher.get(ch, 'not_symbol')

def lexicalError(pathOutput):
    # overwrite output file
    fileOutput = open(pathOutput, 'w')
    fileOutput.close()
    appendOutput(pathOutput, 'LEXICAL_ERROR')

def scanner():

    pathSource = sys.argv[1]
    pathOutput = 'tokens.txt'

    tokens = ['IF','THEN','WHILE','DO']

    # open source code file
    fileSource = open(pathSource, 'r')

    # create or overwrite output file
    fileOutput = open(pathOutput, 'w')
    fileOutput.close()

    # if source code file is not empty
    if os.path.getsize(pathSource) > 0:

        for line in fileSource:
            i = 0
            
            while i < len(line):

                if switchTokens(line[i]) == 'not_symbol':

                    if line[i] == ' ' or line[i] == '\n' or line[i] == '\t':
                        i = i + 1

                    # check if number
                    elif line[i] == '0':
                        if line[i+1].isdigit() == False:
                            appendOutput(pathOutput, 'num: "' + line[i] + '"')
                            i = i + 1

                        else: # error
                            lexicalError(pathOutput)
                            return False

                    elif line[i].isdigit() == True:
                        num = line[i]
                        i = i + 1

                        while i < len(line) and line[i].isdigit() == True:
                            num = num + line[i]
                            i = i + 1

                        if int(num) <= 2147483647:
                            appendOutput(pathOutput, 'num: "' + num + '"')

                        else: # illegal integer constant
                            lexicalError(pathOutput)
                            return False

                    # check if word
                    elif line[i].isalpha() == True:
                        word = line[i]
                        i = i + 1

                        while i < len(line) and line[i].isalpha() == True:
                            word = word + line[i]
                            i = i + 1

                        if word.upper() in tokens and word == word.lower():
                            appendOutput(pathOutput, word.upper() + ': "' + word + '"')

                        elif len(word) == 1 and word == word.lower():
                            appendOutput(pathOutput, 'id: "' + word + '"')

                        else: # error
                            lexicalError(pathOutput)
                            return False

                    # non-existent symbol
                    else:
                        lexicalError(pathOutput)
                        return False

                else:
                    appendOutput(pathOutput, switchTokens(line[i]) + ': "' + line[i] + '"')
                    i = i + 1

    # source code file was empty
    else:
        return False

    # scanner ran with no errors
    return True
