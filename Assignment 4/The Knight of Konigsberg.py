import sys

def solve():  #for fast input
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])

    placed_knights = set()

    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    input_index = 3

    for _ in range(K):
        if input_index >= len(data):
            break
            
        x = int(data[input_index])
        y = int(data[input_index + 1])
        input_index += 2

        for dx, dy in knight_moves:
            nx = x + dx
            ny = y + dy


            if 1 <= nx <= N and 1 <= ny <= M:

                if (nx, ny) in placed_knights:
                    print("YES")
                    return
        
        placed_knights.add((x, y))

    print("NO")

if __name__ == "__main__":
    solve()