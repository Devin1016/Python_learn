def add(x, y):
    if x < y:
        return x + add(x + 1, y)
    else:
        return y


def main():
    re = add(1, 100)
    print(re)


if __name__ == '__main__':
    main()
