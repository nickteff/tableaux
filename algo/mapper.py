import matplotlib.pyplot as plt

def code_shape(c):
    d = {j:0 for j in range(len(c))}
    for i in c:
        d[i] += 1
    return sorted([d[i] for i in d if d[i] > 0], reverse=True)

def createFigure(w):
    n = len(w)
    fig, ax = plt.subplots(figsize=(.75,.75))
    ax.axis([0.5,n+.5,0.5,n+.5])
    ax.axis("off")
    ax.plot(range(1,n+1), w, 'k', marker='o')
    return fig

def mapping(w):
    w = list(w)
    fname = "../img/map_{}.png".format(w)
    imgstr = '<img src="{}" /> '.format(fname)
    return imgstr

def save_mapping(df, n):
    for w in df.perm.values:
        w = list(w)
        fig = createFigure(w)
        fname = "../img/map_{}.png".format(w)
        fig.savefig(fname)
        plt.close(fig)

    df = df.assign(plot = df.perm.apply(mapping))
    df.to_html(
    'decent_map_{}.html'.format(n), 
    escape=False, 
    index=False, 
    table_id="table_id")
        
    df.loc[:, [
        'perm', 
        'code', 
        'index', 
        'shape']].to_csv(
            'decent_map_{}.csv'.format(n),
            index=False)

    with open('decent_map_{}.html'.format(n), mode="r") as f:
        html = f.read()
        html = HEAD + html + TAIL

    with open('decent_map_{}.html'.format(n), mode="w") as g:
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
      $('#table_id').DataTable();
    });
  </script>
</head>

<body>
"""

TAIL = """
</body>

</html>"""