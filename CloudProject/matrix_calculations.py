import multiprocessing, ctypes, time

def read_matrix(file_name):

    path='matrices/' + file_name + '.txt'

    output = []

    try:
        with open(path, 'r') as f:
            row, col = map(int, f.readline().split())

            for i in range(0, row+1):
                output.append(list(map(int, f.readline().split()[:col+1])))

            output.remove(output[0])
            return output
    except IOError:
        return output

def print_matrix(matrix):
    file = open('result.txt', 'w')
    for row in matrix:
        for val in row:
            file.write(str(val))
            file.write(" ")
        file.write('\n')

    file.close()

def print_matrix_names(matrices_name):
    for i, item in enumerate(matrices_name):
        print(i,'.', item)

def read_matrices(matrices_name):
    i = 1
    matrices=[]
    while i:
        j = 0

        print('Enter name of the file containing matrix without file extension')
        file_name = input()

        output = read_matrix(file_name)

        print(' ')

        if output != []:

            print('Matrix saved as: ', file_name)
            matrices.append(output)
            matrices_name.append(file_name)

            while j == 0:
                print('Would you like to add another one? y/n')
                decision=input()

                if decision!="y" and decision!="n":
                    print('Please, repeat your answer')
                    j = 0
                else:
                    if decision=="y":
                        i = 1
                    else:
                        i = 0
                    j = 1
        else:
             print('Could not load matrix form this file. Try again.')

    return matrices

def print_math_operations():

    print()
    print('1. "*"')
    print('2. "+"')



def mx_multiplication(mx1, mx2):
    sum = 0.0
    c = []
    result = []
    for k in range(len(mx1)):
        for i in range(len(mx2[k])):
            for j in range(len(mx2)):
                sum += mx1[k][j] * mx2[j][i]


            c.append(sum)
            sum = 0.0
        result.append(c)
        c = []

    return result

def mx_adding(mx1, mx2):
    result = []
    c=[]
    for i in range(len(mx1)):
        for j in range(len(mx1[0])):
             c.append(mx1[i][j]+mx2[i][j])

        result.append(c)
        c=[]

    return result

def configure_expression(matrices_name, matrices):
    print('Expression Configurator')
    print()

    expression=" "

    addition_list = []
    multiplication_list = []

    i=1
    while i:
        j=1
        print('Choose matrix by entering properly number.')
        print_matrix_names(matrices_name)

        while j:
            number=input()
            number=int(number)

            if number > (len(matrices_name)-1) or number < 0:
                print('Wrong number, type again')
                j=1
            else:
                j=0
                temp_name=matrices_name[number]
                temp_matrix=matrices[number]


        print(' ')
        print('Your expression: ', expression + " " + temp_name)
        print(' ')

        j=0
        while j == 0:
            print('Would you like to end configuring? y/n')
            decision = input()

            if decision != "y" and decision != "n":
                print('Please, repeat your answer')
                j = 0
            else:
                if decision == "y":
                    i = 0
                else:
                    i = 1
                j = 1

        if decision == "y":
            if expression[-1] == " " or expression[-1] == "+":
                addition_list.append(temp_matrix)
            else:
                multiplication_list[len(multiplication_list)-1].append(temp_matrix)

            expression = expression + " " + temp_name
            break

        j=1
        print('')
        print('Choose mathematical operation:')
        print_math_operations()

        while j:
            number = input()
            number = int(number)

            if number > 2 or number < 1:
                print('Wrong number, type again')
                j = 1
            else:
                j = 0
                if number == 1:
                    temp_char="*"
                else:
                    temp_char="+"


        if (expression[-1]==" " or expression[-1]=="+") and temp_char=="+" :
            addition_list.append(temp_matrix)
        elif (expression[-1]==" " or expression[-1]=="+") and temp_char=="*" :
            temp_list=[]
            temp_list.append(temp_matrix)
            multiplication_list.append(temp_list)
        else:
            multiplication_list[len(multiplication_list)-1].append(temp_matrix)

        expression = expression + " " + temp_name + " " + temp_char



    lists=[]
    lists.append(multiplication_list)
    lists.append(addition_list)

    return lists


def calculations(multiplication_list, addition_list):

    t1 = time.clock()
    i=0
    while i < len(multiplication_list):

        while(len(multiplication_list[i])>1):
            temp = mx_multiplication(multiplication_list[i][0], multiplication_list[i][1])
            multiplication_list[i][0] = temp
            multiplication_list[i].remove(multiplication_list[i][1])
        addition_list.append(multiplication_list[i][0])
        i=i+1

    result_init = []
    result = []
    for x in range(len(addition_list[0])):
        for y in range(len(addition_list[0][0])):
            result_init.append(0)
        result.append(result_init)
        result_init = []

    for i in range(len(addition_list)):

         result = mx_adding(result, addition_list[i])
    t2 = time.clock()

    print("")
    print("Calculations ended in: ",'{0:.26f}'.format(t2-t1), " s.")
    return result









matrices_name=[] #list of names of the matrices
matrices=[] #list of matrices imported to the program
lists=[] #list which consists of two list: list with matrices to multiplicate and list with the ones to add
end_result=[] #two-dimensional list to store the result of expression


matrices=read_matrices(matrices_name)

lists=configure_expression(matrices_name, matrices)
multiplication_list=lists[0]
addition_list=lists[1]

end_result=calculations(multiplication_list, addition_list)


print_matrix(end_result)

