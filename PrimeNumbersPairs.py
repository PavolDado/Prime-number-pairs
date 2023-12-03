def prime(number):
    #finds prime numbers
    tmp = [i for i in range(1, number + 1) if number % i == 0]
    return not len(tmp) > 2


def prime_nums_list(start, stop):
    # create list of prime numbers
    tmp_list = [a for a in range(start, stop + 1) if prime(a)]
    return tmp_list


def pairs(start, stop, diference):
    '''
    returns array of prime numbers pairs,
    with specific diference between numbers
    '''
    final_list = []
    tmp_number = 0
    for b in prime_nums_list(start, stop):
        if b - tmp_number == diference:
            append_num = (tmp_number, b)
            final_list.append(append_num)
        tmp_number = b
    return final_list
