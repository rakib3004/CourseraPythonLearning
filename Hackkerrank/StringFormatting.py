def print_formatted(number):

    for i in range(1,number+1):
        a=i
        b = oct(i)[2:]
        c = format(i,"X")
        d = bin(i)[2:]
        print(a,' ',b,' ',c,' ',d)




if __name__ == '__main__':
    n = int(input())
    print_formatted(n)