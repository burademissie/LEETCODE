if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    x=max(arr)
    y=arr.count(x)
    for i in range(y):
        arr.remove(x)
    print (max(arr))
