


def part_01():
    f = open("./primes.txt")
    f1 = f.readlines()
    n = 0
    value = [0 for i in range(10)]

    for x in f1:

        value[ int(x[-2]) ] += 1
        n += 1

    value = [ round(100 * x / n) for x in value]
    print(value)



def part_02():
    f = open("./primes.txt")
    f1 = f.readlines()
    n = 0

    value = [[0 for i in range(10)] for i in range(10)]
    x = f1.pop(0)

    previous_digit = int(x[-2])
    print(previous_digit)

    for x in f1:
        new_digit = int(x[-2])
        value[previous_digit][ new_digit ] += 1

        n += 1
        previous_digit = new_digit

    value = [ [round(100 * j / sum(i) ) if sum(i)>0 else 0 for j in i ] for i in value]

    for i in value :
        print(i)



def main():
    part_02()



if __name__ == "__main__":
    main()