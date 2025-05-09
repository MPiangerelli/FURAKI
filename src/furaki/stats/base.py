from abc import ABC, abstractmethod
from typing import List

from ..base import Subject, Observer

class StatsTracker(Subject):

    """Class that computes and stores summaries of data both categorical or numerical"""
    def __init__(self, observed_features=None) -> None:
        self.feature_indices = []
        self.feature_names = []
        self.n_points = 0
        for i, f in observed_features:
            self.feature_indices.append(i)
            self.feature_names.append(f)
        self.n_features = len(observed_features)
        self.size=None
        self.kernel = None

        self._state: float = None
        self._observers: List[Observer] = []


    def attach(self, observer: Observer) -> None:
        # print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        for observer in self._observers:
            observer.update(self)


    @abstractmethod
    def update(self, x):
        """Update summary statistics"""
        pass

    @abstractmethod
    def get_threshold(self, x):
        pass

    @abstractmethod
    def getmean(self):
        pass

    @abstractmethod
    def getvar(self):
        pass

    @abstractmethod
    def getcov(self):
        pass

    @abstractmethod
    def getpdf(self, support):
        pass

    def reset(self):
        self.n_points = 0
