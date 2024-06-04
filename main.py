import itertools



# Method to turn users string of numbers into usable ints
def userNmbsToInts(numbersString):

    charOne = numbersString[0]
    nmbOne = int(charOne)
    #print(nmbOne)

    charTwo = numbersString[1]
    nmbTwo = int(charTwo)
    #print(nmbTwo)

    charThree = numbersString[2]
    nmbThree = int(charThree)
    #print(nmbThree)

    charFour = numbersString[3]
    nmbFour = int(charFour)
    #print(nmbFour)

    #numberArray = arr.array([nmbOne, nmbTwo, nmbThree, nmbFour])
    nmbList = [nmbOne, nmbTwo, nmbThree, nmbFour]
    #make10(numberArray)
    return nmbList


def make10(list):
    #while True:
        for i in range(len(list)):
            for j in range(len(list)):
                if (j != i):                    # This will make sure that numbers will not do operations on themselves.
                    #print(list[i] * list[j])
                    part1PLUS = list[i] + list[j]
                    part1MINUS = list[i] - list[j]
                    part1TIMES = list[i] * list[j]
                    part1DIVIDE = list[i] / list[j]
                    part1POWER = list[i] ** list[j]
                    listFirstOperations = [part1PLUS, part1MINUS, part1TIMES, part1DIVIDE, part1POWER]
                    for k in range(len(list)):
                        if (k != i and k != j):
                            for a in range(len(listFirstOperations)):
                                part2PLUS = listFirstOperations[a] + list[k]
                                part2MINUS = listFirstOperations[a] - list[k]
                                part2TIMES = listFirstOperations[a] * list[k]
                                part2DIVIDE = listFirstOperations[a] / list[k]
                                part2POWER = listFirstOperations[a] ** list[k]
                                listSecondOperations = [part2PLUS, part2MINUS, part2TIMES, part2DIVIDE, part2POWER]

                                for l in range (len(list)):
                                    if (l != i and l != j and l != k):
                                        for b in range(len(listSecondOperations)):
                                            part3PLUS = listSecondOperations[b] + list[l]
                                            part3MINUS = listSecondOperations[b] - list[l]
                                            part3TIMES = listSecondOperations[b] * list[l]
                                            part3DIVIDE = listSecondOperations[b] / list[l]
                                            part3POWER = listSecondOperations[b] ** list[l]
                                            listThirdOperations = [part3PLUS, part3MINUS, part3TIMES, part3DIVIDE, part3POWER]
                                            for c in range(len(listThirdOperations)):
                                                if (listThirdOperations[c] == 10):
                                                    A = str(list[i])
                                                    B = str(list[j])
                                                    C = str(list[k])
                                                    D = str(list[l])
                                                    ANSWER = str(listThirdOperations[c])


                                                    if (a == 0):
                                                        operator1 = " + "
                                                    elif (a == 1):
                                                        operator1 = " - "
                                                    elif (a == 2):
                                                        operator1 = " x "
                                                    elif (a == 3):
                                                        operator1 = " / "
                                                    else:
                                                        operator1 = " to the power "


                                                    if (b == 0):
                                                        operator2 = " + "
                                                    elif (b == 1):
                                                        operator2 = " - "
                                                    elif (b == 2):
                                                        operator2 = " x "
                                                    elif (b == 3):
                                                        operator2 = " / "
                                                    else:
                                                        operator2 = " to the power "


                                                    if (c == 0):
                                                        operator3 = " + "
                                                    elif (c == 1):
                                                        operator3 = " - "
                                                    elif (c == 2):
                                                        operator3 = " x "
                                                    elif (c == 3):
                                                        operator3 = " / "
                                                    else:
                                                        operator3 = " to the power "


                                                    print(A + operator1 + B + operator2 + C + operator3 + D + " = " + ANSWER)
                                                    #break


def make10v2(list):
    part1PLUS = list[0] + list[1]
    part1MINUS = list[0] - list[1]
    part1TIMES = list[0] * list[1]
    part1DIVIDE = list[0] / list[1]
    part1POWER = list[0] ** list[1]
    listFirstOperations = [part1PLUS, part1MINUS, part1TIMES, part1DIVIDE, part1POWER]

    for a in range(len(listFirstOperations)):
        part2PLUS = listFirstOperations[a] + list[2]
        part2MINUS = listFirstOperations[a] - list[2]
        part2TIMES = listFirstOperations[a] * list[2]
        part2DIVIDE = listFirstOperations[a] / list[2]
        part2POWER = listFirstOperations[a] ** list[2]
        listSecondOperations = [part2PLUS, part2MINUS, part2TIMES, part2DIVIDE, part2POWER]

        for b in range(len(listSecondOperations)):
            part3PLUS = listSecondOperations[b] + list[3]
            part3MINUS = listSecondOperations[b] - list[3]
            part3TIMES = listSecondOperations[b] * list[3]
            part3DIVIDE = listSecondOperations[b] / list[3]
            part3POWER = listSecondOperations[b] ** list[3]
            listThirdOperations = [part3PLUS, part3MINUS, part3TIMES, part3DIVIDE, part3POWER]

            for c in range(len(listThirdOperations)):
                if (listThirdOperations[c] == 10):
                    ANSWER = str(listThirdOperations[c])


                    if (a == 0):
                        operator1 = " + "
                    elif (a == 1):
                        operator1 = " - "
                    elif (a == 2):
                        operator1 = " x "
                    elif (a == 3):
                        operator1 = " / "
                    else:
                        operator1 = " to the power "


                    if (b == 0):
                        operator2 = " + "
                    elif (b == 1):
                        operator2 = " - "
                    elif (b == 2):
                        operator2 = " x "
                    elif (b == 3):
                        operator2 = " / "
                    else:
                        operator2 = " to the power "


                    if (c == 0):
                        operator3 = " + "
                    elif (c == 1):
                        operator3 = " - "
                    elif (c == 2):
                        operator3 = " x "
                    elif (c == 3):
                        operator3 = " / "
                    else:
                        operator3 = " to the power "

                    if (operator1 == " + " or operator1 == " - "):
                        print("(" + str(list[0]) + operator1 + str(list[1]) + ")" + operator2 + str(list[2]) + operator3 + str(list[3]) + " = " + ANSWER)
                        
                    # elif (operator2 == " + " or operator2 == " - "):
                    #     print(str(list[0]) + operator1 + "(" + str(list[1]) + operator2 + str(list[2]) + ")" + operator3 + str(list[3]) + " = " + ANSWER)
                    # elif (operator3 == " + " or operator3 == " - "):
                    #     print(str(list[0]) + operator1 + str(list[1]) + operator2 + "(" + str(list[2]) + operator3 + str(list[3]) + ")" + " = " + ANSWER)
                    else:
                        print(str(list[0]) + operator1 + str(list[1]) + operator2 + str(list[2]) + operator3 + str(list[3]) + " = " + ANSWER)

                    




def main():
    while True:
        # This will take in the users numbers.
        numbers = input("Please enter your 4 digit number: ")
        if (len(numbers) == 4):
            everyNumberList = [''.join(i) for i in itertools.permutations(numbers, 4)]
            for x in everyNumberList:
                numberList= userNmbsToInts(x)
                #make10(numberList)
                make10v2(numberList)
        elif (numbers == 'X') or (numbers == 'x'):
            break
        else:
            print("You can only print a four digit numer, eg.1234...    Enter 'X' to exit the program.")
            
    



if __name__ == "__main__":
    main()








#note - search google to find out how many combinations there are for a four digit number, Then get a function that will sort the 4 numbers into every different possibliliy, then have a function that takes all of these different possibilites and do all the different operation on them.