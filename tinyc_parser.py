from tinyc_output import appendOutput

def productions(values):
    switcher = {
        ('<program>','id'):['<statement_list>'],
        ('<program>','SC'):['<statement_list>'],
        ('<program>','WHILE'):['<statement_list>'],
        ('<program>','DO'):['<statement_list>'],
        ('<program>','IF'):['<statement_list>'],
        ('<program>','$'):['<statement_list>'],
        ('<statement_list>','id'):['<statement>','SC','<statement_list>'],
        ('<statement_list>','SC'):['<statement>','SC','<statement_list>'],
        ('<statement_list>','WHILE'):['<statement>','SC','<statement_list>'],
        ('<statement_list>','DO'):['<statement>','SC','<statement_list>'],
        ('<statement_list>','IF'):['<statement>','SC','<statement_list>'],
        ('<statement_list>','$'):['E'],
        ('<statement>','id'):['id','ASGN','<expr>'],
        ('<statement>','SC'):['SC'],
        ('<statement>','WHILE'):['WHILE','<paren_expr>','<statement>'],
        ('<statement>','DO'):['DO','<statement>','WHILE','<paren_expr>'],
        ('<statement>','IF'):['IF','<paren_expr>','<statement>'],
        ('<paren_expr>','LP'):['LP','<expr>','RP'],
        ('<expr>','num'):['<test>'],
        ('<expr>','id'):['<test>'],
        ('<expr>','LP'):['<test>'],
        ('<test>','num'):['<sum>','<test_opt>'],
        ('<test>','id'):['<sum>','<test_opt>'],
        ('<test>','LP'):['<sum>','<test_opt>'],
        ('<test_opt>','COMPARE'):['COMPARE','<sum>'],
        ('<test_opt>','RP'):['E'],
        ('<test_opt>','SC'):['E'],
        ('<test_opt>','WHILE'):['E'],
        ('<sum>','num'):['<term>','<sum_opt>'],
        ('<sum>','id'):['<term>','<sum_opt>'],
        ('<sum>','LP'):['<term>','<sum_opt>'],
        ('<sum_opt>','SUB'):['SUB','<term>','<sum_opt>'],
        ('<sum_opt>','ADD'):['ADD','<term>','<sum_opt>'],
        ('<sum_opt>','COMPARE'):['E'],
        ('<sum_opt>','RP'):['E'],
        ('<sum_opt>','SC'):['E'],
        ('<sum_opt>','WHILE'):['E'],
        ('<term>','num'):['num'],
        ('<term>','id'):['id'],
        ('<term>','LP'):['<paren_expr>']
        }
    return switcher.get(values, 'syntax_error')

def syntaxError(pathOutput):
    # overwrite output file
    fileOutput = open(pathOutput, 'w')
    fileOutput.close()
    appendOutput(pathOutput, 'SYNTAX_ERROR')

def parser():

    pathTokens = 'tokens.txt'
    pathOutput = 'parse_tree.txt'

    terms = ['num','id','SUB','ADD','COMPARE','RP','LP','SC','ASGN','WHILE','DO','IF']

    tokens = []
    fileTokens = open(pathTokens, 'r')

    for line in fileTokens:
        token = line.split(':')
        token = token[0]
        tokens.append(token)

    tokens.append('$')
    tokens.reverse()

    # create or overwrite output file
    fileOutput = open(pathOutput, 'w')
    fileOutput.close()

    stack = []

    stack.append('$')
    stack.append('<program>')

    token = tokens.pop()
    x = stack[-1]

    while True:
        if x == 'E':
            stack.pop()
        
        elif x in terms:
            if x == token:
                appendOutput(pathOutput, stack.pop())
                token = tokens.pop()
                
            else:
                syntaxError(pathOutput)
                return False

        else: # x is non-term
            prod = productions((x, token))

            if prod == 'syntax_error':
                syntaxError(pathOutput)
                return False
                
            else:
                appendOutput(pathOutput, stack.pop())
                
                # add production to stack in reverse order
                i = -1
                while i * (-1) <= len(prod):
                    stack.append(prod[i])
                    i = i - 1

        x = stack[-1]
            
        if x == '$':
            break

    # parser ran with no errors
    return True
