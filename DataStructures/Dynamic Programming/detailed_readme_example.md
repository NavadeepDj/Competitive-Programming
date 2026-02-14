Perfect timing. 🧠  
Dynamic Programming (DP) is the **natural next step** after graphs — and we’ll do it **exactly like before**:

- from first principles
    
- step by step
    
- with intuition, not formulas
    
- and lots of “why”
    

No rushing. No memorization.

---

# 🧠 DYNAMIC PROGRAMMING — FROM ZERO

## 1️⃣ First: What problem does DP solve?

DP is used when a problem has **two properties**:

### ✅ Overlapping Subproblems

You solve the **same subproblem again and again**.

### ✅ Optimal Substructure

The optimal solution to a problem depends on **optimal solutions to smaller problems**.

If **both** are present → DP applies.

---

## 2️⃣ Why DP exists (the real reason)

Consider recursion:

```python
def f(n):
    return f(n-1) + f(n-2)
```

This looks simple, but it **recomputes** the same values many times.

DP exists to:

> “Remember results so we don’t recompute them.”

That’s all.

---

## 3️⃣ Recursion → DP (the mental shift)

|Approach|What happens|
|---|---|
|Pure recursion|Recomputes subproblems|
|DP|Stores & reuses answers|

DP = **Recursion + Memory**

---

## 4️⃣ Classic first example: Fibonacci (DON’T skip this)

### Naive recursion (❌)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### Problem:

- `fib(2)` called many times
    
- Time complexity ≈ **O(2ⁿ)**
    

---

## 5️⃣ Visualizing overlapping subproblems

```
fib(5)
 ├─ fib(4)
 │   ├─ fib(3)
 │   │   ├─ fib(2)
 │   │   └─ fib(1)
 │   └─ fib(2)
 └─ fib(3)
     ├─ fib(2)
     └─ fib(1)
```

Same nodes repeated ❌

---

## 6️⃣ DP Approach 1: Memoization (Top-Down)

### Idea

- Use recursion
    
- Store results in a dictionary / array
    

### Code

```python
def fib(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

### What changed?

- Each `fib(n)` computed **once**
    
- Time complexity → **O(n)**
    

---

## 7️⃣ DP Approach 2: Tabulation (Bottom-Up)

### Idea

- Start from smallest subproblems
    
- Build up to the answer
    

### Code

```python
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

---

## 8️⃣ Memoization vs Tabulation (IMPORTANT)

|Memoization|Tabulation|
|---|---|
|Top-down|Bottom-up|
|Recursive|Iterative|
|Uses call stack|No recursion|
|Easier to write|More space control|

Interviewers accept **either**, but tabulation is often preferred.

---

## 9️⃣ DP Pattern Recognition (THIS is key)

When you see:

- “maximum / minimum”
    
- “number of ways”
    
- “can we reach”
    
- “longest / shortest”
    

…and recursion is repeating work → DP.

---

## 10️⃣ How to think in DP (4-step framework)

**ALWAYS do this:**

### Step 1: Define the state

What does `dp[i]` represent?

### Step 2: Transition

How do we compute `dp[i]` from smaller states?

### Step 3: Base case

Smallest valid inputs

### Step 4: Answer

Which `dp` value is the final answer?

---

## 11️⃣ Example: Climbing Stairs (first real DP)

Problem:

> You can climb 1 or 2 steps.  
> How many ways to reach step `n`?

---

### Step 1: State

```
dp[i] = number of ways to reach step i
```

---

### Step 2: Transition

```
dp[i] = dp[i-1] + dp[i-2]
```

Why?

- Last step was 1-step OR 2-step
    

---

### Step 3: Base cases

```
dp[0] = 1
dp[1] = 1
```

---

### Step 4: Code

