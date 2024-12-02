
def proccess_changes(line_numbers, increasing, decreasing, saftey_hazard):
    counter = 0
    for number_str in line_numbers:
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
        if (increasing and decreasing) and unsafe_change:
            saftey_hazard = True
            pr
        counter = counter + 1

def save_christmas_day_two_damper(file_input):
    safe = 0
    for line in file_input.readlines():
        increasing = False
        decreasing = False
        unsafe_change = False
        saftey_hazard = False
        line_numbers = line.split(' ')

        previous_number = False
        previous_number_mem = False

        proccess_changes(line, increasing, decreasing, saftey_hazard)

        if (increasing and decreasing) == False:
            if not unsafe_change:
                safe = safe + 1
    return safe

with open('./data/day_two_test_input.txt') as f:
    total_safe = save_christmas_day_two_damper(f) 
    print('TOTAL SAFE should be 4 and is: ' + str(total_safe))
    assert(total_safe, 4)

with open('./data/day_two_input.txt') as f:
    total_safe = save_christmas_day_two_damper(f) 
    print('TOTAL SAFE is: ' + str(total_safe))