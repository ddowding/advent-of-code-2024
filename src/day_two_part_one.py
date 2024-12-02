

def save_christmas_day_two(file_input):
    safe = 0
    for line in file_input.readlines():
        increasing = False
        decreasing = False
        unsafe_change = False
        line_numbers = line.split(' ')

        previous_number = False
        for number_str in line_numbers:
            print(number_str)
            number = int(number_str)
            if previous_number == False:
                previous_number = number
            else:
                if number > previous_number:
                    increasing = True
                else:
                    decreasing = True
                number_difference = abs(previous_number - number)
                if number_difference == 0 or number_difference > 3:
                    unsafe_change = True
                else:
                    print("saffeeee")
                previous_number = number
        if (increasing and decreasing) == False:
            if not unsafe_change:
                safe = safe + 1
    return safe

with open('./data/day_two_test_input.txt') as f:
    total_safe = save_christmas_day_two(f) 
    print('TOTAL SAFE should be 2 and is: ' + str(total_safe))
    assert(save_christmas_day_two, 2)

with open('./data/day_two_input.txt') as f:
    total_safe = save_christmas_day_two(f) 
    print('TOTAL SAFE is: ' + str(total_safe))