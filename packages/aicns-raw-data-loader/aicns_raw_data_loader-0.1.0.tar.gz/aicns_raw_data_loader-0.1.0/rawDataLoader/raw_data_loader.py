"""
    Interface module for raw data loader that fetch speci
"""

from abc import ABCMeta, abstractmethod
from feature.featureCluster import FeatureCluster
from feature.feature import Feature
from typing import List


class RawDataLoader(metaclass=ABCMeta):
    """

    """

    @abstractmethod
    def prepare_to_load(self, **conn):
        pass

    @abstractmethod
    def load_data(self, start, end, clusters: List[FeatureCluster]):
        pass

    @abstractmethod
    def load_feature_data_by_object(self, start, end, feature: Feature):
        pass
