
def natural_sum(last_number):
    if last_number < 1:
        return last_number

    total = 0
    for number in range(1, last_number+1):
        total += number

    return total

