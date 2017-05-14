# Imports
from random import randint
from os import remove, rename
import forceOpen

# Deliver user score
def getUserPoint(userName):
    # Attempt to open scores file
    forceOpen('userScores.txt')

    # Open file to memory
    f = open('userScores.txt', 'r')
    # Find user name and return score, else  return -1
    for line in f:
        content = line.split(', ')
        if content[0]==userName:
            return content[1]
    return '-1'
    f.close()

# Create user entry or update user score
def updateUserPoints(newUser, userName, score):
    # Check if user is new
    if newUser == True:
        # Append user to userScores.txt
        f = open('userScores.txt', 'a')
        msg=(userName + ', ' + score + '\n')
        f.write(msg)
        f.close()
        
    else:
        # Open existing score, create temporary handler
        f = open('userScores.txt', 'r')
        w = open('userScores.tmp', 'w')

        print('\nCurrent score list:\n')
        # Read line, check for userName, write new score to temp
        for l in f:
            content = l.split(', ')
            if content[0]==userName:
                content[1] = score + '\n'
            msg=(content[0] + ', ' + content[1])
            print(msg, end = '')
            l = w.write(msg)
        f.close()
        w.close()
        print('\n\n>Saved!')
        # Remove old txt and rename temp file
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
