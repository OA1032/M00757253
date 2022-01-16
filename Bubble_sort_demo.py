import pdb #import python debugger

L = [30, 21, 16, 66, 78, 109, 1, 4, 52]
print(L) #show list before sorting algorithm

def bubbleSort(lis): # function for sorting algo
    length = len(lis) # called with the L variable, length = 9
    for i in range(length): # go from 0 to 8:
        for j in range(length - i): #8-i: 7 to 0
            a = lis[j]
            if a != lis[-1]:
                b = lis[j + 1]
                if a > b:
                    lis[j] = b
                    lis[j + 1] = a
        #print(lis)
    return lis

pdb.set_trace() # set a trace for the debugger
bubbleSort(L) # perform function (step thru)
print(L) # show the list after sorting
