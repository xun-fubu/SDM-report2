#!/usr/bin/python3

def calc(A, B):
    # 型チェック（int 以外は不正）
    if not isinstance(A, int) or not isinstance(B, int):
        return -1

    # 値チェック（正の整数のみ許可）
    if A <= 0 or B <= 0:
        return -1

    return A * B


def main():
    while True:
        A = input('input A (end to quit): ')
        if A == 'end':
            break
        B = input('input B: ')

        try:
            A = int(A)
            B = int(B)
        except ValueError:
            print('input A * input B = ', -1)
            continue

        print('input A * input B = ', calc(A, B))


if __name__ == '__main__':
    main()
