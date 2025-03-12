from random import randint
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)
luoi = list(range(9))

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
        return best_move

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    nguoi = data.get('position')

    if isinstance(luoi[nguoi], int):
        luoi[nguoi] = 'x'

        if(KiemTraThang() == 'x'):
            return jsonify({'board': luoi, 'message': 'Bạn đã thắng!', 'winner': 'x'})

        if not Trong():
            return jsonify({'board': luoi, 'message': 'Trò chơi hòa!', 'winner': 'draw'})

        may_move = MayChon()

        if KiemTraThang() == 'o':
            return jsonify({'board': luoi, 'message': 'Máy đã thắng!', 'winner': 'o'})

        return jsonify({'board': luoi, 'message': f'Máy đánh ô: {may_move}', 'winner': None})

    return jsonify({'board': luoi, 'message': 'Ô này đã được chọn, vui lòng chọn ô khác.', 'winner': None})

@app.route('/reset', methods=['POST'])
def reset():
    global luoi
    luoi = list(range(9))
    return jsonify({'board': luoi, 'message': 'Ván mới đã bắt đầu!'})

if __name__ == '__main__':
    app.run(debug=True)