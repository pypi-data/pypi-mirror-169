from __future__ import annotations
import numpy
import torch
import torch.utils.data
from typing import Union
from typing import Tuple
from math import isnan
from copy import deepcopy
from ailca.core.operation import sublist
from ailca.core.operation import split_list
from ailca.core.operation import merge_lists
from ailca.data.base import Dataset


class MultimodalDataset(torch.utils.data.Dataset):
    """
    A dataset class to store heterogeneous datasets for multimodal learning.
    """

    def __init__(self,
                 datasets: list,
                 targets: torch.Tensor = None):
        self.datasets = datasets
        self.y = None if targets is None else targets
        self.data = list()

        for i in range(0, len(self.datasets[0])):
            self.data.append([dataset.data[i] for dataset in self.datasets])

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self,
                    idx: int) -> Union[Tuple[list, None], Tuple[list, torch.Tensor]]:
        if self.y is None:
            return [d.x for d in self.data[idx]], None
        else:
            return [d.x for d in self.data[idx]], self.y[idx]

    @property
    def idx_data(self):
        return self.datasets[0].idx_data

    @property
    def tooltips(self):
        return self.datasets[0].tooltips

    def clone(self,
              x: list = None,
              y: torch.Tensor = None) -> MultimodalDataset:
        """
        Generate a clone of the dataset.
        If new data is given through ``x``, a new dataset with copied metadata is generated.

        :param x: (*list, optional*) New data to be stored the copied dataset (*default* = ``None``).
        :param y: (*torch.Tensor*) New target data (*default* = ``None``).
        :return: (*MultimodalDataset*) A copied dataset.
        """

        if x is None:
            return deepcopy(self)
        else:
            new_datasets = list()
            for i in range(0, len(self.datasets)):
                new_datasets.append(Dataset([d[i] for d in x]))

            return MultimodalDataset(new_datasets, y)

    def split(self,
              ratio_train: float,
              ratio_val: float = None,
              random_seed: int = None) -> Union[Tuple[MultimodalDataset, MultimodalDataset],
                                                Tuple[MultimodalDataset, MultimodalDataset, MultimodalDataset]]:
        """
        Split the dataset into three sub-datasets.
        If ``ratio_val`` is ``None``, the original dataset is divided into two sub-datasets.

        :param ratio_train: (*float*) A ratio of the number of data in the training dataset.
        :param ratio_val: (*float, optional*) A ratio of the number of data in the validation dataset (*default* = ``None``).
        :param random_seed: (*int, optional*) A random seed to split the dataset (*default* = ``None``).
        :return: (*Union[Tuple[MultimodalDataset, MultimodalDataset],
        Tuple[MultimodalDataset, MultimodalDataset, MultimodalDataset]]*) Two sub-datasets of the original dataset.
        """

        if random_seed is not None:
            numpy.random.seed(random_seed)

        idx_rand = numpy.random.permutation(len(self))
        n_data_train = int(ratio_train * len(self))

        if ratio_val is None:
            new_data_train = sublist(self.data, idx_rand[:n_data_train])
            new_data_test = sublist(self.data, idx_rand[n_data_train:])

            if self.y is None:
                dataset_train = self.clone(x=new_data_train)
                dataset_test = self.clone(x=new_data_test)
            else:
                dataset_train = self.clone(x=new_data_train, y=self.y[idx_rand[:n_data_train]])
                dataset_test = self.clone(x=new_data_test, y=self.y[idx_rand[n_data_train:]])

            return dataset_train, dataset_test
        else:
            n_data_val = int(ratio_val * len(self))
            new_data_train = sublist(self.data, idx_rand[:n_data_train])
            new_data_val = sublist(self.data, idx_rand[n_data_train:n_data_train+n_data_val])
            new_data_test = sublist(self.data, idx_rand[n_data_train+n_data_val:])

            if self.y is None:
                dataset_train = self.clone(x=new_data_train)
                dataset_val = self.clone(x=new_data_val)
                dataset_test = self.clone(x=new_data_test)
            else:
                dataset_train = self.clone(x=new_data_train, y=self.y[idx_rand[:n_data_train]])
                dataset_val = self.clone(x=new_data_val, y=self.y[idx_rand[n_data_train:n_data_train+n_data_val]])
                dataset_test = self.clone(x=new_data_test, y=self.y[idx_rand[n_data_train+n_data_val:]])

            return dataset_train, dataset_val, dataset_test

    def save(self,
             path: str):
        """
        Save the dataset in a given ``path``.

        :param path: (*str*) Path of the saved dataset.
        """

        torch.save(self, path)

    @staticmethod
    def load(path: str) -> MultimodalDataset:
        """
        Load the dataset from a given ``path``.

        :param path: (*str*) Path of the dataset.
        :return: (*MultimodalDataset*) A dataset object.
        """

        return torch.load(path)

    def complete(self) -> MultimodalDataset:
        """
        Remove the data of the missing values in the target data.

        :return: (*MultimodalDataset*) A refined dataset without missing values in the target data.
        """

        new_data = list()
        new_targets = list()

        for i in range(0, self.y.shape[0]):
            if not isnan(self.y[i]):
                new_data.append(self.data[i])
                new_targets.append(self.y[i])

        return self.clone(x=new_data, y=torch.vstack(new_targets))

    def get_k_folds(self,
                    k: int,
                    random_seed: int = None) -> list:
        """
        Generate ``k`` subsets of the dataset for k-fold cross-validation.

        :param k: (*int*) The number of subsets for k-fold cross-validation.
        :param random_seed: (*int, optional*) An integer index of the random seed (*default* = ``None``).
        :return: (*list*) A list of the k-folds.
        """

        if random_seed is not None:
            numpy.random.seed(random_seed)

        # Split the dataset into k subsets.
        idx_rand = numpy.array_split(numpy.random.permutation(len(self.data)), k)
        sub_data = split_list(self.data, k, idx_rand=idx_rand)
        sub_targets = [self.y[idx] for idx in idx_rand]
        k_folds = list()

        # Generate k tuples of the training and test datasets from the k subsets.
        for i in range(0, k):
            data_train = merge_lists(sub_data[:i], sub_data[i+1:])
            targets_train = torch.vstack(merge_lists(sub_targets[:i], sub_targets[i+1:]))
            data_test = sub_data[i]
            targets_test = sub_targets[i]
            dataset_train = self.clone(x=data_train, y=targets_train)
            dataset_test = self.clone(x=data_test, y=targets_test)
            k_folds.append([dataset_train, dataset_test])

        return k_folds
