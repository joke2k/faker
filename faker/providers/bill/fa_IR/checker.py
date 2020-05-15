def check_bill_id(bill_id):
    """ Check if bill match the bill id algorithm """
    j = 0
    sum_of_numbers = 0
    codes = [2, 3, 4, 5, 6, 7]
    if len(bill_id) <= 11:
        return False
    length = len(bill_id)
    i = length - 2
    while i >= 0:
        sum_of_numbers += int(bill_id[i]) * codes[j]
        if j < 5:
            j += 1
        else:
            j = 0
        i -= 1

    i = sum_of_numbers % 11
    if i > 1:
        i = 11 - i
    else:
        i = 0
    if int(bill_id[length - 1]) != i:
        return False
    return True