```python
def climb_stairs(n):
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

---

## 12️⃣ Notice the pattern

Fibonacci and Climbing Stairs are **the same DP** in disguise.

This is why DP is powerful.

---

## 13️⃣ Space Optimization (next level)

We don’t need the whole array:

```python
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
```

Space → **O(1)**

---

## 14️⃣ Mental model for DP 🧠

- Recursion = brute force
    
- DP = avoid recomputation
    
- State = what you remember
    
- Transition = how states connect
    

---

## What comes NEXT (logical order)

Now that DP basics are clear, next we’ll do:

1️⃣ **1D DP patterns**  
2️⃣ **2D DP (grid problems)**  
3️⃣ **Knapsack (classic interview DP)**  
4️⃣ **DP vs Greedy**

---

### Choose the next step:

Reply with:

- `1D DP PATTERNS`
    
- `GRID DP`
    
- `KNAPSACK`
    
- `INTERVIEW DP QUESTIONS`
    

We’ll continue **exactly at this depth** 👊

Perfect. Slow is **exactly** how DP should be learned.  
We’ll build this **brick by brick**, no jumps.

---

# 🧠 1D Dynamic Programming — Patterns (Slow & Deep)

## First: what does **1D DP** mean?

It simply means:

> Your DP state depends on **one variable** (usually an index or number)

Examples:

- `dp[i]`
    
- `dp[n]`
    
- `dp[amount]`
    

No grids yet. No matrices. Just **one dimension**.

---

## The CORE idea (don’t skip this)

In 1D DP:

> `dp[i]` represents the **answer for size / index / value = i**

Everything depends on **how you define `dp[i]`**.

---

## 🧩 Pattern 1: Fibonacci-type DP (Linear DP)

### When you see:

- “number of ways”
    
- “can take 1 or 2 steps”
    
- “sum of previous results”
    

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

- “how many ways”
    
- “reach a target”
    
- “allowed steps”
    

---

### Example 2: Climbing Stairs

#### Problem

You can climb:

- 1 step
    
- 2 steps
    

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

- “minimum cost”
    
- “maximum profit”
    
- “fewest steps”
    

---

### Example 3: Min Cost to Reach End

You can move:

- 1 step
    
- 2 steps
    

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

- “can we reach”
    
- “is it possible”
    
- “true / false”
    

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

- “maximum subarray”
    
- “best ending here”
    

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

|Pattern|Key Question|
|---|---|
|Fibonacci|Depends on previous values|
|Ways|Count combinations|
|Min / Max|Optimize cost|
|Decision|Can / cannot|
|Subarray|Best ending here|

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

- recursion → memo → tabulation
    
- full dry run
    

### Pick ONE:

- `FIB / CLIMBING`
    
- `MIN COST`
    
- `MAX SUBARRAY`
    
- `REACHABILITY`
    

Tell me which one you want to _lock in_ completely 👊

Perfect choice.  
**Maximum Subarray** is _the_ DP problem that teaches you how to **think locally but answer globally**.

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

- Try **all possible subarrays**
    
- Compute their sums
    
- Take the maximum
    

### Why this is bad

- Number of subarrays ≈ `n²`
    
- Sum computation inside ≈ `n`
    
- Total ≈ **O(n³)** ❌
    

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

- `dp[i]` only needs `dp[i-1]`
    

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

- Drop it
    
- Restart fresh
    

This is why restarting is sometimes better than extending.

---

## 🔥 ONE sentence that unlocks everything

> “At each index, I decide whether to extend the previous subarray or start a new one, and I track the best sum seen so far.”

That’s the whole algorithm.

---

## 10️⃣ Edge cases (don’t miss these)

- All negatives → answer is **max element**
    
- Single element array
    
- Mixed positives & negatives
    

Kadane handles all of them.

---

## 11️⃣ Pattern recognition (INTERVIEW GOLD)

When you see:

- “maximum subarray”
    
- “best ending here”
    
- “contiguous segment”
    

Think:

```
dp[i] = max ending at i
```

---

## 12️⃣ What this prepares you for next

Maximum Subarray unlocks:

- Maximum product subarray
    
- Stock buy/sell DP
    
- 2D max submatrix
    
- DP on arrays
    

---

### Next (slow and logical)

Pick one:

- `MAX PRODUCT SUBARRAY`
    
- `STOCK BUY SELL`
    
- `COIN CHANGE (1D DP)`
    
- `DP INTERVIEW PRACTICE`
    

Tell me where you want to go 👊

Yes — **exactly** 👍  
You’re thinking in the **right direction**.

👉 **2D DP is where problems like LCS (Longest Common Subsequence) live.**  
But before jumping straight into LCS, let’s **slowly build the intuition** so LCS feels _obvious_, not magical.

---

# 🧠 What is 2D Dynamic Programming?

## Core idea

In **1D DP**, we had:

```
dp[i]
```

In **2D DP**, we have:

```
dp[i][j]
```

Meaning:

> The answer depends on **two changing parameters**.

Usually:

- two indices
    
- two strings
    
- two arrays
    
- grid positions (row, column)
    

---

## When does 2D DP appear?

You’ll almost always see **2D DP** when the problem involves:

✅ **Two sequences**  
✅ **Comparisons between prefixes**  
✅ **Choices involving include / exclude**  
✅ **Grid movement**

That’s why **LCS fits perfectly**.

---

## Big mental shift (VERY IMPORTANT)

### 1D DP thinking:

> “What’s the answer up to index `i`?”

### 2D DP thinking:

> “What’s the answer using  
> first `i` elements of X  
> and first `j` elements of Y?”

This sentence alone explains **LCS**, **Edit Distance**, **LPS**, etc.

---

## Before LCS: understand the DP table

Suppose we have two strings:

```
X = "abc"
Y = "ac"
```

We create a table:

```
dp[i][j]
```

Where:

```
dp[i][j] = answer considering:
           X[0..i-1] and Y[0..j-1]
