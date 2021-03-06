mem = {}

def ans(x, mem):
    count = 0
    if x in mem:
        return mem[x]
    if x == 1:
        return 1
    src = x
    if x % 2 != 0:
        x = 3*x+1
    else:
        x = x//2
    count = ans(x, mem)+1
    mem[src] = count
    return count

while True:
    try: 
        n = input().split()
        i = int(n[0])
        j = int(n[1])
        st = -1
        end = -1
        if i > j:
            st = j
            end = i
        else:
            st = i
            end = j
        maxlen = 0
        for n in range(st, end+1):
            #maxlen = max(maxlen, ans(n, mem))
            count = 1
            src = n
            while n != 1:
                if n in mem:
                    count += mem[n]
                    break
                else:
                    count = count+1
                    
                if n % 2 != 0:
                    n = 3*n+1
                else:
                    n = n//2
                    
            mem[src] = count
            maxlen = max(maxlen, count)
        print(i, j, maxlen)
    except EOFError:
        break