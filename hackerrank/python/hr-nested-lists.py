if __name__ == '__main__':
    ls = []
    min_score = 0

    for i,e in enumerate(range(int(input()))):
        name = input()
        score = float(input())
        if i == 0:
            min_score = score
        elif score < min_score:
            min_score = score
        ls.append([name, score])

    ls = [[i[0], i[1]] for i in ls if i[1] != min_score]

    min_score = min([i[1] for i in ls])

    ls = [i[0] for i in ls if i[1] == min_score]
    
    for i in sorted(ls):
        print(i)