l, r = map(int, input().split())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_nums(l, r):
    count = 0
    for num in range(l, r + 1):
        if not is_prime(num) and num != 1:
            if is_prime(count_divs(num)):
                count += 1
    return count

def count_divs(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2
    if int(n**0.5)**2 == n:
        count = count - 1
    return count

print(count_nums(l, r))