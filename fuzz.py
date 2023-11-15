

##count_initial_comment_line (filepath):

##def checkIfWeirdYAML(yaml_script):

##def getKeyRecursively(  dict_, list2hold,  depth_ = 0  ) :
import parser
import logger
import random 

#print(parser.checkIfWeirdYAML("FuzzingFiles/Comment_Line_Test_1.yaml"))

def getNaughtyLine():
        f= open("blns.json", "r")
        lines = f.readlines()
        randLine = random.randint(0,515)
        return lines[randLine]

def getJunk(): # returns a random datatype with a random value. 

    randValue = random.randint(1,4)

    if (randValue == 1 ):
        f= open("blns.json", "r")
        lines = f.readlines()
        randLine = random.randint(0,515)
        return lines[randLine]

    if (randValue == 1 ):
        randomInt = random.randint(0,100)
        return (randomInt)

    if (randValue == 1 ):
        randomfloat = round(random.uniform(0,100),3)
        return (randomfloat)

    if (randValue == 4 ):
        return (None)


def fuzzWeirdYAML():
   # generated either an invalid path or sends an integer value or float value

   
      return (getJunk())


   


def fuzzKeyMiner():     #Creates a randomly nested dictionary with naughty values.

    randChoice = random.randint(1,2)

    if(randChoice == 1):
        randValue = random.randint(1,10)
        nestedDict = {}
        for i in range(randValue):

            testDict = { getJunk(): getJunk()}
            nestedDict[i] = testDict

        return(nestedDict)
    else:
        return (getJunk())



def simpleFuzzer():

    weirdyaml = fuzzWeirdYAML()

    try:
        weirdyaml_result = parser.checkIfWeirdYAML(weirdyaml)
        print("\n1. Fuzzing checkIfWeirdYAML with ", str(weirdyaml) , "\nResult: is valid yaml " ,  str(weirdyaml_result) , "\n")
    except Exception as e:
        print("\n1. Fuzzing checkIfWeirdYAML with ", str(weirdyaml) , "\n\nException generated: " ,  str(e) , "\n\n")

    try:
        print("\n\n1. Fuzzing getValuesRecursively with randomly sized nested dictionary",  list((parser.getValuesRecursively(fuzzKeyMiner()))) , "\n")
    except Exception as e:
        print("\n1. Fuzzing checkIfWeirdYAML with ", str(weirdyaml) , "\n\nException generated: " ,  str(e) , "\n\n")


    #print (getNaughtyLine())

    #print 



if __name__=='__main__':
    simpleFuzzer()