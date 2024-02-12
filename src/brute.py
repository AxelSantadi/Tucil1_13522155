max_reward = 0
max_route = []

class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def count_seq_length(tucil, idx):
    count = 0
    if idx < len(tucil.sequence):
        for i in range(min(tucil.sequence_length, len(tucil.sequence[idx]))):
            if tucil.sequence[idx][i] != "":
                count += 1
    return count

def count_score(tucil, temp):
    score = 0
    size = len(temp)
    for i in range(size):
        for j in range(tucil.jumlah_sequence):
            length = count_seq_length(tucil, j)
            if size - i >= length:
                count = 0
                for k in range(length):
                    if temp[i + k] == tucil.sequence[j][k]:
                        count += 1
                if count == length:
                    score += tucil.reward_sequence[j]
    if score == 0:
        score = -1
    return score

def same_sequence(route, betul):
    if len(route) != len(betul):
        return False
    else:
        for i in range(len(betul)):
            if route[i] != betul[i]:
                return False
        return True


global max_route_coordinates

def search_route(tucil, matrix, row, col, route, route_points, visited, buffer, is_vertical):
    global max_reward, max_route, max_route_coordinates
    route.append(matrix[row][col])
    route_points.append(Point(row, col))
    visited[row][col] = True
    temp_reward = count_score(tucil, route)
    if temp_reward > max_reward:
        max_reward = temp_reward
        max_route = list(route)
        max_route_coordinates = list(route_points)  # update max_route_coordinates here
    if len(route) == buffer:
        route.pop()
        route_points.pop()
        visited[row][col] = False
        return
    if is_vertical:
        for i in range(tucil.row):
            if not visited[i][col]:
                search_route(tucil, matrix, i, col, route, route_points, visited, buffer, not is_vertical)
    else:
        for j in range(tucil.col):
            if not visited[row][j]:
                search_route(tucil, matrix, row, j, route, route_points, visited, buffer, not is_vertical)
    route.pop()
    route_points.pop()
    visited[row][col] = False

def write_sequence_to_file(filename, max_route, max_reward, max_route_coordinates, execution_time):
    with open(filename, 'w') as f:
        # Write max_reward
        f.write(str(max_reward) + '\n')
        
        # Write max_route
        f.write(' '.join(max_route) + '\n')
        
        # Write max_route_coordinates
        for point in max_route_coordinates:
            f.write(f'{point.row + 1}, {point.col + 1}\n')

        f.write('\n')
        
        # Write execution time
        f.write(str(execution_time) + ' ms\n')