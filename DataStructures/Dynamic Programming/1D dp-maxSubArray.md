Perfect choice.
**Maximum Subarray** is *the* DP problem that teaches you how to **think locally but answer globally**.

We’ll go **very slow**, from brute force → DP → intuition → code → why it works.

No shortcuts.

---

# 🧠 MAXIMUM SUBARRAY (Kadane’s Algorithm)

## Problem statement (simple words)

Given an array of integers (can be negative):

```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Find the **maximum sum of a contiguous subarray**.

Answer here:

```
[4, -1, 2, 1] → sum = 6
```

---

## 1️⃣ First: Brute force thinking (important)

### Idea

* Try **all possible subarrays**
* Compute their sums
* Take the maximum

### Why this is bad

* Number of subarrays ≈ `n²`
* Sum computation inside ≈ `n`
* Total ≈ **O(n³)** ❌

Even with prefix sums → **O(n²)** ❌

So we need a smarter idea.

---

## 2️⃣ Key DP insight (THIS is the turning point)

Instead of asking:

> “What is the maximum subarray overall?”

Ask a **smaller, local question**:

> 👉 “What is the maximum subarray sum that **ENDS at index i**?”

This is the magic.

---

## 3️⃣ Define the DP state (most important step)

```
dp[i] = maximum subarray sum ending exactly at index i
```

⚠️ “Ending at i” is crucial.

We are **not** asking for the global answer yet.

---

## 4️⃣ Transition (the heart of the algorithm)

At index `i`, you have **two choices**:

### Choice 1: Extend previous subarray

```
dp[i-1] + nums[i]
```

### Choice 2: Start fresh at i

```
nums[i]
```

So:

```
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

That’s it. That’s Kadane.

---

## 5️⃣ Base case

At the start:

```
dp[0] = nums[0]
```

You have no choice at index 0.

---

## 6️⃣ Walk through the example STEP BY STEP

```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Let’s build `dp` slowly.

### i = 0

```
dp[0] = -2
best = -2
```

---

### i = 1 (value = 1)

```
extend = -2 + 1 = -1
restart = 1

dp[1] = 1
best = 1
```

---

### i = 2 (value = -3)

```
extend = 1 + (-3) = -2
restart = -3

dp[2] = -2
best = 1
```

---

### i = 3 (value = 4)

```
extend = -2 + 4 = 2
restart = 4

dp[3] = 4
best = 4
```

---

### i = 4 (value = -1)

```
extend = 4 + (-1) = 3
restart = -1

dp[4] = 3
best = 4
```

---

### i = 5 (value = 2)

```
extend = 3 + 2 = 5
restart = 2

dp[5] = 5
best = 5
```

---

### i = 6 (value = 1)

```
extend = 5 + 1 = 6
restart = 1

dp[6] = 6
best = 6
```

---

### i = 7 (value = -5)

```
extend = 6 - 5 = 1
restart = -5

dp[7] = 1
best = 6
```

---

### i = 8 (value = 4)

```
extend = 1 + 4 = 5
restart = 4

dp[8] = 5
best = 6
```

---

## ✅ Final answer

```
6
```

---

## 7️⃣ Full DP code (clear version)

```python
def max_subarray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        best = max(best, dp[i])

    return best
```

---

## 8️⃣ Space optimization (important interview improvement)

Notice:

* `dp[i]` only needs `dp[i-1]`

So we don’t need the array.

---

### Optimized Kadane (O(1) space)

```python
def max_subarray(nums):
    curr = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        curr = max(nums[i], curr + nums[i])
        best = max(best, curr)

    return best
```

---

## 9️⃣ Why this works (deep intuition)

### Key rule

> If your current sum becomes **negative**, it will only **hurt future sums**.

So:

* Drop it
* Restart fresh

This is why restarting is sometimes better than extending.

---

## 🔥 ONE sentence that unlocks everything

> “At each index, I decide whether to extend the previous subarray or start a new one, and I track the best sum seen so far.”

That’s the whole algorithm.

---

## 10️⃣ Edge cases (don’t miss these)

* All negatives → answer is **max element**
* Single element array
* Mixed positives & negatives

Kadane handles all of them.

---

## 11️⃣ Pattern recognition (INTERVIEW GOLD)

When you see:

* “maximum subarray”
* “best ending here”
* “contiguous segment”

Think:

```
dp[i] = max ending at i
```

---

## 12️⃣ What this prepares you for next

Maximum Subarray unlocks:

* Maximum product subarray
* Stock buy/sell DP
* 2D max submatrix
* DP on arrays

---

### Next (slow and logical)

Pick one:

* `MAX PRODUCT SUBARRAY`
* `STOCK BUY SELL`
* `COIN CHANGE (1D DP)`
* `DP INTERVIEW PRACTICE`

Tell me where you want to go 👊
