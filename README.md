# Tic-Tac-Toe
Tic-Tac-Toe (hay "Cờ ca-rô" 3x3) là một trò chơi hai người phổ biến, trong đó người chơi lần lượt đánh dấu "X" hoặc "O" vào một bảng 3x3. Mục tiêu là tạo được một hàng ngang, dọc hoặc chéo gồm ba ký hiệu giống nhau trước đối thủ.

# Cây trò chơi và tìm kiếm trên câu trò chơi 
## Cách xây dựng câu trò chơi 
- Gốc của cây ứng với trạng thái u
- Với trạng thái u, chúng ta có thể thực hiện các nước đi hợp lệ để tạo ra các trạng thái của nó

# Giải thuật minimax
**Nhận đinh**
- Giả sử đến một thời điểm đường đi đã dẫn đến đỉnh u
- Nước đi tối ưu cho trạng thái u là nước đi dẫn đến đỉnh con v (Tốt nhất trong tất cả cá đỉnh con của u)
- Để chọn nước đi tốt nhất cho trạng thái u ta cần xác định giá trị các đỉnh của cây trò chơi có gốc là u

**Các tính điểm cho các đỉnh trên cây trò chơi**
- Để xác định giá trị tại đỉnh có gốc là u, ta phải đi từ mức thấp nhất đến đỉnh u
- Cây nhị phân sẽ được phân thành các lớp Min - Max xen kẽ lẫn nhau
    - Lớp Min: Lấy giá trị nhỏ nhất của các node con
    - Lớp Max: Lấy giá trị lớn nhất của các node con

![image](https://github.com/user-attachments/assets/ce78321f-f2a1-41ee-88b8-86d902e6d08d)

**Giải thuật minimax với trò chơi cờ ca-ro**
![image](https://github.com/user-attachments/assets/217692f1-4eac-4b02-a136-be70e6ef1a15)




