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
    oTrong = [i for i in range(9) if isinstance(luoi[i], int)]
    may = randint(0, len(oTrong) - 1)
    luoi[oTrong[may]] = 'o'
    print(f'Máy đánh ô: {oTrong[may]}')
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