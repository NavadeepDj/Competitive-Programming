````markdown
# 🧮 Count Primes — LeetCode #204

This repository documents my step-by-step journey solving the **Count Primes** problem from [LeetCode 204](https://leetcode.com/problems/count-primes/).  
The goal:  
> Given an integer `n`, return the number of prime numbers **strictly less than** `n`.

I started with a naive brute-force approach and gradually optimized the solution, analyzing time complexity and identifying bottlenecks at each stage — finally reaching a fast, accepted version using the **Sieve of Eratosthenes**.

---

## 🧩 Problem Statement

```text
Input: n = 10
Output: 4
Explanation: There are 4 primes less than 10 — [2, 3, 5, 7]
````

---

## 🚶 Step 1 – Brute-Force Method

### **Idea**

Check every number `i` from 2 to `n − 1`
→ for each `i`, test divisibility by every smaller number.

```python
def countPrimes(self, n: int) -> int:
    if n <= 2:
        return 0
    count = 0
    for i in range(2, n):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            count += 1
    return count
```

### **Issues**

* Nested loops for each `i` → **O(n²)** time.
* Works for small `n` (e.g. 1000) but **times out** for large inputs (>10⁵).

### **Result**

❌ **Time Limit Exceeded (TLE)** on LeetCode.

---

## ⚙️ Step 2 – Square-Root Optimization

### **Idea**

We don’t need to check all divisors up to `i − 1`.
If `i` is divisible by a number greater than √i, the complementary factor is already checked.

```python
def countPrimes(self, n: int) -> int:
    if n <= 2:
        return 0
    count = 0
    for i in range(2, n):
        isPrime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            count += 1
    return count
```

### **Complexity**

* **Time:** O(n√n)
* **Space:** O(1)

### **Issues**

* Much faster, but still ~10¹⁰ operations for n = 5,000,000.
* ❌ Still **TLE**.

---

## ⚡ Step 3 – Skip Even Numbers

### **Idea**

All even numbers except 2 are non-prime.
Only iterate odd numbers and test odd divisors.

```python
def countPrimes(self, n: int) -> int:
    if n <= 2:
        return 0
    count = 1  # count '2' as prime
    for i in range(3, n, 2):
        isPrime = True
        j = 3
        while j * j <= i:
            if i % j == 0:
                isPrime = False
                break
            j += 2
        if isPrime:
            count += 1
    return count
```

### **Complexity**

* **Time:** ≈ O((n/2)√n) → ~O(n√n)
* **Space:** O(1)

### **Issues**

* Skips half the checks but still far too slow for millions.
* ❌ **TLE** at n ≈ 5 × 10⁵.

---

## 🧠 Step 4 – The Sieve of Eratosthenes (Optimized and Accepted)

### **Idea**

Instead of testing every number individually,
mark all multiples of each prime as **non-prime** in a boolean list.

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)
```

### **Complexity**

* **Time:** O(n log log n)
* **Space:** O(n)

### **Why It Works**

Each composite number is crossed out only once per prime factor,
making the algorithm nearly linear in n.

### **Result**

✅ **Accepted** on LeetCode for n up to 5 × 10⁶.

---

## 🧩 Step 5 – Bitwise Sieve (Extra Optimization)

Further reduce memory and skip evens by using a `bytearray`.

```python
def countPrimes(self, n: int) -> int:
    if n < 3:
        return 0
    sieve = bytearray(b'\x01') * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = b'\x00' * ((n - i * i - 1) // (2 * i) + 1)
    return sum(sieve)
```

### **Complexity**

* **Time:** O(n log log n)
* **Space:** ≈ O(n / 2)

### **Notes**

* Only stores odd numbers in memory.
* ~2× faster and uses half the space of the normal sieve.
* Fastest pure-Python version.

---

## 📈 Summary Table

| Step | Approach              | Time Complexity | Space    | LeetCode Status | Notes               |
| ---- | --------------------- | --------------- | -------- | --------------- | ------------------- |
| 1    | Brute-Force           | O(n²)           | O(1)     | ❌ TLE           | Checks all divisors |
| 2    | √i Check              | O(n√n)          | O(1)     | ❌ TLE           | Stops at √i         |
| 3    | Skip Evens            | O(n√n / 2)      | O(1)     | ❌ TLE           | Odd numbers only    |
| 4    | Sieve of Eratosthenes | O(n log log n)  | O(n)     | ✅ Accepted      | Marks multiples     |
| 5    | Bitwise Sieve         | O(n log log n)  | O(n / 2) | ✅ Fastest       | Odd-only sieve      |

---

## 🏁 Conclusion

Starting from the brute-force approach, each iteration improved efficiency:

* **Brute-force:** too many redundant checks.
* **√i optimization:** reduced checks but still quadratic-like.
* **Odd skipping:** half the work, but still too slow.
* **Sieve of Eratosthenes:** the breakthrough — nearly linear performance.
* **Bitwise sieve:** fine-tuned version for Python performance.

This progression demonstrates how algorithmic thinking and complexity analysis
transform an unscalable idea into an efficient, production-ready solution.

---

## 📚 References

* [LeetCode 204 – Count Primes](https://leetcode.com/problems/count-primes/)
* [Wikipedia: Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
* [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

