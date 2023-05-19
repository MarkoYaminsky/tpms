from samples.interval_sample import BaseIntervalSample


class Lab2IntervalSample(BaseIntervalSample):
    def __init__(self):
        self.interval_size, self.interval_confidence = self.get_data_from_file()

    @property
    def variance(self):
        ...

    @property
    def interval_sample(self):
        ...

    def get_data_from_file(self):
        with open("task1") as task:
            data = task.readline()
            return (float(element) for element in data.split())

    def __len__(self):
        pass

    def get_sample_from_file(self):
        ...
