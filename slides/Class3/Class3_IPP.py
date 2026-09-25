import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class3_IPP.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Class 3 Individual Practice Problems (IPP)

    Name: _________________________________________________

    **Instructions:**

    - You have **5 minutes** to complete these problems
    - **No references or notes allowed**
    - Show your work where indicated
    - This will be collected for attendance and graded using the EARN system
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### Problem 1 (2 points)

    What will this code print?

    ```python
    x = 10
    y = 5
    result = (x > y)
    print(result)
    ```

    Answer: _________________________________________________
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### Problem 2 (2 points)

    Write the correct comparison operator to check if a variable `score` is
    greater than or equal to 90.

    ```python
    if score _____ 90:
        print("Grade: A")
    ```

    Answer: _________________________________________________
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### Problem 3 (2 points)

    What will this expression evaluate to?

    ```python
    True and False
    ```

    Answer: _________________________________________________
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### Problem 4 (2 points)

    According to EK125 style, which is the CORRECT way to write this if statement?

    *Circle ONE answer:*

    a) `if isStudent:`

    b) `if isStudent == True:`

    c) `if isStudent is True:`
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Problem 5 (2 points)

    What Boolean operator would you use to check if a value is in a list?

    *Example: Check if `"apple"` is in the list `fruits`*

    Answer: _________________________________________________
    """)
    return


if __name__ == "__main__":
    app.run()
