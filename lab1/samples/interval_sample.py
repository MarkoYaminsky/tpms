from math import log10, sqrt

from matplotlib import pyplot as plot

from tools.decorators import rounded
from tools.utils import print_table, show_plot
from .discrete_sample import DiscreteSample


class Interval:
    def __init__(self, start, end, values_amount, is_last=False):
        self.start = start
        self.end = end
        self.values_amount = values_amount
        self.is_last = is_last

    def __str__(self):
        return f"[{self.start}, {self.end}" + ("]" if self.is_last else ")")

    def __contains__(self, item):
        return self.start <= item < self.end

    @property
    def middle(self):
        return (self.start + self.end) / 2


class IntervalSample:
    def __init__(self, sample: DiscreteSample):
        self.discrete_sample = sample
        self.interval_sample = self.get_interval_sample()

    def __str__(self):
        return str(self.interval_sample)

    @property
    def interval_amount(self):
        return round(1 + 3.2 * log10(len(self.discrete_sample)))

    @property
    def interval_size(self):
        return self.discrete_sample.range // self.interval_amount

    @property
    def mode(self):
        sorted_sample = sorted(
            self.interval_sample.items(), key=lambda x: x[1], reverse=True
        )
        return sorted_sample[0][0]

    @property
    @rounded
    def median(self):
        middle_interval: Interval = list(self.interval_sample.items())[
            len(self.interval_sample) // 2
            ][0]
        print("середній: ", middle_interval)
        return middle_interval.start + (middle_interval.end - middle_interval.start) / middle_interval.values_amount * (
                len(self.discrete_sample) / 2
                - self.get_sum_of_values_before_point(middle_interval.start)
        )

    @property
    @rounded
    def mean(self):
        return sum(
            [
                interval.middle * interval.values_amount
                for interval in self.interval_sample
            ]
        ) / len(self.discrete_sample)

    @property
    @rounded
    def variance(self):
        return self.get_central_empirical_moment(2)

    @property
    @rounded
    def standard_deviation(self):
        return sqrt(self.variance)

    @property
    @rounded
    def variation_coefficient(self):
        return self.standard_deviation / self.mean

    @property
    @rounded
    def skewness(self):
        return self.get_central_empirical_moment(3) / self.standard_deviation ** 3

    @property
    @rounded
    def kurtosis(self):
        return self.get_central_empirical_moment(4) / self.standard_deviation ** 4 - 3

    def get_interval_sample(self, end=None):
        if not end:
            end = self.discrete_sample.max
        interval_sample = {}
        interval_start = self.discrete_sample.min
        while (interval_end := interval_start + self.interval_size) <= end:
            values_amount = 0
            is_last = interval_end == self.discrete_sample.max
            for key in range(interval_start, interval_end + (1 if is_last else 0)):
                values_amount += self.discrete_sample.stats.get(key, 0)
            interval_sample[
                Interval(interval_start, interval_end, values_amount, is_last)
            ] = values_amount
            interval_start = interval_end
        return interval_sample

    def get_sum_of_values_before_point(self, point):
        return sum([item[1] for item in self.get_interval_sample(point).items()])

    def build_table(self):
        print_table(
            [
                ["∆j", *self.interval_sample.keys()],
                ["Nj", *self.interval_sample.values()],
            ]
        )

    def draw_frequency_histogram(self):
        data = zip(
            *[
                (interval.start, interval.values_amount)
                for interval in self.interval_sample.keys()
            ],
            (self.discrete_sample.max, self.discrete_sample.stats[self.discrete_sample.max])
        )
        plot.bar(*data, width=self.interval_size - 0.08)
        show_plot("Гістограма частот")

    def draw_empirical_distribution_function(self):
        interval_starts = [*[interval.start for interval in self.interval_sample.keys()], self.discrete_sample.max]
        cumulative_sum = [
            self.get_sum_of_values_before_point(point) for point in interval_starts
        ]
        plot.plot(interval_starts, cumulative_sum)
        show_plot("Емпірична функція розподілу")

    @rounded
    def get_central_empirical_moment(self, order):
        return sum(
            [
                (interval.middle - self.mean) ** order * interval.values_amount
                for interval in self.interval_sample
            ]
        ) / len(self.discrete_sample)
