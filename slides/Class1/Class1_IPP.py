import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class1_IPP.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Class 1 Individual Practice Problems

    Please remember to put your name on your paper and number your answers.

    *Write what the result of each expression would be.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### 1.

    ```python
    >>> mynum = 3 + 5
    >>> mynum
    ```

    Answer: _________________________________________________
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### 2.

    ```python
    >>> numb = 3 ** 2
    >>> numb
    ```

    Answer: _________________________________________________
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### 3.

    ```python
    >>> round(4.51)
    ```

    Answer: _________________________________________________
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### 4.

    ```python
    >>> 2e3
    ```

    Answer: _________________________________________________
    ''')
    return


if __name__ == "__main__":
    app.run()
