
def append_distances(data_line, data_lists):
    data_split = data_line.split('   ')
    dist_a = data_split[0]
    dist_b = data_split[1]
    data_lists['list_a'].append(int(dist_a))
    data_lists['list_b'].append(int(dist_b))
    return data_lists

def sort_lists(data_lists):
    data_lists['list_a'] = sorted(data_lists['list_a'])
    data_lists['list_b'] = sorted(data_lists['list_b'])
    return data_lists

def calculate_distances(data_lists):
    for i in range(len(data_lists['list_a'])):
        data_lists['differences'].append(abs((data_lists['list_a'][i]) - (data_lists['list_b'][i])))
    return data_lists

def calc_sim_score(data_lists):
    for i in range(len(data_lists['list_a'])):
        data_lists['sim_score'].append(data_lists['list_a'][i] * data_lists['list_b'].count(data_lists['list_a'][i]))
    return sum(data_lists['sim_score'])

def save_christmas_day_one(file_input):
    data_lists = { 'list_a': [], 'list_b': [], 'differences': [] }
    for line in file_input.readlines():
        data_lists = append_distances(line, data_lists)
    data_lists = sort_lists(data_lists)
    data_lists = calculate_distances(data_lists)
    return(sum(data_lists['differences']))

def save_christmas_day_one_p2(file_input):
    # multiply the number in the left list by the number of times seen in right list
    data_lists = { 'list_a': [], 'list_b': [], 'sim_score': [] }
    for line in file_input.readlines():
        data_lists = append_distances(line, data_lists)
    return calc_sim_score(data_lists)

with open('./data/day_one_test_input.txt') as f:
    total_distance_ordered = save_christmas_day_one(f) 
    print('TOTAL DISTANCE for test should be 11 and result is: ' + str(total_distance_ordered))
    assert(save_christmas_day_one, 11)

with open('./data/day_one_test_input.txt') as f:
    total_sim_score = save_christmas_day_one_p2(f)
    print('TOTAL simscore for test should be 31 and result is: ' + str(total_sim_score))

with open('./data/day_one_input.txt') as f:
    total_distance_ordered = save_christmas_day_one(f) 
    print('TOTAL DISTANCE ' + str(total_distance_ordered))

with open('./data/day_one_input.txt') as f:
    total_sim_score = save_christmas_day_one_p2(f)
    print('TOTAL SIM SCORE ' + str(total_sim_score))
