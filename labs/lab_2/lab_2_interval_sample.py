from math import sqrt

from samples.interval_sample import BaseIntervalSample, Interval
from numpy import arange

from tools.decorators import rounded
from tools.from_file import FromFile
from tools.utils import print_table


class Lab2IntervalSample(BaseIntervalSample, FromFile):
    def __init__(self, rows_names: list[str]):
        (
            self.counting_start,
            self.interval_size,
            self.t,
            self.q,
        ) = self.get_data("task1")
        self.rows_names = rows_names

    def __len__(self):
        return sum(self.interval_sample.values())

    @property
    def assessment_accuracy(self):
        accuracy = round(self.standard_deviation / sqrt(len(self)) * self.t, 2)
        mean = self.mean
        left_side, right_side = [
            round(element, 2) for element in (mean - accuracy, mean + accuracy)
        ]
        return f"{left_side} < a < {right_side}"

    @property
    def confidence_interval(self):
        deviation = self.standard_deviation
        left_side, right_side = [
            round(deviation * value, 2) for value in [1 - self.q, 1 + self.q]
        ]
        return f"({max(0, left_side)}; {right_side})"

    @property
    @rounded
    def variance(self):
        return sum(
            [
                interval.middle**2 * interval.values_amount
                for interval in self.interval_sample
            ]
        ) / (len(self) - 1) - self.mean**2 * len(self) / (len(self) - 1)

    @property
    def interval_sample(self):
        with open("task1") as task:
            interval_values = iter(task.readlines()[1].split())
        interval_sample = {}
        for interval_start in arange(
            self.counting_start,
            counting_end := self.counting_start + 7 * self.interval_size,
            self.interval_size,
        ):
            values_amount = int(next(interval_values))
            is_last = interval_start == counting_end - self.interval_size
            interval_sample[
                Interval(
                    interval_start,
                    interval_start + self.interval_size,
                    values_amount,
                    is_last,
                )
            ] = values_amount
        return interval_sample

    def build_table(self, rows_names=None):
        if not rows_names:
            rows_names = self.rows_names
        return super().build_table(rows_names)

    def build_discrete_sample_table(self):
        print_table(
            [
                [
                    self.rows_names[0],
                    *[interval.middle for interval in self.interval_sample.keys()],
                ],
                [self.rows_names[1], *self.interval_sample.values()],
            ]
        )
