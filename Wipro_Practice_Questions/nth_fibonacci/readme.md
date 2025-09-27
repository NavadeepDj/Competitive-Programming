# Fibonacci Numbers – Recursion & Dynamic Programming

## 📌 Problem Statement

Compute the **Nth Fibonacci number**. The Fibonacci sequence is defined as:

```
F(1) = 0
F(2) = 1
F(n) = F(n-1) + F(n-2), for n ≥ 3
```

The goal is to understand **recursive computation**, analyze its behavior, and explore **Dynamic Programming (DP)** as a more efficient alternative.

---

## 💻 Recursive Approach

### Code

```java
public static int fibRecursive(int n) {
    if (n <= 1) return n;  // Base case
    return fibRecursive(n - 1) + fibRecursive(n - 2); // Recursive case
}
```

---

### How It Works

1. **Base Case**

   ```java
   if (n <= 1) return n;
   ```

   * Stops recursion.
   * Returns known values:

     * `fib(1) = 0`
     * `fib(2) = 1`

2. **Recursive Case**

   ```java
   return fibRecursive(n - 1) + fibRecursive(n - 2);
   ```

   * Breaks the problem into two smaller subproblems (`n-1` and `n-2`).
   * Each call waits for its child calls to finish, then adds their results.

---

### Step-by-Step Example (fib(5))

Here’s how the recursion **stack builds and unwinds**:

#### Call Stack Execution

1. **Initial Call:** `fibRecursive(5)` → not base case → compute `fib(4) + fib(3)`
   **Stack:** `[fib(5)]`

2. **Call:** `fibRecursive(4)` → compute `fib(3) + fib(2)`
   **Stack:** `[fib(4), fib(5)]`

3. **Call:** `fibRecursive(3)` → compute `fib(2) + fib(1)`
   **Stack:** `[fib(3), fib(4), fib(5)]`

4. **Call:** `fibRecursive(2)` → not base case → compute `fib(1) + fib(0)`
   **Stack:** `[fib(2), fib(3), fib(4), fib(5)]`

5. **Call:** `fibRecursive(1)` → base case → return `1`
   **Stack unwinds one level** → back to `fib(2)`

6. **Call:** `fibRecursive(0)` → base case → return `0`
   **fib(2) = 1 + 0 = 1`**   **Stack unwinds** → back to `fib(3)`

7. **Call:** `fibRecursive(1)` → base case → return `1`
   **fib(3) = fib(2) + fib(1) = 1 + 1 = 2`**   **Stack unwinds** → back to `fib(4)`

8. **Call:** `fibRecursive(2)` → compute `fib(1) + fib(0)`

   * `fib(1) = 1`
   * `fib(0) = 0`
     **fib(2) = 1 + 0 = 1`**   **Stack unwinds** → back to `fib(4)`

9. **fib(4) = fib(3) + fib(2) = 2 + 1 = 3`**   **Stack unwinds** → back to `fib(5)`

10. **Call:** `fibRecursive(3)` → compute `fib(2) + fib(1)`

    * `fib(2) = 1`
    * `fib(1) = 1`
      **fib(3) = 1 + 1 = 2`**   **Stack unwinds** → back to `fib(5)`

11. **Final Result:** `fib(5) = fib(4) + fib(3) = 3 + 2 = 5` ✅

---

### 🔎 Observations / Doubts

1. **Duplicate Computation**

   * `fib(3)` computed **two times**.
   * `fib(2)` computed **three times**.
   * `fib(1)` computed **five times**.

2. **Why Recursion is Slow**

   * Each function call spawns two more calls → **exponential growth**.
   * Time complexity = **O(2^n)**
   * Space complexity = **O(n)** (due to call stack).

3. **Call Stack Behavior**

   * Each recursive call waits for child calls.
   * Base case returns propagate back up, combining results.

4. **Your Doubts**

   * Why some values like `fib(2)` or `fib(3)` are computed multiple times?
   * How recursion tree expands and why it grows exponentially?
   * Difference between base case and recursive case?

**Answer:** Duplicate computations happen because recursion recalculates the same subproblems instead of storing them. Each level of the recursion tree doubles the calls approximately, causing exponential growth.

---

## 💡 Dynamic Programming (DP) – The Efficient Alternative

### Idea

* **Store previously computed results** to avoid recomputation.
* Two main approaches:

  1. **Memoization (Top-down)**
  2. **Tabulation (Bottom-up)**

---

### 1. Memoization (Top-Down)

```java
public static int fibMemo(int n, int[] dp) {
    if (n <= 1) return n;
    if (dp[n] != -1) return dp[n]; // already computed
    dp[n] = fibMemo(n - 1, dp) + fibMemo(n - 2, dp);
    return dp[n];
}

int n = 10;
int[] dp = new int[n + 1];
Arrays.fill(dp, -1);
System.out.println(fibMemo(n, dp)); // 55
```

* Time complexity: **O(n)**
* Space complexity: **O(n)**
* ✅ Each Fibonacci number is computed only **once**.

---

### 2. Tabulation (Bottom-Up)

```java
public static int fibTab(int n) {
    if (n <= 1) return n;

    int[] dp = new int[n + 1];
    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}
```

* Iteratively builds the sequence from base cases.
* Also **O(n)** time, **O(n)** space.

---

### 3. Space Optimized Iterative DP

```java
public static int fibOptimized(int n) {
    if (n <= 1) return n;

    int prev2 = 0, prev1 = 1, curr = 0;
    for (int i = 2; i <= n; i++) {
        curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return curr;
}
```

* Uses only **two variables** instead of an array.
* Time complexity: **O(n)**
* Space complexity: **O(1)**

---

## ⚖️ Comparison: Recursion vs DP

| Method             | Time Complexity | Space Complexity | Notes                               |
| ------------------ | --------------- | ---------------- | ----------------------------------- |
| Recursive (naive)  | O(2^n)          | O(n)             | Exponential, recomputes subproblems |
| Memoization (DP)   | O(n)            | O(n)             | Stores results in cache             |
| Tabulation (DP)    | O(n)            | O(n)             | Iterative, bottom-up                |
| Space-Optimized DP | O(n)            | O(1)             | Most efficient for practical use    |

---

## 🔑 Key Insights from Our Discussion

1. Recursion is **intuitive**, but inefficient for Fibonacci due to **duplicate computations**.
2. Dynamic Programming **eliminates recomputation** and makes the algorithm scalable.
3. **Base case**: stops recursion.
4. **Recursive case**: divides the problem into smaller subproblems.
5. **Stack explanation:** Each recursive call waits for its children; results bubble up the stack once base cases return.
6. DP is preferred for **large N** or **performance-critical scenarios**.
7. Space optimization can reduce memory usage without changing time complexity.

---

## ✅ Conclusion

* Use **recursion** to understand the problem and algorithm logic.
* Use **DP** for efficiency and large input sizes.
* Iterative DP with space optimization is the **best practical approach**
