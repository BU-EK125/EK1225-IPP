import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class6_IPP.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Class 6 IPP

    Name: _________________________________________________
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### 1.

    In the space under the following, show what would be printed.

    ```python
    for i in range(2):
        print('*', end='')
        for j in range(3):
            print('#', end='')
        print()
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### 2.

    For the following code, write down exactly what this program prints.
    Be careful with spaces and line breaks:

    ```python
    for i in range(1, 4):
        for j in range(1, 4):
            if i == j:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()
    ```
    ''')
    return


if __name__ == "__main__":
    app.run()
