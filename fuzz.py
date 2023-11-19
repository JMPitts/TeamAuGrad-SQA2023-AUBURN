
## fuzzer to fuzz methods in parser.py
import parser
import logger
import random 

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

    if (randValue == 2 ):
        randomInt = random.randint(0,100)
        return (randomInt)

    if (randValue == 3 ):
        randomfloat = round(random.uniform(0,100),3)
        return (randomfloat)

    if (randValue == 4 ):
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
        return (randomInt)
   



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

    for i in range(5):

        
        errorList1 = []
        try:
            weirdyaml = fuzzWeirdYAML()
            weirdyaml_result = parser.checkIfWeirdYAML(weirdyaml)
            print("\n1. Fuzzing checkIfWeirdYAML with ", str(weirdyaml) , "\nResult: is valid yaml " ,  str(weirdyaml_result) , "\n")
        except Exception as e:
            errorList.append("checkIfWeirdYAML: " + str(e))
            print("\n1. Fuzzing checkIfWeirdYAML with ", str(weirdyaml) , "\n\nException generated: " ,  str(e) , "\n\n")
        
        
        errorList2 = []
        try:
            print("\n\n2. Fuzzing getValuesRecursively with randomly sized nested dictionary",  list((parser.getValuesRecursively(fuzzKeyMiner()))) , "\n")
        except Exception as e:
            errorList.append("getValuesRecursively: " +  str(e))
            print("\n2. Fuzzing getValuesRecursively with ", str(weirdyaml) , "\n\nException generated: " ,  str(e) , "\n\n")
        
        errorList3 = []
        try:
            weirdyaml = fuzzWeirdYAML()
            ymlAsString = parser.readYAMLAsStr(weirdyaml)
            print("\n3. Fuzzing readYAMALAsStr with ", str(weirdyaml) , "\nResult: is valid yaml " ,  str(ymlAsString) , "\n")
        except Exception as e:
            errorList.append("readYAMALAsStr: " +  str(e))
            print("\n3. Fuzzing readYAMALAsStr with ", str(weirdyaml) , "\n\nException generated: " ,  str(e) , "\n\n")
        
        errorList4 = []
        try:
            weirdyaml = fuzzWeirdYAML()
            initial_comment = parser.count_initial_comment_line(weirdyaml)
            print("\n4. Fuzzing count_initial_comment_line with ", str(weirdyaml) , "\nResult: is valid yaml " ,  str(initial_comment) , "\n")
        except Exception as e:
            errorList.append("count_initial_comment_line: " +  str(e))
            print("\n4. Fuzzing count_initial_comment_line with ", str(weirdyaml) , "\n\nException generated: " ,  str(e) , "\n\n")
        
        errorList5 = []
        try:
            weirdyaml = fuzzWeirdYAML()
            SingleDict = parser.getSingleDict4MultiDocs(weirdyaml)
            print("\n5. Fuzzing getSingleDict4MultiDocs with ", str(weirdyaml) , "\nResult: is valid yaml " ,  str(SingleDict) , "\n")
        except Exception as e:
            errorList.append("getSingleDict4MultiDocs: " + str(e))
            print("\n5. Fuzzing getSingleDict4MultiDocs with ", str(weirdyaml) , "\n\nException generated: " ,  str(e) , "\n\n")

    ''' 
    try:
        weirdyaml = fuzzWeirdYAML()

        keyMiner = parser.keyMiner(fuzzKeyMiner(),getJunk())
        print("\n6. Fuzzing keyMiner with ", str(weirdyaml) , "\nResult: is valid yaml " ,  str(keyMiner) , "\n")
    except Exception as e:
         errorList.append("checkIfWeirdYAML: " + e)
        print("\n6. Fuzzing keyMiner with ", str(weirdyaml) , "\n\nException generated: " ,  str(e) , "\n\n")

    try:
        weirdyaml = fuzzWeirdYAML()

        ValidK8SYaml = parser.checkIfValidK8SYaml(weirdyaml)
        print("\n7. Fuzzing checkIfValidK8SYaml with ", str(weirdyaml) , "\nResult: is valid yaml " ,  str(ValidK8SYaml) , "\n")
    except Exception as e:
        print("\n7. Fuzzing checkIfValidK8SYaml with ", str(weirdyaml) , "\n\nException generated: " ,  str(e) , "\n\n")
    '''
    for i in range(len(errorList)):
        print("\n"+errorList[i])
    print("\n\n\nEnd of error list")




if __name__=='__main__':
    simpleFuzzer()