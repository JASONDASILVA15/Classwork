def main():
    words = []
    with open('dictionary.txt') as f:
        for line in f:
            words.append(line.strip())

    words.sort()
    print("APPLE" in words)
    print(words)


if __name__ == '__main__':
    main()
