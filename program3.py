def generate_odd_series(a: int):
    count = a if a % 2 != 0 else a - 1  # Reduce by 1 if even
    series = [2 * i + 1 for i in range(count)]
    return series
  
a = int(input("Enter a number (a): "))
result = generate_odd_series(a)
print("Output:", ", ".join(map(str, result)))
