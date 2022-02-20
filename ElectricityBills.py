def bill(unit):
    ans = None
    # YOUR CODE GOES HERE
    amt = 0.0

    if unit <= 50:
        amt = unit * 0.50
    elif unit <= 150:
        amt = 25 + ((unit - 50) * 0.75)
    elif unit <= 250:
        amt = 100 + ((unit - 150) * 1.20)
    else:
        amt = 220 + ((unit - 250) * 1.50)

    ans = amt + amt * 0.20
    return int(ans)

######################
def bill(unit):
    ans = None
    unit = int(unit)
    if unit <= 50:
        bill = 0.50 * unit
        bill = bill + (0.20 * bill)
        print(int(bill))

    elif  unit <= 150 and unit > 50:
        tempN = unit - 50
        temp = 50 * 0.5
        temp1 = tempN * 0.75
        bill = temp + temp1
        bill = bill + (0.20 * bill)
        print(int(bill))

    elif unit <=250  and unit > 150:
        tempN = unit - 150
        temp1 = 1.20 * tempN
        temp2 = 0.75 * 100
        temp3 = 50 * 0.50
        bill = temp1 + temp2 + temp3
        bill = bill + (0.20 * bill)
        print(int(bill))

    else:
        tempN = unit - 250
        temp1 = tempN * 1.50
        temp2 = 50 * 0.5
        temp3= 100 * 0.75
        temp4 = 100 * 1.20
        bill = temp1 + temp2 + temp3 + temp4
        bill = bill + (0.20 * bill)
        print(int(bill))

    #return ans
