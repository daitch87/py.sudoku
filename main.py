print("Hello, Python World!")
import os

# 1. 게임 보드 초기화 (0은 빈칸을 의미함)
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

def print_board(bo):
    """현재 스도쿠 판을 화면에 출력하는 함수"""
    # 화면을 깨끗하게 지워서 게임기처럼 보이게 함
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    print("\n    0 1 2   3 4 5   6 7 8 (열)")
    print("  -------------------------")
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("  |-------+-------+-------|")
        
        print(f"{i} |", end=" ") # 행 번호 출력
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            
            # 빈칸(0)은 점(.)으로 표시
            display_val = bo[i][j] if bo[i][j] != 0 else "."
            print(display_val, end=" ")
        print("|")
    print("  -------------------------")

def is_valid(bo, num, pos):
    """숫자가 스도쿠 규칙에 맞는지 검사하는 함수"""
    r, c = pos
    # 가로(행) 및 세로(열) 검사
    for i in range(9):
        if bo[r][i] == num or bo[i][c] == num:
            return False
    
    # 3x3 작은 박스 검사
    box_x, box_y = c // 3, r // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num:
                return False
    return True

def find_empty(bo):
    """아직 채워지지 않은 칸이 있는지 확인"""
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return True
    return False

def main():
    while find_empty(board):
        print_board(board)
        try:
            print("입력 예시 -> 0,2,4 (0행 2열에 숫자 4 입력)")
            user_input = input("행,열,숫자를 입력하세요 (종료: q): ")
            
            if user_input.lower() == 'q':
                print("게임을 종료합니다.")
                return

            # 입력받은 문자열을 숫자로 분리
            r, c, n = map(int, user_input.split(','))

            # 1. 범위 체크
            if not (0 <= r < 9 and 0 <= c < 9 and 1 <= n <= 9):
                input("\n⚠️ 범위 오류! 행/열은 0~8, 숫자는 1~9까지입니다. (Enter)")
                continue
            
            # 2. 빈칸 여부 체크
            if board[r][c] != 0:
                input("\n⚠️ 이미 숫자가 있는 칸입니다! (Enter)")
                continue

            # 3. 스도쿠 규칙 체크 및 채우기
            if is_valid(board, n, (r, c)):
                board[r][c] = n
            else:
                input(f"\n❌ 규칙 위반! {n}은 그 자리에 넣을 수 없습니다. (Enter)")

        except ValueError:
            input("\n⚠️ 형식이 틀렸습니다! '행,열,숫자' 형식으로 쉼표를 넣어주세요. (Enter)")

    print_board(board)
    print("\n🎉 축하합니다! 스도쿠를 모두 완료하셨습니다!")

if __name__ == "__main__":
    main()