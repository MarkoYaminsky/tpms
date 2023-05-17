from collections import Counter

from matplotlib import pyplot as plot

from tools.decorators import rounded
from tools.utils import print_table, show_plot


class DiscreteSample:
    def __init__(self):
        self.sample = self.get_data_from_file()
        self.stats = Counter(self)

    def __iter__(self):
        return iter(self.sample)

    def __getitem__(self, item):
        return self.sample[item]

    def __len__(self):
        return len(self.sample)

    def __str__(self):
        return ", ".join([str(element) for element in self])

    def get_data_from_file(self):
        with open("data") as file:
            joined_data_string = "".join(file.readlines())
            return [int(element) for element in joined_data_string.split()]

    @property
    def min(self):
        return min(self)

    @property
    def max(self):
        return max(self)

    @property
    def range(self):
        return self.max - self.min

    @property
    def mode(self):
        sample_stats = Counter(self)
        sorted_by_frequency = sample_stats.most_common()
        biggest_occurancy_count = sorted_by_frequency[0][1]
        return [
            element
            for element, count in sample_stats.items()
            if count == biggest_occurancy_count
        ]

    @property
    def median(self):
        length = len(self)
        return (
            self[length // 2]
            if length % 2
            else (self[length // 2] + self[length // 2 - 1]) / 2
        )

    @property
    @rounded
    def mean(self):
        return sum(self.sample) / len(self.sample)

    def order(self):
        self.sample.sort()

    def get_sorted_frequency_dict(self, by: str):
        ordered_stats = sorted(
            self.stats.most_common(), key=lambda x: x[0 if by == "x" else 1]
        )
        return dict(ordered_stats)

    def get_paginated_table_data(
        self,
        row_titles,
        rows_data,
        half,
    ):
        rows_data = [list(row) for row in rows_data]
        ordered_stats = self.get_sorted_frequency_dict("x")
        middle = len(ordered_stats) // 2
        is_first_half = half == "first"
        data = [
            [
                row_title,
                *row_data[
                    middle
                    if not is_first_half
                    else 0 : middle
                    if is_first_half
                    else None
                ],
            ]
            for row_title, row_data in zip(row_titles, rows_data)
        ]
        return data

    def build_sample_table(self):
        sorted_data = self.get_sorted_frequency_dict("x")
        second_row_data = sorted_data.values()
        for half in ("first", "second"):
            paginated_data = self.get_paginated_table_data(
                row_titles=["Xi", "Ni", "Wi"],
                rows_data=[
                    sorted_data.keys(),
                    second_row_data,
                    (element / 100 for element in second_row_data),
                ],
                half=half,
            )
            print_table(paginated_data)

    def get_plot_items(self):
        frequencies_dict = self.get_sorted_frequency_dict("x")
        return frequencies_dict.keys(), frequencies_dict.values()

    def draw_frequency_graph(self):
        plot.plot(*self.get_plot_items())
        show_plot("Полігон частот")
