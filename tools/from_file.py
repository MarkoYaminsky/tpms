from abc import ABC, abstractmethod


class FromFile(ABC):
    def get_data(self, file_name):
        with open(file_name) as task:
            return [float(element) for element in task.readline().split()]
