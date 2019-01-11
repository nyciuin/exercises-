def divide(div):
    try:
        return 100 / div
    except Exception:
        print('nope')

print(divide(16))
print(divide(2))
print(divide(82))
print(divide(0))
