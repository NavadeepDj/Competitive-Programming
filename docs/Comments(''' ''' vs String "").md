# 📝 Python: Triple Quotes (`'''` / `"""`) vs Comments

In Python, triple quotes **look like comments**, but they are **not real comments**. Let’s understand what they are and how they behave.

---

## ❓ What Are Triple Quotes in Python?

Triple quotes are used to define **multi-line strings**:

```python
str1 = '''This is
a multi-line
string'''
```

They can be:

* `''' triple single quotes '''`
* `""" triple double quotes """`

These strings can span multiple lines and preserve newline characters.

---

## ❌ Misconception: Are triple quotes comments?

> **No**, triple quotes are **not comments**.
> They are **string literals**, even when not assigned to any variable.

---

### 🔍 Example:

```python
str1 = '''I am Navadeep: snkbjbjcdjcldc'''
'''I am Navadeep: snkbjbjcdjcldc'''
# bjwvcdhckec
'''I am Navadeep: snkbjbjcdjcldc'''

print(str1)
```

### ✅ What happens?

1. `str1` stores the string `'I am Navadeep: snkbjbjcdjcldc'`.
2. The other `'''...'''` lines are valid **multi-line string literals** but:

   * They are **not assigned** to any variable.
   * They get **created and discarded**.
3. The `#` line is a true **comment** and ignored.

### 🧾 Output:

```
I am Navadeep: snkbjbjcdjcldc
```

---

## ✅ True Comment Syntax in Python

```python
# This is a valid single-line comment
```

Python does **not** have a dedicated block comment syntax like C/C++ (`/* ... */`), so all comments must start with `#`.

---

## ⚠️ Triple Quotes for Commenting? (Not Recommended)

Sometimes developers do this:

```python
'''
This block is commented out
during development
'''
```

### It works because:

* Triple quotes define a string.
* If that string is not assigned or used, Python just discards it.

### BUT:

* Python **still parses and processes** the string.
* It is **not truly ignored** like a `#` comment.
* **Avoid using triple quotes** for commenting long blocks of code permanently.

---

## 🧪 Testing Behavior

```python
print("Start")

'''This is a fake comment.
Python will still parse it.
'''
print("End")
```

### Output:

```
Start
End
```

But if you add a syntax error *inside* the triple-quoted string, Python still throws an error!

---

## ✅ Best Practices

| Task                          | Use                                                                |
| ----------------------------- | ------------------------------------------------------------------ |
| Single-line comment           | `# Comment`                                                        |
| Block of real code comments   | `# Line 1`<br>`# Line 2`                                           |
| Multi-line string (docstring) | `'''string'''` or `"""string"""`                                   |
| Temporary block comment       | You *can* use `'''...'''`, but it's better to use `#` on each line |

---

## ✅ Summary

| Feature               | Triple Quotes (`'''`) | Comment (`#`)    |
| --------------------- | --------------------- | ---------------- |
| Used for strings      | ✅ Yes                 | ❌ No             |
| Used for docstrings   | ✅ Yes                 | ❌ No             |
| Executed by Python    | ✅ Yes (parsed)        | ❌ No (ignored)   |
| Creates unused object | ✅ If not assigned     | ❌ Not applicable |
| True comment          | ❌ No                  | ✅ Yes            |

---

## 📌 Final Note

> Triple quotes are for **multi-line strings**, not real comments.
> Always use `#` for actual commenting in your Python programs.
