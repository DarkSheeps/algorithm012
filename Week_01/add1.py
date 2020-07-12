def plusOne(digits):
    int_dig = int(''.join(map(str, digits))) + 1
    return [int(i) for i in str(int_dig)]

if __name__ == '__main__':
    plusOne([1,2,9])