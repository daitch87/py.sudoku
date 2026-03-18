import os

# 1. 초기 보드 설정 (0은 빈칸)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# 2. 판을 화면에 그리는 함수
def draw_board(b):
    # 터미널 화면을 깨끗하게 지워주는 명령어 (선택 사항)
    # os.system('cls' if os.name == 'nt' else 'clear') 
    
    print("\n==== 9x9 SUDOKU GAME ====")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 25)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            
            # 숫자가 0이면 빈칸(.)으로, 아니면 숫자로 출력
            val = b[i][j]
            print(val if val != 0 else ".", end=" ")
        print()
    print("=========================\n")

# 3. 규칙 검사 함수 (가로, 세로, 3x3 박스)
def can_place(b, r, c, n):
    # 가로/세로 검사
    for i in range(9):
        if b[r][i] == n or b[i][c] == n:
            return False
    # 3x3 박스 검사
    br, bc = (r // 3) * 3, (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if b[i][j] == n:
                return False
    return True

# 4. 실제 게임 루프
def main():
    while True:
        draw_board(board) # 현재 판을 보여줌
        
        try:
            print("입력 예시: 0 2 1 (0행 2열에 1 넣기)")
            user_input = input("행 열 숫자 입력 (종료: q): ")
            
            if user_input.lower() == 'q':
                break
                
            r, c, n = map(int, user_input.split())
            
            # 규칙 확인 후 판에 채워넣기
            if can_place(board, r, c, n):
                board[r][c] = n
                print(f"\n성공! {r},{c} 위치에 {n}을 넣었습니다.")
            else:
                print("\n❌ 규칙 위반! 그 자리에 그 숫자는 넣을 수 없어요.")
                
        except ValueError:
            print("\n⚠️ 숫자 세 개를 띄어쓰기로 입력해 주세요 (예: 0 2 1)")

if __name__ == "__main__":
    main()
