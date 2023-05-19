from abc import ABC, abstractmethod
from math import sqrt

from tools.decorators import rounded


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


class BaseIntervalSample(ABC):
    def __str__(self):
        return str(self.interval_sample)

    @property
    @abstractmethod
    @rounded
    def variance(self):
        ...

    @property
    @abstractmethod
    def interval_sample(self):
        ...

    @abstractmethod
    def __len__(self):
        ...

    @property
    @rounded
    def mean(self):
        return sum(
            [
                interval.middle * interval.values_amount
                for interval in self.interval_sample
            ]
        ) / len(self)

    @property
    @rounded
    def standard_deviation(self):
        return sqrt(self.variance)
