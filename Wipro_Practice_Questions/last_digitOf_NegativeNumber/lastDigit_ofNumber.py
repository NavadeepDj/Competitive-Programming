# Method 1: Using abs()
def last_digit(num):
    return abs(num) % 10

# Method 2: Without abs(), normalize remainder
def last_digit_no_abs(num):
    return ((num % 10) + 10) % 10

# Demo
test_cases = [123, -123, -10, 456, -19]

print("Python Results:")
for n in test_cases:
    print(f"{n} -> abs method: {last_digit(n)}, no-abs method: {last_digit_no_abs(n)}")
