# itertools模块
# itertools模块提供了多个有用的迭代器函数，例如count(), cycle(), repeat()等。
import itertools

print("itertools.count:")
for i in itertools.count(10):
    if i > 15:
        break
    print(i, end=' ')

print("\nitertools.cycle:")
count = 0
for i in itertools.cycle('AB'):
    if count >= 6:
        break
    print(i, end=' ')
    count += 1

print("\nitertools.repeat:")
for i in itertools.repeat('Hello', 3):
    print(i, end=' ')