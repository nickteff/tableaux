import time
from itertools import permutations
from math import factorial
from multiprocessing import Pool
from typing import Any, List

import matplotlib.pyplot as plt
import pandas as pd
from descent import descent_algo
from perms import desc


def code_shape(c: List[int]) -> List[int]:
    """
    Calculate the shape of a given code.

    Args:
      c: A list of integers representing the code.

    Returns:
      A list of integers representing the shape of the code.
    """
    d = {j: 0 for j in range(len(c))}
    for i in c:
        d[i] += 1
    return sorted([d[i] for i in d if d[i] > 0], reverse=True)


def worker(ww: List[int]) -> List[str]:
    """
    Perform the descent algorithm on a given permutation.

    Args:
      ww: A list of integers representing the permutation.

    Returns:
      A list containing the permutation, code, index, and descents.
    """
    code, index = descent_algo(ww)
    return [ww, str(code), str(index), desc(ww)]


def de_stringer(code: str) -> List[int]:
    """
    Convert a string representation of a code to a list of integers.

    Args:
      code: A string representation of the code.

    Returns:
      A list of integers representing the code.
    """
    return [int(i) for i in code[1:-1].split(",")]


def createFigure(w: List[int]) -> Any:
    """
    Create a figure for plotting a permutation.

    Args:
      w: A list of integers representing the permutation.

    Returns:
      The created figure.
    """
    n = len(w)
    fig, ax = plt.subplots(figsize=(0.75, 0.75))
    ax.axis([0.5, n + 0.5, 0.5, n + 0.5])
    ax.axis("off")
    ax.plot(range(1, n + 1), w, "k", marker="o")
    return fig


def mapping(w: List[int]) -> str:
    """
    Generate the HTML code for displaying a mapping of a permutation.

    Args:
      w: A list of integers representing the permutation.

    Returns:
      The HTML code for displaying the mapping.
    """
    w = list(w)
    fname = "../img/map_{}.png".format(w)
    imgstr = '<img src="{}" /> '.format(fname)
    return imgstr


def save_mapping(df: pd.DataFrame, n: int) -> None:
    """
    Save the mapping of permutations to HTML and CSV files.

    Args:
      df: A DataFrame containing the permutations and their properties.
      n: The size of the permutations.

    Returns:
      None
    """
    for w in df.perm.values:
        w = list(w)
        fig = createFigure(w)
        fname = "../img/map_{}.png".format(w)
        fig.savefig(fname)
        plt.close(fig)

    df = df.assign(plot=df.perm.apply(mapping))
    df.to_html(
        "../output/decent_map_{}.html".format(n),
        escape=False,
        index=False,
        table_id="table_id",
    )

    df.loc[:, ["perm", "code", "increasing_code", "index", "descents", "shape"]].to_csv(
        "../output/decent_map_{}.csv".format(n), index=False
    )

    with open("../output/decent_map_{}.html".format(n), mode="r") as f:
        html = f.read()
        html = HEAD + html + TAIL

    with open("../output/decent_map_{}.html".format(n), mode="w") as g:
        g.write(html)


HEAD = """
<html>

<head>
  <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous">
  </script>
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.css">

  <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.js"></script>
  <script>
  $(document).ready(function() {
    var table = $('#table_id').DataTable(); // Initialize your DataTable

    // Add event listeners to the input boxes
    $('input').on('keyup', function() {
    var column = this.id;
    var value = this.value;

    // Search the column for the exact match
    table.column(column).search(value).draw();
    });
  });
  </script>
</head>

<body>
  <table class="inputs">
  <tbody>
    <tr>
    <td>Permutations:</td>
    <td><input type="text" id="0" name="perm"></td>
    </tr>
    <tr>
    <td>Increasing Codes:</td>
    <td><input type="text" id="4" name="code"></td>
    </tr>
    <tr>
    <td>Shape:</td>
    <td><input type="text" id="5" name="shape"></td>
    </tr>
    <tr>
    <td>Indices:</td>
    <td><input type="text" id="2" name="index"></td>
    </tr>
    <tr>
    <td>Descents:</td>
    <td><input type="text" id="3" name="descent"></td>
    </tr>
  </tbody>
  </table>
"""

TAIL = """
</body>

</html>"""

if __name__ == "__main__":
    for n in range(2, 6):
        t = time.time()
        id = range(1, n + 1)
        with Pool() as p:
            data = p.map(worker, permutations(id))
        df = pd.DataFrame(data, columns=["perm", "code", "index", "descents"])
        if n <= 7:
            df = df.assign(
                increasing_code=df.code.apply(de_stringer).apply(sorted),
                shape=df.code.apply(de_stringer).apply(code_shape),
            )
            save_mapping(df, n)
        print(
            n,
            df.loc[:, ["code", "index"]].drop_duplicates().shape[0],
            factorial(n),
            round(time.time() - t, 2),
        )