```

⚠️ Notice:

- `i` and `j` are **lengths**, not indices
    
- That’s why dp size is `(len(X)+1) x (len(Y)+1)`
    

---

## Why the extra row & column?

Base case:

```
If one string is empty → LCS = 0
```

So:

```
dp[0][j] = 0
dp[i][0] = 0
```

This avoids boundary headaches.

---

## Now… does LCS come into picture?

👉 **YES. This is the canonical 2D DP problem.**

LCS is usually the **first serious 2D DP** people learn because:

- logic is clean
    
- transition is intuitive
    
- teaches prefix-based thinking
    

---

# 🔑 LCS Problem (conceptual)

### Problem statement

Given two strings:

```
X = "abcde"
Y = "ace"
```

Find the **length of the longest subsequence** common to both.

Subsequence:

- characters in order
    
- not necessarily contiguous
    

---

## Step-by-step LCS DP formulation

### Step 1️⃣ State definition (MOST IMPORTANT)

```
dp[i][j] = length of LCS of
           X[0..i-1] and Y[0..j-1]
```

Say this out loud — it matters.

---

### Step 2️⃣ Base case

If either string is empty:

```
dp[0][j] = 0
dp[i][0] = 0
```

---

### Step 3️⃣ Transition (THIS is the heart)

Now compare:

```
X[i-1] and Y[j-1]
```

Two cases:

---

### ✅ Case 1: Characters match

```
X[i-1] == Y[j-1]
```

Then:

```
dp[i][j] = 1 + dp[i-1][j-1]
```

Why?

> We extend the LCS of smaller prefixes.

---

### ❌ Case 2: Characters do NOT match

We have a choice:

- ignore current char of X
    
- OR ignore current char of Y
    

So:

```
dp[i][j] = max(
              dp[i-1][j],
              dp[i][j-1]
          )
```

---

## This logic is the SOUL of LCS

Every LCS explanation reduces to this:

> “If characters match, include them.  
> If not, try skipping one from either side.”

---

## Full LCS code (clean & standard)

```python
def lcs(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]
```

---

## Why LCS MUST be 2D DP

Because the decision at `(i, j)` depends on:

- previous prefix of X (`i-1`)
    
- previous prefix of Y (`j-1`)
    

You **cannot collapse this into 1D** without losing information.

---

## Pattern recognition (INTERVIEW GOLD)

If you see:

- two strings
    
- “longest common…”
    
- “edit / transform”
    
- “minimum operations between strings”
    

Think:

```
2D DP over prefixes
```

---

## 2D DP problems closely related to LCS

Once LCS is clear, these become easy:

- Longest Palindromic Subsequence
    
- Edit Distance
    
- Shortest Common Supersequence
    
- Delete Operation for Two Strings
    

They all reuse **this exact DP table idea**.

---

## Let’s go REALLY slow from here

Next, we should:  
1️⃣ **Dry-run LCS on a small example (table filled step by step)**  
2️⃣ Show **how to reconstruct the actual LCS string**  
3️⃣ Compare **LCS vs Longest Common Substring** (very common confusion)

### Tell me what you want next:

- `LCS DRY RUN`
    
- `PRINT THE LCS`
    
- `LCS vs SUBSTRING`
    
- `GRID DP (paths)`
    

We’ll continue at the same calm pace 🧘‍♂️

Perfect — this is the **most important part of LCS**.  
Length is easy. **Printing the LCS is where real understanding shows.**

We’ll go **very slowly**, exactly like before.

---

# 🧠 Printing the Longest Common Subsequence (LCS)

We’ll do this in **3 phases**:

1. Build the DP table (already known)
    
2. Understand **what the table represents**
    
3. **Backtrack** to print the LCS
    

No magic. Just logic.

---

## 1️⃣ Problem setup (small, clear example)

Let’s take:

```
X = "abcde"
Y = "ace"
```

Expected LCS:

```
"ace"
```

---

## 2️⃣ Step 1: Build the DP table (quick recap)

### DP definition

```
dp[i][j] = length of LCS of X[0..i-1] and Y[0..j-1]
```

### Code to build DP table

```python
def build_lcs_table(X, Y):
    n, m = len(X), len(Y)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp
