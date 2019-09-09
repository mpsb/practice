def find_nb(m):
    if(m==1):
        return 1
    else:
        volume = 0
        n = 1
        while volume < m:
            volume = volume + n**3
            if(volume == m):
                return n
            n += 1
        return -1