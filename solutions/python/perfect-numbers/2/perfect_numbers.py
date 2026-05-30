def classify(number):
    if not isinstance(number, int):
        raise ValueError("Classification is only possible for positive integers.")
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0
    for i in range(1, number):
        if number % i == 0 and number !=i:
            aliquot_sum += i
            
    if number == aliquot_sum:
        return "perfect"
    elif number < aliquot_sum:
        return "abundant"
    else:
        return "deficient"