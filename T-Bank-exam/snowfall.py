def check_snow_log(n, snow_depths):

    snowfall = [1] * n 

    for i in range(n):
        if snow_depths[i] != -1:
            if snow_depths[i] < sum(snowfall[:i]):
                return "NO" 
            snowfall[i] = snow_depths[i] - sum(snowfall[:i])

    return "YES\n" + " ".join(map(str, snowfall))

n = int(input())
snow_depths = list(map(int, input().split()))

print(check_snow_log(n, snow_depths))