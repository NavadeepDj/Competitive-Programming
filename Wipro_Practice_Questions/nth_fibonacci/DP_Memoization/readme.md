# 📝 Fibonacci Using Dynamic Programming (Memoization)

## 🚨 Problem Recap

When solving Fibonacci using **plain recursion**:

```java
fib(n) = fib(n-1) + fib(n-2)
```

* For `fib(5)`, the function calls repeat the same subproblems many times.
* Example: `fib(3)` is calculated multiple times, `fib(2)` even more.
* This leads to **exponential time complexity O(2^n)**.

---

## ✅ Solution: Dynamic Programming 
DP says:

Don’t repeat work you’ve already done. Store results and reuse them.

There are two common DP approaches: Memiozation(Top-Down) and Tabulation (Bottom-up)



**Memoization** = "Remember what you’ve already solved".
You write the same recursive function, but whenever you compute a result, you store it in an array/map.


Instead of recalculating the same subproblem, we **store results** in an array/map and reuse them.

### Java Implementation

```java
import java.util.*;

public class FibonacciMemo {
    static int[] memo;

    public static int fibMemo(int n) {
        if (n <= 1) return n;

        // Already computed? Return it
        if (memo[n] != -1) return memo[n];

        // Otherwise compute and store
        memo[n] = fibMemo(n - 1) + fibMemo(n - 2);
        return memo[n];
    }

    public static void main(String[] args) {
        int n = 6;
        memo = new int[n + 1]; // Initialize with size n+1
        Arrays.fill(memo, -1);

        System.out.println("Fibonacci(" + n + ") = " + fibMemo(n));
    }
}
```

👉 How it works:

First time fibMemo(5) computes fib(3), it stores it in memo[3].

Next time someone calls fib(3), we just return memo[3] instead of recalculating.

Cuts off all repeated calls.

⏱️ Time Complexity: O(n)
💾 Space Complexity: O(n) (stack + memo array)



## 🔍 Doubt: Why `n+1` Instead of Just `n`?

This is a **very important detail**.
In Java, arrays are **0-indexed**.

* If we only create `new int[n]`, the **valid indices** are `0` to `n-1`.
* But in Fibonacci, we need to store results for **all values up to `n`**, including `fib(n)` itself.

👉 Example:

* Suppose `n = 6`.
* We need `memo[6]` to store `fib(6)`.
* If we had only created `new int[6]`, indices go from `0` to `5`.
* Trying to access `memo[6]` would throw an `ArrayIndexOutOfBoundsException`.

✅ That’s why we create `memo = new int[n + 1]` so indices are available from `0` through `n`.

---

## ⚡ How Memoization Works Internally

1. First call: `fibMemo(6)` → not in `memo`, so compute.
2. It calls `fibMemo(5)` and `fibMemo(4)`.
3. Each subproblem is stored in `memo` after first calculation.
4. When the same subproblem is needed again, it is **directly returned from `memo`** instead of recalculating.

---

## 📊 Complexity

* **Time Complexity**: O(n)
  Each subproblem is solved once and then reused.
* **Space Complexity**: O(n)
  For the `memo` array + recursion stack.

---

## ✨ Summary

* Recursion alone is inefficient because of repeated calculations.
* **Memoization (Top-Down DP)** optimizes it by storing results.
* Using `n+1` for the memo array ensures we can safely store results up to `fib(n)` without index issues.

---

Would you like me to also prepare the **same style README for Tabulation (Bottom-Up)** next, so you’ll have a side-by-side comparison in your repo?
