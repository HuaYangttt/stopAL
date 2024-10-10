"""
Author: Hua Yang
Email: yanghuattt@gmail.com
Date: 10/09/2024
Description: loading data from tim's
"""

import os
import yaml
import numpy as np
import os.path as osp

# get the data_list from dataset_info.yaml
try:
    with open('./dataset_info.yaml', 'r') as file:
        data = yaml.safe_load(file)
        dataset_info_dict = {dataset['name']: dataset['path'] for dataset in data['datasets']}
except FileNotFoundError:
    print('dataset_info.yaml not found, please use make file command to generate it')

Tims_datasets_61 = ['pom3d', 'pom3a', 'coc1000', 'xomo_ground', 'pom3b', 'xomo_osp', 'nasa93dem', 'pom3c', 
'xomo_osp2', 'xomo_flight', 'Wine_quality', 'auto93', 'FFM-1000-200-0.50-SAT-1', 
'FFM-500-100-0.50-SAT-1', 'Scrum1k', 'Scrum10k', 'billing10k', 'Scrum100k', 
'FFM-125-25-0.50-SAT-1', 'FM-500-100-1.00-SAT-1', 'FM-500-100-0.75-SAT-1', 
'FM-500-100-0.50-SAT-1', 'FFM-250-50-0.50-SAT-1', 'FM-500-100-0.25-SAT-1', 
'SS-R', 'SQL_AllMeasurements', 'SS-J', 'SS-V', 'SS-M', 'rs-6d-c3_obj1', 'SS-B', 
'wc+wc-3d-c4-obj1', 'SS-K', 'HSMGP_num', 'sol-6d-c2-obj1', 'SS-G', 'wc-6d-c1-obj1', 
'SS-E', 'SS-D', 'SS-T', 'Apache_AllMeasurements', 'SS-N', 'wc+sol-3d-c4-obj1', 'wc+rs-3d-c4-obj1', 
'SS-O', 'SS-W', 'SS-X', 'X264_AllMeasurements', 'SS-C', 'SS-S', 'SS-I', 'SS-A', 'rs-6d-c3_obj2', 
'SS-P', 'SS-F', 'SS-L', 'SS-Q', 'SS-H', 'SS-U', 'healthCloseIsses12mths0001-hard', 
'healthCloseIsses12mths0011-easy']

tims_datasets_45 = []

class Data_se:
    
    


class Dataset_tims:
    def __init__(self, root, dataset_name):
        self.root = root
        self.dataset_name = dataset_name
    
    def load_dataset(self):
        """
        Load the dataset from the path
        """
        pass
        



def load_dataset(root, dataset_name):
    """
    
    """

    if dataset_name.lower() in list(datasets_name_list.lower()):
        path = dataset_info_dict[dataset_name]
