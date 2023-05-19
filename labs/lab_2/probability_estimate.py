from math import sqrt

from tools.decorators import rounded
from tools.from_file import FromFile


class ProbabilityEstimate(FromFile):
    def __init__(self):
        self.total_event_amount, self.successful_event_amount, self.t = self.get_data(
            "task2"
        )

    @property
    @rounded
    def relative_frequency(self):
        return self.successful_event_amount / self.total_event_amount

    @property
    def confidence_interval(self):
        relative_frequency = self.relative_frequency
        deviation = round(
            self.t
            * sqrt(
                relative_frequency / self.total_event_amount * (1 - relative_frequency)
                + (self.t / (2 * self.total_event_amount)) ** 2
            ),
            2,
        )
        left_side, right_size = [
            round(
                self.total_event_amount
                / (self.t**2 + self.total_event_amount)
                * (
                    relative_frequency
                    + getattr(self.t**2 / (2 * self.total_event_amount), function)(
                        deviation
                    )
                ),
                2,
            )
            for function in ("__sub__", "__add__")
        ]
        return f"{left_side} < p < {right_size}"
