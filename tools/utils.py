from tabulate import tabulate
from matplotlib import pyplot as plot


def print_table(data):
    table = tabulate(data, tablefmt="fancy_grid")
    print(table)


def show_plot(title):
    plot.xlabel("Значення")
    plot.ylabel("Частота")
    plot.title(title)
    plot.show()
