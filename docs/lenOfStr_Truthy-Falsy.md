Sure! Here's a complete and well-formatted `README.md` for your GitHub repo, documenting how to calculate the **length of a string without using `len()`**, including your code, explanation, and a **mini truthy/falsy cheat sheet** at the end.

---

# 🔢 Finding Length of a String Without `len()` in Python

In Python, you usually find the length of a string using the built-in `len()` function.
But what if you’re not allowed to use `len()`?
Here’s a simple and intuitive way to do it using a `while` loop.

---

## 🧪 Code

```python
count1 = 0
str1 = input("Enter a string: ")
while str1:
    print(str1)  # Debug: See the string getting shorter each loop
    str1 = str1[1:]  # Remove the first character
    count1 = count1 + 1  # Count each removal

print(count1)
```

---

## 🧠 Explanation

### ✅ How does this work?

* We repeatedly remove the first character from the string using `str1 = str1[1:]`.
* Each time we do that, we **increment a counter**.
* We stop when the string becomes empty (`""`).
* Since we remove one character per loop, the final value of `count1` is the total length of the original string.

---

## ❓ Why does `while str1:` work?

In Python, an empty string `""` is treated as `False` in a boolean condition.
So:

```python
while str1:
```

...means:

> 🔁 **"Loop while the string is not empty."**

Once `str1` becomes `""`, the loop ends.

This is because Python has a concept of **"truthy" and "falsy"** values, where some non-boolean objects can behave like `True` or `False` in conditions.

---

## ✅ Sample Input and Output

**Input:**

```
hello
```

**Output:**

```
hello
ello
llo
lo
o
5
```

You see the string getting shorter each time, and the final count is the length!

---

## 🧾 Mini Truthy/Falsy Cheat Sheet in Python

Here’s a quick reference of values that are treated as `False`:

| Type         | Value Considered False |
| ------------ | ---------------------- |
| Boolean      | `False`                |
| NoneType     | `None`                 |
| Numbers      | `0`, `0.0`, `0j`       |
| Strings      | `""`                   |
| Lists        | `[]`                   |
| Tuples       | `()`                   |
| Dictionaries | `{}`                   |
| Sets         | `set()`                |

**Everything else is considered `True` ("truthy").**

---

## 💡 Summary

✅ This technique is useful when:

* You're learning Python internals
* You want to practice logic without built-in functions
* You're solving a problem where `len()` isn't allowed

---

Let me know if you want this exported as a file or added to another README section!
