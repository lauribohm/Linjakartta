routes = {'A': ['B', 'C', 'D'],
         'B': ['A', 'D'],
         'C': ['A', 'D', 'E'],
         'D': ['A', 'B', 'C', 'E', 'R'],
         'E': ['C', 'D', 'F', 'M'],
         'F': ['E', 'G'],
         'G': ['F', 'H', 'I', 'K'],
         'H': ['G', 'I'],
         'I': ['G', 'H', 'J'],
         'J': ['I'],
         'K': ['G', 'L'],
         'L': ['K', 'M'],
         'M': ['E', 'N'],
         'N': ['M', 'O', 'Q', 'R'],
         'O': ['N', 'P', 'Q'],
         'P': ['O', 'Q'],
         'Q': ['N', 'O', 'P', 'R'],
         'R': ['D', 'N', 'Q']}

times = [['AB', 3], ['BD', 2], ['DA', 1], ['AC', 1], ['CD', 5], ['CE', 2], ['ED', 3], ['EF', 1], ['FG', 1], ['GH', 2],
         ['BA', 3], ['DB', 2], ['AD', 1], ['CA', 1], ['DC', 5], ['EC', 2], ['DE', 3], ['FE', 1], ['GF', 1], ['HG', 2],
         ['HI', 2], ['IJ', 1], ['IG', 1], ['GK', 8], ['KL', 1], ['LM', 1], ['EM', 10], ['MN', 2], ['NO', 2], ['OP', 2],
         ['IH', 2], ['JI', 1], ['GI', 1], ['KG', 8], ['LK', 1], ['ML', 1], ['ME', 10], ['NM', 2], ['ON', 2], ['PO', 2],
         ['OQ', 1], ['PQ', 2], ['NQ', 1], ['QR', 5], ['RN', 3], ['DR', 6],
         ['QO', 1], ['QP', 2], ['QN', 1], ['RQ', 5], ['NR', 3], ['RD', 6]]

yellow = ['EF', 'FG', 'GK', 'KL', 'LM', 'MN', 'FE', 'GF', 'KG', 'LK', 'ML', 'NM']
red = ['CD', 'DR', 'RQ', 'QN', 'NO', 'OP','DC', 'RD', 'QR', 'NQ', 'ON', 'PO']
green = ['DB', 'BA', 'AC', 'CE', 'EF', 'FG', 'GH', 'HI', 'IJ', 'BD', 'AB', 'CA', 'EC', 'FE', 'GF', 'HG', 'IH', 'JI']
blue = ['DE', 'EM', 'MN', 'NO', 'ED', 'ME', 'NM', 'ON']


def find_paths(routes, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in routes:
        return []
    paths = []
    for stop in routes[start]:
        if stop not in path:
            new_paths = find_paths(routes, stop, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def calculate_time(paths):
    total_paths = []
    all_times = []
    for path in paths:
        one_path = []
        time = 0
        for i in range(len(path)-1):
            one_path.append(path[i]+path[i+1])
        for stop in one_path:
            for t in times:
                if stop == t[0]:
                    time = time+t[1]
        total_paths.append(one_path)
        all_times.append(time)
    return(total_paths, all_times)

def check_if_lines(paths, times):
    final_paths = []
    final_times = []
    path_id = 0
    
    for path in paths:
        count = 0
        for route in path:
            if route not in yellow and route not in red and route not in green and route not in blue:
                count=count+1
                
        if count == 0:
            final_paths.append(path)
            final_times.append(times[path_id])

        path_id = path_id+1

    return(final_paths, final_times)

def find_shortest_path(paths):
    shortest = ''
    min_time = 99999999999
    for i in range(len(paths)):
        value = paths[i]
        if value<min_time:
            min_time = value
            shortest = i
    return(shortest)

def used_lines(paths):
    line_list = []
    for path in paths:
        if path in yellow:
            line_list.append("yellow")
        elif path in red:
            line_list.append("red")
        elif path in green:
            line_list.append("green")
        elif path in blue:
            line_list.append("blue")
    return(line_list)
            


def main():
    paths = find_paths(routes, 'A', 'P')
    complete_paths, time_taken = calculate_time(paths)
    final_paths, final_time_taken = check_if_lines(complete_paths, time_taken)
    shortest = find_shortest_path(final_time_taken)
    line_list = used_lines(final_paths[shortest])
    
    ##print(paths)
    ##print(complete_paths)
    ##print(complete_paths[shortest])
    print("Fastest path: " + str(final_paths[shortest]))
    print("Used lines: " + str(line_list))
    print("Time taken: " + str(final_time_taken[shortest]))
    

main()
