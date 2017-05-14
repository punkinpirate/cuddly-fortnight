from random import randint
import myPythonFunctions

operandList = [0,0,0,0,0]
operatorList = ['','','','']
operatorDict = {'1':'+', '2':'-', '3':'*', '4':'**'}

# populate operand list with random integer, 1 thru 9
i = 0
while i < 5:
    operandList[i] = randint(1, 9)
    i += 1

# populate operator list with random integer, 1 thru 9
i = 0
while i < 4:
    operatorList[i] = operatorDict['%s' %(randint(1, 4))]
    # check for congruent exponents
    if operatorList[i]=='**':
        if operatorList[i-1]=='**':
            i -= 1
    i += 1

# Create list of operand and operators in order
opList=['%d' %(operandList[0])]
i=0
while i < len(operatorList):
    opList.append('%s' %(operatorList[i]))
    opList.append('%d' %(operandList[i+1]))
    i += 1

# Join list into string with spaces
sep=' '
userMsg=sep.join(opList)
noSep=''
evalString=noSep.join(opList)

######## WHY DA HAIL DIS DOESN'T WORKING ########
userMsg.replace(' **', '**')
######## AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ########

# Send string as question to user and accept input to be evaluated
userAnswer = input('What does ' + userMsg + ' equal?\nNote: ** is an exponent operator\n')
compAnswer = eval(evalString)

print('Correct answer: %s | Your answer: %s'  %(compAnswer, userAnswer))
