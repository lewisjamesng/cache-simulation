import matplotlib.pyplot as plt
import numpy as np

def make_graph(x, y, title):
    xs = np.array(x)
    ys = np.array(y)
    fig, ax = plt.subplots()
    ax.plot(xs, ys)

    ax.set(xlabel='Time (log10) (s)', ylabel='Cache hit ratio (%)', title=title)
    ax.grid()

    fig.savefig("test.png")
    plt.show()