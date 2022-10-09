#gets all factors of a number
def factors(num):
    flist = []
    for i in range(1, num+1):
        if num % i == 0:
            flist.append(i)
    return flist

#gets the greatest common factor of 2 numbers
def gcf(num1, num2):
    
    # method 1 (probably better overall) - compare 2 sets. delete the difference of the 2 sets from 1 of the sets. 
    # should be left with all common factors
    # note - cant get largerst common factor ecause sets are unordered (pop and indexing do not work)

    #lists of all factors of num1 and num2
    fnum1 = factors(num1)
    fnum2 = factors(num2)

    print(str(fnum1) + ' - list 1 \n' + str(fnum2) + ' - list 2')

    #transforming factor lists into sets
    a = set(fnum1)
    b = set(fnum2)

    #gets intersection of sets (all common items)
    commonSet = a & b

    print(str(commonSet) + ' - all common factors')
    
    # method 2 (proably faster) - reverse for loops through list 1 until it finds an equivalent num in list 2. 
    # should produce one greatest common factor
    # note - slower if num1 >>> num2

    #for i in reversed(fnum1):
    #    num1 = i
    #    for j in reversed(fnum2):
    #        if num1 == j:
    #            return num1
    #    print(str(num1) + ' is not in list 2')
            



