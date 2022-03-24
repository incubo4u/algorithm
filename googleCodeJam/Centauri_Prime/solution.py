# TODO: Complete the get_ruler function
volwes = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}


def get_ruler(kingdom):
    if kingdom[-1] == 'Y' or kingdom[-1] == 'y':
        return 'nobody'
    if kingdom[-1] in volwes:
        return 'Alice'
    return 'Bob'


def main():
    T = int(input())
    for t in range(T):
        kingdom = input()
        print('Case #%d: %s is ruled by %s.' %
              (t + 1, kingdom, get_ruler(kingdom)))


if __name__ == '__main__':
    main()
