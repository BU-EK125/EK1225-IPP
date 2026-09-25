import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class4_IPP.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Class 4 Individual Practice Problems
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### Problem 1 (2 points)

    What will this code print?

    ```python
    temperature = 75
    if temperature > 80:
        print("Hot")
    elif temperature > 60:
        print("Warm")
    else:
        print("Cold")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### Problem 2 (2 points)

    Write the correct syntax to start an if statement that checks if a
    variable `score` is greater than or equal to 90.

    ```python
    _____ score _____ 90 _____
        print("Grade A")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Problem 3 (2 points)

    *True or False*: In nested if statements, the inner if statement will
    always execute.

    *Circle ONE answer:*     TRUE     FALSE
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### Problem 4 (2 points)

    What will this code print?

    ```python
    age = 25
    if age >= 18:
        if age >= 65:
            status = "Senior"
        else:
            status = "Adult"
    else:
        status = "Minor"
    print(status)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### Problem 5 (2 points)

    Out of the three code snippets below, circle every one that prints more
    than one line when `x = 10`.

    **Snippet A**
    ```python
    if x > 5:
        print("A")
    elif x > 8:
        print("B")
    ```

    **Snippet B**
    ```python
    if x > 5:
        print("A")
    if x > 8:
        print("B")
    ```

    **Snippet C**
    ```python
    if x > 8:
        print("B")
    elif x > 5:
        print("A")
    ```
    ''')
    return


if __name__ == "__main__":
    app.run()
