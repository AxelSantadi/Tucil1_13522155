def baca_file(nama_file):
    with open(nama_file, 'r') as file:
        data = file.readlines()
    return data

def proses_data(data):
    buffer_size = int(data[0].strip())

    matrix_info = list(map(int, data[1].strip().split()))
    matrix_width = matrix_info[0]
    matrix_height = matrix_info[1]

    matrix = [list(map(str, line.strip().split())) for line in data[2:2+matrix_height]]

    num_sequences = int(data[8].strip())
    sequences = []
    rewards = []

    for i in range(num_sequences):
        sequences.append(data[2+matrix_height+1+i*2].strip())
        rewards.append((data[2+matrix_height+i*2+2].strip()))

    return buffer_size, matrix_width, matrix_height, matrix, num_sequences, sequences, rewards