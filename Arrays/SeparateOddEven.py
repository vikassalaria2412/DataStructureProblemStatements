def main():
    inputs = int(input())
    for ct in range(inputs):
        length = int(input())
        A = input().split(' ')
        odd = [int(val) for val in A if val and int(val)%2!=0]
        even = [int(val) for val in A if val and int(val)%2==0]
        for i in range(0, len(odd)):
            print(odd[i], end = ' ')
        print()
        for i in range(0, len(even)):
            print(even[i], end = ' ')
        print()
    return 0

if __name__ == '__main__':
    main()