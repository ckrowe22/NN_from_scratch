from enum import Enum
import collections
import numpy as np
import random

XOR_features = [[0, 0], [0, 1], [1, 0], [1, 1]]
XOR_labels = [[0], [1], [1], [0]]


class Order(Enum):
    """Creating Order Enum class."""
    SHUFFLE = 1
    STATIC = 2


class Set(Enum):
    """Creating Set Enum class."""
    TRAIN = 1
    TEST = 2


class NNData:
    """Creating NNData Class."""

    def __init__(self, features=None, labels=None, train_factor=.9):
        if features is None:
            self._features = []
        else:
            self._features = None

        if labels is None:
            self._labels = []
        else:
            self._labels = None

        self._train_factor = NNData.percentage_limiter(train_factor)
        self._train_indices = []
        self._test_indices = []
        self._train_pool = collections.deque([])
        self._test_pool = collections.deque([])
        self.load_data(features, labels)

    @staticmethod
    def percentage_limiter(percentage: float):
        """Keeps percentage between 0 and 1."""
        if percentage < 0:
            return 0
        elif percentage > 1:
            return 1
        else:
            return percentage

    def load_data(self, features=None, labels=None):
        """Loads features and data to determine if """
        if features is None or labels is None:
            self._features = None
            self._labels = None
            return self.spilt_set()
            #return
        if len(features) != len(labels):
            self._features = None
            self._labels = None
            self.split_set()
            raise ValueError('The length of Features and Labels do not match.')
        try:
            self._features = np.array(features, dtype=float)
            self._labels = np.array(labels, dtype=float)
        except Exception:
            self._features = None
            self._labels = None
            self.split_set()
            raise ValueError("Failed to create numpy arrays from features and labels")
        self.split_set()

    def split_set(self, new_train_factor=None):
        """Splits dataset into testing and training data."""
        if new_train_factor is not None:
            self._train_factor = self.percentage_limiter(new_train_factor)
        num_examples_loaded = len(self._features) if self._features is not None else 0
        train_size = int(num_examples_loaded * self._train_factor)
        self._train_indices = random.sample(range(num_examples_loaded), train_size)
        self._test_indices = [i for i in range(num_examples_loaded) if i not in self._train_indices]

    def prime_data(self, target_set=None, order=None):
        if target_set is None:
            target_set = [Set.TRAIN, Set.TEST]
        elif isinstance(target_set, Set):
            target_set = [target_set]

        for i in target_set:
            if i == Set.TRAIN:
                pool = self._train_pool
                indices = self._train_indices
            else:
                pool = self._test_pool
                indices = self._test_indices
            pool.clear()
            pool.extend(indices)
            if order == Order.SHUFFLE:
                random.shuffle(pool)

    def get_one_item(self, target_set=None):
        """Returns a feature-label pair as a tuple."""
        pool = None
        if target_set == Set.TRAIN or target_set is None:
            pool = self._test_pool
        elif target_set == Set.TEST:
            pool = self._test_pool
        if not pool:
            return None
        index = pool.popleft()
        return self._features[index], self._labels[index]

    def number_of_samples(self, target_set=None):
        """Returns a count of the total number of training or testing examples."""
        if target_set is None:
            return len(self._train_indices) + len(self._test_indices)
        elif target_set == Set.TRAIN:
            return len(self._train_indices)
        elif target_set == Set.TEST:
            return len(self._test_indices)

    def pool_is_empty(self, target_set=None):
        """Determines if the training pool is empty."""
        if target_set is None:
            target_set = Set.TRAIN
        if target_set == Set.TRAIN:
            return not self._train_pool
        elif target_set == Set.TEST:
            return not self._test_pool
