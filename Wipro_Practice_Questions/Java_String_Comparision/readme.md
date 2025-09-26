# 📘 Counting Evens or Odds (Java)

This README documents a small Java program that counts how many **even** or **odd** numbers exist among 5 given integers.
It also covers a **common beginner mistake** with Java string comparison and how we fixed it.

---

## 🔎 Problem Statement

Write a method:

* Inputs: 5 integers (`input1, input2, input3, input4, input5`) and a string (`input6`).
* Behavior:

  * If `input6 == "even"` → return the count of even numbers.
  * If `input6 == "odd"` → return the count of odd numbers.

---

## ❌ My Initial Code (Buggy)

```java
int nums[] = {input1, input2, input3, input4, input5};
int count = 0;

if (input6 == "even") {
    for (int n : nums) {
        if (n % 2 == 0) {
            count++;
            System.out.println("even c" + count);
        }
    }
}

if (input6 == "odd") {
    for (int n : nums) {
        if (n % 2 != 0) {
            count++;
            System.out.println("Odd c" + count);
        }
    }
}

return count;
```

### 🚨 The Mistake

I used `==` to compare strings in Java:

```java
if (input6 == "even")
```

But in Java:

* `==` compares **object references** (memory addresses).
* `.equals()` compares the **string content**.

So even if `input6` was `"even"`, the condition didn’t work as expected.

---

## ✅ Corrected Code

```java
public static int countEvensOdds(int input1, int input2, int input3, int input4, int input5, String input6) {
    int nums[] = {input1, input2, input3, input4, input5};
    int count = 0;

    if (input6.equals("even")) {
        for (int n : nums) {
            if (n % 2 == 0) {
                count++;
            }
        }
        System.out.println("Even count = " + count);
    } else if (input6.equals("odd")) {
        for (int n : nums) {
            if (n % 2 != 0) {
                count++;
            }
        }
        System.out.println("Odd count = " + count);
    }

    return count;
}
```

---

## 🧠 Key Insights

1. **String comparison in Java**

   * Use `.equals()` for content comparison.
   * Use `.equalsIgnoreCase()` if case sensitivity doesn’t matter.
   * Avoid using `==` with strings (works for primitives like `int`, `double`, but not for `String`).

2. **Cleaner structure**

   * Using `else if` prevents checking both `"even"` and `"odd"`.
   * Printing the result outside the loop avoids clutter in output.

---

## 📌 Example Run

```java
System.out.println(countEvensOdds(2, 3, 6, 7, 8, "even")); 
// Output: Even count = 3
// Return value: 3

System.out.println(countEvensOdds(2, 3, 6, 7, 8, "odd"));  
// Output: Odd count = 2
// Return value: 2
```

