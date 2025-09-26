````markdown
# Understanding Python Modulo with Negative Numbers

This repository is my notes and exploration of how Python calculates the remainder (`%`) and why some test cases failed when I tried to get the last digit of a number.

---

## Problem

I wanted to get the **last digit** of a number:

```python
def last_digit(input1):
    return input1 % 10
````

It worked for positive numbers ✅, but failed for negative numbers ❌.
For example:

```python
print(-123 % 10)   # Output: 7
```

Expected last digit: **3**, but Python gave **7**.

---

## Why does this happen?

In Python:

```
a = b * q + r
```

* `a` = dividend
* `b` = divisor
* `q = floor(a/b)` (quotient is floored, not truncated)
* `r = a - b*q` (remainder)

👉 The remainder `r` **always has the same sign as the divisor `b`**.

### Example: `a = -123, b = 10`

```
-123 / 10 = -12.3
floor(-12.3) = -13
q = -13
r = -123 - (10 * -13) = -123 + 130 = 7
```
## Basically, if we are dividing: Dividend with a divisor, we do it such that we are subracting less nymber coompared to dividend; 
### What I mean is, it is not a problem with positive numbers...Ex: 123/10 -> 10* 12 + 3 (here we gave 12*10 = 120 < 123) and remainder is teh last dugut of teh dividend;

### But when it came to teh negative numbers, like -123/10 -> -12 * 10 (we cant do this since 120 is greater than -123)
### so, we gotta do -13 * 10 + 7 = -123; But remainder 7 is not equal to the last digit of the number; SO, we definetly have to turn it into postive number using abs() or simple if loop; So after converting, we can do as same as we do for postive numbers
So:

```python
-123 % 10 == 7
```

Check: `-123 == 10 * (-13) + 7 ✅`

But if we want the **last digit**, this is not what we want.

---

## Fix: Using `abs()`

```python
def last_digit(input1):
    return abs(input1) % 10
```

Now:

```python
print(last_digit(123))   # 3
print(last_digit(-123))  # 3
print(last_digit(-10))   # 0
```

Works for all cases 🎉

---

## Alternative Without `abs()`

If `abs()` is not allowed, we can normalize the remainder:

```python
def last_digit(input1):
    return ((input1 % 10) + 10) % 10
```

This trick ensures the result is always between `0..9`.

---

## Key Insights

* Python uses **floor division** when calculating quotient and remainder.
* Formula: `a = b*q + r` with `r` having the **same sign as divisor**.
* This differs from some languages (like C or Java before Java 8), which use truncation toward zero, where remainder has the same sign as the dividend.
* For “last digit” tasks, always take `abs()` first.

---

## Quick Demo Script

```python
def last_digit(input1):
    return abs(input1) % 10

test_cases = [123, -123, -10, 456, -19]

for num in test_cases:
    print(f"{num} -> last digit: {last_digit(num)}")
```

**Output:**

```
123 -> 3
-123 -> 3
-10 -> 0
456 -> 6
-19 -> 9
```

---

## Extra Check with `divmod()`

```python
for a, b in [(123,10), (-123,10), (-10,10), (7,-3), (-7,-3)]:
    q, r = divmod(a, b)
    print(f"a={a}, b={b} => q={q}, r={r} | check: {b}*{q}+{r} = {a}")
```

This shows how Python keeps `r` with the sign of divisor.

---

```

---

Would you like me to also **add a small table of examples (like -123, -10, 7, -7, etc.)** inside the README so you can visually see how `%` behaves in Python?
```
