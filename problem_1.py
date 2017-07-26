"""
10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.

1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
"""

total = 0

for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        total += number

print(total)