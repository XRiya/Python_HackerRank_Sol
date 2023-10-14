
def create_door_mat(N, M):
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    welcome = 'WELCOME'.center(M, '-')
    door_mat = '\n'.join(pattern + [welcome] + pattern[::-1])
    print(door_mat)

if __name__ == "__main__":
    N, M = map(int, input().split())
    create_door_mat(N, M)
