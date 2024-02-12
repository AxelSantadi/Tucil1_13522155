class Tucil:
    def __init__(self, buffer, row, col, jumlah_sequence, sequence_length, matriks, sequence, reward_sequence):
        self.buffer = buffer
        self.row = row
        self.col = col
        self.jumlah_sequence = jumlah_sequence
        self.sequence_length = sequence_length
        self.matriks = matriks
        self.sequence = sequence
        self.reward_sequence = reward_sequence

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

    num_sequences = int(data[2+matrix_height].strip())
    sequences = []
    rewards = []

    for i in range(num_sequences):
        sequences = [list(map(str, line.strip().split())) for line in data[3+matrix_height:3+matrix_height+(2*num_sequences):2]]
        rewards.append(int(data[2+matrix_height+i*2+2].strip()))
    sequence_length = max(len(seq) for seq in sequences)
    
    tucil = Tucil(buffer_size, matrix_width, matrix_height, num_sequences, sequence_length, matrix, sequences, rewards)

    return tucil