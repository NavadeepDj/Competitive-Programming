# Java Command Line Execution: A Detailed Guide

This README documents the journey from common Java command line errors to a complete understanding of the compilation and execution process, including the newer single-file source code feature.

## 1. The Initial Problem: Confusing the Compiler and the Runtime

The initial confusion stemmed from combining the Java execution command (`java`) with the file extension (`.class` or `.java`) incorrectly.

### 🔴 The Error Scenario

| User Command | Output Error | Core Mistake |
| :--- | :--- | :--- |
| `java .\oddOrEven.class` | `Error: Could not find or load main class .\oddOrEven.class` | Included both the **path prefix** (`.\`) and the **`.class` extension**. |
| `java oddOrEven.class` | `Error: Could not find or load main class oddOrEven.class` | Included the **`.class` extension**. |

### 💡 The Solution for Bytecode Execution

When running an **already compiled** class file (`.class`), you must use only the **Class Name** (the name of the public class inside the file), not the file name or extension.

| Correct Command | Meaning |
| :--- | :--- |
| `java oddOrEven` | Tells the **JVM** to load and run the bytecode file named `oddOrEven.class`. |

***

## 2. Understanding the Java Tool Chain

To understand why the first commands failed, we must know the roles of the two main Java command line tools: `javac` and `java`.

### 📚 Tool 1: `javac` (The Java Compiler)

| Command | Role | Output |
| :--- | :--- | :--- |
| `javac <FileName>.java` | The **Java Compiler**. Its sole purpose is to read human-readable source code (`.java`). | Converts the source code into **bytecode**, creating a new file named `<ClassName>.class` on the disk. |
| **Example:** `javac prime.java` | Compiles the source file. | Creates `prime.class`. |

### 📚 Tool 2: `java` (The Java Virtual Machine Launcher)

| Command | Role | Input |
| :--- | :--- | :--- |
| `java <ClassName>` | The **JVM Launcher**. Its traditional role is to load and run compiled bytecode. | Requires a **Class Name** (not a file name) to load the corresponding `.class` file. |
| **Example:** `java prime` | Executes the main method inside `prime.class`. | Loads `prime.class`. |

***

## 3. The Modern Feature: Single-File Source Code Execution

Your observation that you could run the code using `java .\prime.java` without a preceding `javac` step introduced a modern feature of the Java language.

### 🚀 Java 11+ Source-Code Mode (JEP 330)

| Command | Action | Key Detail |
| :--- | :--- | :--- |
| `java <FileName>.java` | The `java` command (JVM) switches into a special mode: it **implicitly compiles** the source file *in memory* and then immediately executes it. | **No permanent** `.class` file is generated on the disk. This is a convenience feature for quick scripts and learning. |
| **Example:** `java .\prime.java` | Compiles and runs the program in a single step. | The program runs successfully, but no `prime.class` file is updated/created on your desktop. |

***

## 4. Final Conclusion: The Two Correct Ways to Run Java

Your final summary is the perfect conclusion. There are now two distinct, correct methods for running a single Java source file from the command line:

### Method A: The Quick Single-Step (Java 11+)

This is the easiest way to test a single file.

| Step | Command | Result |
| :--- | :--- | :--- |
| 1. Run | `java prime.java` | Auto-compiles **in memory** and executes the code. |

### Method B: The Traditional Two-Step (Manual Compilation)

This is the classic, mandatory method for all multi-file projects, or when you specifically need the compiled `.class` file.

| Step | Command | Result |
| :--- | :--- | :--- |
| 1. Compile | `javac prime.java` | Creates/updates the permanent **`prime.class`** file on disk. |
| 2. Run | `java prime` | Loads the **`prime.class`** file from disk and executes the bytecode. |

---

> **Crucial Difference:** You must use the **Class Name** (`prime`) when running a compiled class, but you must use the **File Name with extension** (`prime.java`) when invoking the single-step compilation mode.
