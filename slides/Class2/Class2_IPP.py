import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class2_IPP.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Class 2 Individual Practice Problems

    *Multiple choice.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 1. Which of these creates a tuple with a single item?

    a. `(42)`     b. `(42,)`     c. `[42]`     d. `"42"`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 2. True or False: All *sequences* in Python can be indexed using square brackets.

    a. True     b. False
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 3. What method would you use to add an item to the end of a list?

    a. `insert()`     b. `append()`     c. `add()`     d. `push()`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 4. Which sequence type should you use for storing GPS coordinates that won't change?

    a. String     b. List     c. Tuple     d. Any of these work
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Answers

    B, A, B, C
    """)
    return


if __name__ == "__main__":
    app.run()