```

At the end:

```
dp[n][m] = length of LCS
```

But **the table contains more information** — the _choices_ we made.

---

## 3️⃣ What the DP table really means (IMPORTANT)

At each cell `(i, j)`:

- If characters matched → we came from **diagonal**
    
- If they didn’t match → we came from:
    
    - top `(i-1, j)` OR
        
    - left `(i, j-1)`
        

This means:  
👉 **We can reverse the process** to recover the sequence.

---

## 4️⃣ Step 2: Backtracking to print the LCS

### Where do we start?

From:

```
i = len(X)
j = len(Y)
```

Bottom-right corner of the table.

---

### Backtracking rules (burn this in 🔥)

While `i > 0` and `j > 0`:

#### ✅ Case 1: Characters match

```
X[i-1] == Y[j-1]
```

Then:

- This character **is part of LCS**
    
- Add it to result
    
- Move diagonally:
    

```
i -= 1
j -= 1
```

---

#### ❌ Case 2: Characters do NOT match

Look at DP values:

- If `dp[i-1][j] > dp[i][j-1]`  
    → move **up**
    
    ```
    i -= 1
    ```
    
- Else  
    → move **left**
    
    ```
    j -= 1
    ```
    

This mirrors the choice we made while building the table.

---

## 5️⃣ Full code: Print the LCS

```python
def print_lcs(X, Y):
    dp = build_lcs_table(X, Y)
    i, j = len(X), len(Y)
    lcs = []

    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])   # part of LCS
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs))
```

---

## 6️⃣ Dry run intuition (high-level)

For:

```
X = abcde
Y = ace
```

Backtracking path:

```
e == e → include 'e'
c == c → include 'c'
a == a → include 'a'
```

Collected (reverse order):

```
['e', 'c', 'a']
```

Reverse it:

```
"ace"
```

---

## 7️⃣ Why reversing is needed

We backtrack from the **end to the start**, so:

- characters are added **backwards**
    

That’s why we reverse at the end.

---

## 8️⃣ Time & space complexity

- DP table build: `O(n * m)`
    
- Backtracking: `O(n + m)`
    
- Space: `O(n * m)`
    

This is optimal for LCS.

---

## 9️⃣ Common mistakes (watch out)

❌ Forgetting to reverse result  
❌ Comparing `X[i]` instead of `X[i-1]`  
❌ Moving wrong direction on mismatch  
❌ Confusing LCS with substring

---

## 🔑 One sentence that proves understanding (interview gold)

> “After building the DP table for LCS length, I backtrack from the bottom-right cell. When characters match, I move diagonally and include the character; otherwise, I move in the direction of the larger DP value.”

That sentence alone is 🔥.

---

## What’s the natural next step?

Now that you can **print LCS**, the next logical topics are:

1️⃣ **LCS vs Longest Common Substring** (very common trap)  
2️⃣ **Edit Distance** (uses almost same DP table)  
3️⃣ **Shortest Common Supersequence**  
4️⃣ **Grid-based 2D DP problems**

Tell me what you want next — we’ll keep the same slow, solid pace 👊
