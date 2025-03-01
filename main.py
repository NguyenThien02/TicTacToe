from random import randint


luoi = [0,1,2,3,4,5,6,7,8]

def InLuoi():
    for i in range(0,9,3):
        print(luoi[i], '|', luoi[i+1], '|', luoi[i+2])
        print('---------')

def Trong():
    for i in luoi:
        if i != 'x' and i != 'o':
            return True
    return False

def NguoiChon():
    nguoi = int(input('Bạn chọn ô nào: '))
    if luoi[nguoi] == 'x' or luoi[nguoi] == 'o':
        print(f'Ô này đã được chọn: {luoi[nguoi]}')
        nguoi = int(input('Vui lòng chọn lại: '))
    else:
        luoi[nguoi] = 'x'
    InLuoi()

def MayChon():
    best_select = -float('inf')
    best_move = None
    for i in range(9):
        if(isinstance(luoi[i], int)):
            luoi[i] = 'o'
            select = Minimax(luoi, 0, False)
            luoi[i] = i
            if select > best_select:
                best_select = select
                best_move = i
    if(best_move is not None):
        luoi[best_move] = 'o'
        print(f'Máy đánh ô: {best_move}')
        InLuoi()

def KiemTraThang():
    thang = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Hàng ngang
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cột dọc
        [0, 4, 8], [2, 4, 6]  # Đường chéo
    ]
    for line in thang:
        if(luoi[line[0]] == luoi[line[1]] == luoi[line[2]] ):
            return luoi[line[0]]
    return None

def Minimax(board, depth, is_maximizing):
    winner = KiemTraThang()
    if(winner == '0'):
        return 1
    elif (winner == 'x'):
        return -1
    elif not Trong():
        return 0

    if is_maximizing:
        best_select = -float('inf')
        for i in range(9):
            if (isinstance(board[i], int)):
                board[i] = 'o'
                select = Minimax(board, depth + 1, False)
                board[i] = i
                best_select = max(select, best_select)
        return best_select
    else:
        best_select = float('inf')
        for i in range(9):
            if(isinstance(board[i], int)):
                board[i] = 'x'
                select = Minimax(board, depth + 1, True)
                board[i] = i
                best_select = min(select, best_select)
        return best_select

InLuoi()
while(Trong()):
    NguoiChon()
    if KiemTraThang() == 'x':
        print('Chúc mừng! Bạn đã thắng!')
        break
    if not Trong():
        print("Trò chơi hòa!")
        break
    MayChon()
    if KiemTraThang() == 'o':
        print("Máy đã thắng! Bạn thua cuộc!")
        break
    if not Trong():
        print("Trò chơi hòa!")
        break
    print('============================')