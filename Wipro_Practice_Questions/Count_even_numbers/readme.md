# 📘 Counting Even Numbers (5 Inputs)

This small project explores different ways to count how many **even numbers** exist among 5 given integers.
It also demonstrates Python and Java implementations, using both traditional loops and functional-style approaches (`filter`, `lambda`, `streams`).

---

## 🔎 Problem Statement

Write a function that:

* Accepts **5 integer inputs**.
* Returns the **count of numbers that are even**.

---

## 🐍 Python Solutions

### ✅ Using `filter` + `lambda`

```python
def count_evens(a, b, c, d, e):
    nums = [a, b, c, d, e]
    return len(list(filter(lambda x: x % 2 == 0, nums)))

# Example
print(count_evens(2, 3, 6, 7, 8))  # Output: 3
```

### 🔎 Explanation

1. Store all inputs in a list `nums`.
2. Use `filter` with a `lambda` function to keep only even numbers (`x % 2 == 0`).
3. Convert the result into a list.
4. Return its length.

---

### ✅ Using List Comprehension

```python
def count_evens(a, b, c, d, e):
    nums = [a, b, c, d, e]
    return len([x for x in nums if x % 2 == 0])
```

---

### ✅ Using `sum` + Generator

```python
def count_evens(a, b, c, d, e):
    nums = [a, b, c, d, e]
    return sum(1 for x in nums if x % 2 == 0)
```

---

## ☕ Java Solutions

### ✅ Using a For Loop

```java
public class CountEvens {
    public static int countEvens(int a, int b, int c, int d, int e) {
        int[] nums = {a, b, c, d, e};
        int count = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(countEvens(2, 3, 6, 7, 8)); // Output: 3
    }
}
```

---

### ✅ Using Java Streams

```java
import java.util.stream.IntStream;

public class CountEvens {
    public static int countEvens(int a, int b, int c, int d, int e) {
        return (int) IntStream.of(a, b, c, d, e)
                              .filter(x -> x % 2 == 0)
                              .count();
    }

    public static void main(String[] args) {
        System.out.println(countEvens(2, 3, 6, 7, 8)); // Output: 3
    }
}
```

---

## 🧠 Key Insights

* **Python**

  * `filter + lambda` provides a functional style.
  * List comprehensions and `sum(1 for ...)` are more Pythonic.
* **Java**

  * For loop is the most straightforward.
  * Streams provide a functional alternative (similar to Python’s `filter`).

---

## 📌 Example Run

Input: `2, 3, 6, 7, 8`
Output: `3` (since 2, 6, and 8 are even)

