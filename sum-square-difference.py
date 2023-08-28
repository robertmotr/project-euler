def find_difference(n: int) -> int:
    squared_sum = 0
    sum = 0
    for i in range(1, n + 1):
        squared_sum += i**2
        sum += i
    return sum**2 - squared_sum

print(find_difference(100))