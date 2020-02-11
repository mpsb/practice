if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)
    max_v = max(arr_list)

    print(max([i for i in arr_list if i != max_v]))