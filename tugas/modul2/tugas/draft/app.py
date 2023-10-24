# nah ini harus di import dulu randomnya, biar nanti bisa dipake fungsi randomnya ke python
import random 

def create_board(width, default_char='-'):
    # jadi ini buat bikin board nya pake simbol dash (-)
    # saranku nanti km ganti aja namanya jangan default_char atau width, kek kurang manusiawi aja menurutku 
    # namanya hehe, tp terserah siii kalo aku pengen ku ganti nanti
    board = [[default_char for _ in range(width)] for _ in range(width)]
    return board

# width ini buat ukuran board nya
def generate_random_position(width):
    while True:
        # row ini kek di web buat yang kesamping dan col buat atas bawahnya
        # di ukur dari width yang tadi, di jadiin parameter, trs kenapa kok di kasih minus 1
        # karena value yang di input user harus di minus -1 biar random nya ga berlebih board nya
        # pake fungsi random. ini bawaan dari pythonnya, buat ngebikin angka randaom 0 - angka yang di input user
        row = random.randint(0, width - 1)
        col = random.randint(0, width - 1)
        yield (row, col)

def place_piece(board, row, col, piece_char):
    # Menempatkan bidak pada posisi yang ditentukan
    # nah ini yang agak ribet, jadi si if nya itu ngedetect dulu panjang nya board itu segimana, trs baru dia nanti 
    # nempatin harus kemana parameter piece_char nya nanti, bisa A atau O tergatung parameternya 
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        board[row][col] = piece_char
    else:
        print("Posisi di luar batas board.")

def print_board(board):
    # di looping sebanyak parameter board nya
    for row in board:
        # kenapa kok string kosong, karena buat jaran board nya
        print(' '.join(row))

def move_piece(board, position, move_direction):
    # Fungsi ini akan memindahkan bidak ke arah yang ditentukan
    row, col = position
    new_row, new_col = row, col

    # pas klik w ini kenapa kok row > 0 karena buat limit board nya, jadi kalo udah mentok ke atas ga bisa klik w nya lagi
    # begitu juga yang a
    if move_direction == 'w' and row > 0 and board[row - 1][col] != '#':
        new_row = row - 1
    elif move_direction == 's' and row < len(board) - 1 and board[row + 1][col] != '#':
        new_row = row + 1
    elif move_direction == 'a' and col > 0 and board[row][col - 1] != '#':
        new_col = col - 1
    elif move_direction == 'd' and col < len(board[0]) - 1 and board[row][col + 1] != '#':
        new_col = col + 1

    if (new_row, new_col) != (row, col):
        board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
        return new_row, new_col
    else:
        return row, col

def main():
    # Input lebar dari pengguna
    # harusnya int biar ga bisa terima string, jadi nanti ga error boardnya
    width = int(input("Masukkan lebar board: "))

    # Membuat board sesuai dengan inputan, mengisi dengan karakter '-'
    board = create_board(width)

    # Membuat generator posisi awal bidak dan tujuan bidak secara acak
    position_generator = generate_random_position(width)
    start_row, start_col = next(position_generator)
    # goal nya ini di set random juga, tapi posisinya sama kek simbol O
    goal_row, goal_col = next(position_generator)

    # Menempatkan bidak (simbol 'A') pada posisi awal yang dihasilkan secara acak
    # nah ini dia parameternya, jadiA ini buat simbol nya sama juga yang O
    # ini udah di tentuin dari kode nya, jadi kalo mau ganti simbol ya harus ganti bagian ini
    place_piece(board, start_row, start_col, 'A')

    # Menempatkan tujuan bidak (simbol 'O') pada posisi yang dihasilkan secara acak
    # nah ini simbol 0 nya, jadi lokasi goal nya di set jadi simbol O 
    place_piece(board, goal_row, goal_col, 'O')

    print("Selamat datang dalam permainan!")
    print_board(board)

    while True:
        move_direction = input("Masukkan arah pergerakan (w/a/s/d) atau 'q' untuk keluar: ").lower()

        if move_direction == 'q':
            print("Anda keluar dari permainan.")
            break

        # ini buat kek if else kalo inputnnya bener, harus wasd, kalo selain itu ga bisa
        if move_direction not in ['w', 'a', 's', 'd']:
            print("Arah pergerakan tidak valid. Harap masukkan arah yang benar.")
            continue

                # inputan mu tadi bakal masuk ke move_direction trs bakal masuk ke move_piece diatas
        start_row, start_col = move_piece(board, (start_row, start_col), move_direction)
        print_board(board)

        # nah taunya bisa menang gimana? kalo lokasi A nya sama kek lokasi O nya jadi menang dehh
        if (start_row, start_col) == (goal_row, goal_col):
            print("Selamat! Anda menang!")
            break

if __name__ == "__main__":
    main()