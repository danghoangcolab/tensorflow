import tensorflow as tf
from tensorflow.data import Dataset
import os
import glob
from pathlib import Path
import numpy as np
from imutils import paths
import matplotlib.pyplot as plt



class DataLoader(object):
    def __init__(self, folder_contain_data, batch_size=32, argument_data=True,
    one_hot_end_coder=True, *args, **kwargs):
        self.folder_contain_data = folder_contain_data
        self.batch_size = batch_size
        self.class_name = None
        self.one_hot_endcoder = one_hot_end_coder
        self.width = width
        self.height = height

    
    def get_label(self, file_path):
        parts = tf.strings.split(path_file, os.path.sep)
        label = parts[2] == self.class_name
        if one_hot_end_coder:
            label = tf.one_hot(label)
            return label
        else:
            return label 
    
    def decode_image(self, img, channels=3):
        img = tf.image.decode_jpeg(img, channels=channels)
        #convert data to float32 in rang[0, 1]
        img = tf.image.convert_image_dtype(img, tf.float32)
        #resize img to size set in contructor
        img = tf.image.resize(img, size=(self.height, self.width))
        return img
    
    def process_path(file_path):
        img = tf.io.read_file(file_path)
        label = self.get_label(file_path)
        img = self.decode_image(img)
        return img, label
        
    def get_class_name(self):
        path = Path(self.folder_contain_data)
        self.class_name = np.array([item.name for item in path.glob("test/*/**")])
        return 
    
    def info_ds(self):
        total_image = len(list(paths.list_images(self.folder_contain_data)))
        print("Total image have in dataset is :", total_image)

        folder = ["train", "test", "pre"]
        data_in_subfolder = dict()
        for i in folder:
            folder_name = os.path.join(self.folder_contain_data, i)
            total = len(list(paths.list_images(folder_name)))
            data_in_subfolder[i] = total
            print("Total image in {} folder is: {}".format(i, total))
        
        return total_image, data_in_subfolder
        
        
    
    
    def visualize_data(self):
        total_image, data_in_subfolder = self.info_ds()
        data_in_subfolder["total"] = total_image

        #plot data
        fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharey=True)
        names = data_in_subfolder.keys()
        
        







            
            

        