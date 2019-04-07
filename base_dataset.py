"""
File: base_dataset.py
Author: VDeamoV
Email: vincent.duan95@outlook.com
Github: https://github.com/VDeamoV
Description:
    Use to load data, can be use to create meta-dataset
"""
from __future__ import print_function
import os

import yaml
import torch.utils.data as data


class BaseCustomDataset(data.Dataset):
    """
    BaseCustomDataset:
        Provide the fundamental method for other dataset
        Basic function is following below:
            1. Configurae Dataset with yml file
            2. Output Dataset Configure
            3. Basic Analysis the Dataset

    Example yaml:
        ```
        # yaml_file
        info:
            name: 'example_name'
            data_type: 'image' # image or other types will support later

        directory:
            root_dir:

        preprocess:
            transforms:
                transform_list: ['Scale']
                image_size: 224
            transforms_target:
                transform_list: []

        ```
    """

    def __init__(self, yml_file_path):
        super(BaseCustomDataset, self).__init__()
        try:
            with open(yml_file_path, 'r') as config_file:
                params = yaml.load(config_file)
        except FileNotFoundError as error:
            print(error)
        finally:
            print("===yml load success ===")

        self.params = params
        self.name = params['info']['name']
        self.data_type = params['info']['data_type']

        self.root_dir = params['directory']['root_dir']

        self.transforms = params['preorocess']['transforms']
        self.transforms_target = params['preorocess']['transforms_target']

    def __getitem__(self, index):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def config_output(self):
        """
        Output the configure information
        """
        print("======info=======")
        print("Dataset Name: ", self.name)
        print("Data_type: ", self.data_type)
        print("====directory====")
        print("root_dir: ", self.root_dir)
        print("===preorocess===")
        print("transforms: ", self.transforms)
        print("transforms_target: ", self.transforms_target)

    def pre_analyse(self):
        """
        Use to pre_analyse the dataset

        Output:
            1. How many classes
            2. How many samples each class
        """
        #  TODO:  <07-04-19, VDeamoV> #
        raise NotImplementedError



class CustomImageDataset(BaseCustomDataset):
    """
    CustomImageDataset:
        Load Image in the custom folder
        Basic function is folllowing below:
    """

    def __init__(self, yml_file_path):
        super(CustomImageDataset, self).__init__()

    def __getitem__(self, index):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
