import sys


def main():
    input_filename = "hamstr.in" if len(sys.argv) == 1 else sys.argv[1]
    output_filename = "hamstr.out" if len(sys.argv) == 1 else sys.argv[2]

    #print read_input(input_filename)
    X, N, C, G = read_input(input_filename)
    result =  solve (X, C, G, N, max=N+1)
    #array, discount = read_input(input_filename)
    #total = solve(array, discount)
    write_output(output_filename, result)


def read_input(filename):
    with open(filename, "r") as input_file:
        X = int(input_file.readline())
        N = int(input_file.readline())
        C = []
        G = []
        for line in input_file:
            C.append(int(line.split()[0]))
            G.append(int(line.split()[1]))
        #array_str = input_file.readline()
        #array = [int(item) for item in array_str.split()]
        #discount = int(input_file.readline())
        return X, N, C, G


def solve1(array, discount):
    #print(X)
    #print(V)
    #print(C)
    #print(G)
    #return total
    pass

def qsort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = qsort(less)
        more = qsort(more)
        return less + pivotList + more

def calc_cost(A,B, k):
    y = [A[i]+(k-1)*B[i] for i in xrange(len(A))]
    return sum(qsort(y)[:k])


def solve (value, cost, greed, N, flag=0, min=0, max=0, count=0):

    if 2**(count-1)>=N:
        return flag
    else:
        count+=1
        M = max
        m = min
        pivot = (M+m)//2
        x = calc_cost(cost, greed, pivot)
        #print("pivot " , pivot)
        #print("Target ", value)
        #print("Calc val ", x)
        #print("Max ", M)
        #print("Min ", m)
        #print("Count ", count)
        #print("----------END---------")
        if x<=value:
            flag = pivot
            m = pivot
            return solve (value, cost, greed, N, flag, m, M, count)
        else:
            M = pivot
            return solve (value, cost, greed, N, flag, m , M, count)


def write_output(filename, total):
    with open(filename, "w") as output_file:
        output_file.write(str(total))

if __name__ == "__main__":
    main()



def countingSort(a, min, max):
    cnt = [0] * (max - min + 1)
    for x in a:
        cnt[x - min] = 1

    return [x for x, n in enumerate(cnt, start=min)
              for i in xrange(n)]