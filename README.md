markdown
# Simple Calculator Functions

This project provides a set of basic arithmetic functions written in Python, along with corresponding unit tests to ensure their correctness. It's a small, focused module designed to perform fundamental mathematical operations.

## Available Functions

The `app.py` file contains the following functions:

*   **`add(a, b)`**:
    *   Returns the sum of two numbers, `a` and `b`.
    *   Example: `add(5, 3)` returns `8`.
*   **`subtract(a, b)`**:
    *   Returns the difference between two numbers, `a` and `b`.
    *   Example: `subtract(10, 4)` returns `6`.
*   **`multiply(a, b)`**:
    *   Returns the product of two numbers, `a` and `b`.
    *   Example: `multiply(6, 7)` returns `42`.

## How to Run Tests

The project includes a `test_app.py` file that uses Python's built-in `unittest` framework to verify the functionality of the `add` function.

To run the tests, navigate to the project's root directory in your terminal and execute the following command:

bash
python -m unittest test_app.py


This command will run all the test cases defined in `test_app.py` and report the results.