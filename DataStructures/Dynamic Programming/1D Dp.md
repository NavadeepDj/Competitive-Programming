Perfect. Slow is **exactly** how DP should be learned.
We’ll build this **brick by brick**, no jumps.

---

# 🧠 1D Dynamic Programming — Patterns (Slow & Deep)

## First: what does **1D DP** mean?

It simply means:

> Your DP state depends on **one variable** (usually an index or number)

Examples:

* `dp[i]`
* `dp[n]`
* `dp[amount]`

No grids yet. No matrices. Just **one dimension**.

---

## The CORE idea (don’t skip this)

In 1D DP:

> `dp[i]` represents the **answer for size / index / value = i**

Everything depends on **how you define `dp[i]`**.

---

## 🧩 Pattern 1: Fibonacci-type DP (Linear DP)

### When you see:

* “number of ways”
* “can take 1 or 2 steps”
* “sum of previous results”

---

### Example 1: Fibonacci (revisited, but properly)

#### Step 1: Define state

```
dp[i] = ith Fibonacci number
```

#### Step 2: Transition

```
dp[i] = dp[i-1] + dp[i-2]
```

#### Step 3: Base cases

```
dp[0] = 0
dp[1] = 1
```

#### Step 4: Code

```python
def fib(n):
    dp = [0]*(n+1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

---

### 🔑 Mental pattern

> “Current depends on previous 1 or 2 values”

---

## 🧩 Pattern 2: Climbing / Ways DP

### When you see:

* “how many ways”
* “reach a target”
* “allowed steps”

---

### Example 2: Climbing Stairs

#### Problem

You can climb:

* 1 step
* 2 steps

How many ways to reach step `n`?

---

#### Step 1: State

```
dp[i] = number of ways to reach step i
```

#### Step 2: Transition

```
dp[i] = dp[i-1] + dp[i-2]
```

#### Step 3: Base cases

```
dp[0] = 1
dp[1] = 1
```

#### Step 4: Code

```python
def climb(n):
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

---

### 🔑 Mental pattern

> “Last move decides the count”

---

## 🧩 Pattern 3: Minimum / Maximum DP

### When you see:

* “minimum cost”
* “maximum profit”
* “fewest steps”

---

### Example 3: Min Cost to Reach End

You can move:

* 1 step
* 2 steps

Each step has a cost.

---

#### Step 1: State

```
dp[i] = minimum cost to reach step i
```

#### Step 2: Transition

```
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
```

#### Step 3: Base cases

```
dp[0] = cost[0]
dp[1] = cost[1]
```

#### Step 4: Code

```python
def min_cost(cost):
    n = len(cost)
    dp = [0]*n
    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[-1], dp[-2])
```

---

### 🔑 Mental pattern

> “Choose the cheapest previous path”

---

## 🧩 Pattern 4: Decision DP (Yes / No)

### When you see:

* “can we reach”
* “is it possible”
* “true / false”

---

### Example 4: Can You Reach End?

You can jump up to `k` steps.

---

#### Step 1: State

```
dp[i] = True if index i is reachable
```

#### Step 2: Transition

```
dp[i] = True if any dp[j] is True
(where j can jump to i)
```

#### Step 3: Base case

```
dp[0] = True
```

#### Step 4: Code

```python
def can_reach(nums):
    n = len(nums)
    dp = [False]*n
    dp[0] = True

    for i in range(n):
        if dp[i]:
            for j in range(1, nums[i]+1):
                if i+j < n:
                    dp[i+j] = True

    return dp[-1]
```

---

### 🔑 Mental pattern

> “Reachability flows forward”

---

## 🧩 Pattern 5: Subsequence / Subarray DP (1D version)

### When you see:

* “maximum subarray”
* “best ending here”

---

### Example 5: Maximum Subarray Sum (Kadane’s DP)

#### Step 1: State

```
dp[i] = maximum subarray sum ending at i
```

#### Step 2: Transition

```
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

#### Step 3: Base case

```
dp[0] = nums[0]
```

#### Step 4: Code

```python
def max_subarray(nums):
    dp = [0]*len(nums)
    dp[0] = nums[0]
    ans = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        ans = max(ans, dp[i])

    return ans
```

---

### 🔑 Mental pattern

> “Extend or restart”

---

## 🔒 The 5 CORE 1D DP PATTERNS (summary)

| Pattern   | Key Question               |
| --------- | -------------------------- |
| Fibonacci | Depends on previous values |
| Ways      | Count combinations         |
| Min / Max | Optimize cost              |
| Decision  | Can / cannot               |
| Subarray  | Best ending here           |

If you can identify **which pattern** a problem belongs to,
**90% of DP is done**.

---

## 🧠 How interviewers expect you to think

They want to hear:

1. What is `dp[i]`?
2. How do we build it?
3. What are base cases?
4. What is the answer?

Not memorized code.

---

## Let’s REALLY go slow now…

Next, we should do **ONE pattern deeply** with:

* recursion → memo → tabulation
* full dry run

### Pick ONE:

* `FIB / CLIMBING`
* `MIN COST`
* `MAX SUBARRAY`
* `REACHABILITY`

Tell me which one you want to *lock in* completely 👊
