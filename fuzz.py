
## fuzzer to fuzz methods in parser.py
import parser
import random 



def getJunk(): # returns a random datatype with a random value. 

    randValue = random.randint(1,3)

    if (randValue == 1 ):
        randomInt = random.randint(0,100)
        return (randomInt)

    if (randValue == 2 ):
        randomfloat = round(random.uniform(0,100),3)
        return (randomfloat)

    if (randValue == 3 ):
        return (None)


def fuzzWeirdYAML():
   # generated either an invalid path or sends an integer value or float value
    randValue = random.randint(1,2)

    if (randValue == 1 ):
        f= open("blns.json", "r")
        lines = f.readlines()
        randLine = random.randint(0,515)
        return lines[randLine]

    if (randValue == 2 ):
        randomInt = random.randint(0,100)
        return (getJunk)
   



def fuzzKeyMiner():     #Creates a randomly nested dictionary with bad values.

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
    errorList = []
    for i in range(5):
 
        try:
            weirdyaml = fuzzWeirdYAML()
            weirdyaml_result = parser.checkIfWeirdYAML(weirdyaml)
        except Exception as e:
            errorList.append("checkIfWeirdYAMLwith input of "+ str(weirdyaml) + "  ERROR IS:   " +   str(e))
        
        try:
            weirdyaml = fuzzWeirdYAML()

            ValidK8SYaml = parser.checkIfValidK8SYaml(weirdyaml)
        except Exception as e:
            errorList.append("checkIfValidK8SYaml with input of "+ str(weirdyaml) + "  ERROR IS:   " +   str(e))

        try:
            weirdyaml = fuzzWeirdYAML()
            ymlAsString = parser.readYAMLAsStr(weirdyaml)
        except Exception as e:
            errorList.append("readYAMALAsStr with input of "+ str(weirdyaml) + "  ERROR IS:   " +   str(e))
        
        try:
            weirdyaml = fuzzWeirdYAML()
            initial_comment = parser.count_initial_comment_line(weirdyaml)
        except Exception as e:
            errorList.append("count_initial_comment_line with input of "+ str(weirdyaml) + "  ERROR IS:   " +   str(e))
        
        try:
            weirdyaml = fuzzWeirdYAML()
            SingleDict = parser.getSingleDict4MultiDocs(weirdyaml)
        except Exception as e:
            errorList.append("getSingleDict4MultiDocs with input of " + str(weirdyaml) + "  ERROR IS:   " +  str(e))

    for i in range(len(errorList)):
        print("\n\nError found in method: "+errorList[i])
    print("\n\n\n****End of error list****")


if __name__=='__main__':
    simpleFuzzer()