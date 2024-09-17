#!/usr/bin/env python
# coding: utf-8

# Find the data here:
# https://nemar.org/dataexplorer/detail?dataset_id=ds005420

# In[1]:


import os
import re
import mne
import warnings
import numpy as np
import matplotlib.pyplot as plt

from os.path import join

import pandas as pd
from tqdm import tqdm


# In[2]:


def process_eeg(eeg_data, sample_rate):
    # eeg_data.set_eeg_reference(ref_channels='average', projection=False, verbose=False)
    # eeg_data.resample(sample_rate, method='fft')
    return eeg_data


# In[3]:


pattern = r'sub-\d+'
path_data = 'eeg_data'
data_array_oc = []
data_array_oa = []
subject_ids = []
samplerate = 500  # The data is originally sampled at 500 Hz
invalid_indexes = []

for i, folder_name in tqdm(enumerate(os.listdir(path_data)), total=len(os.listdir(path_data))):
    if re.match(pattern, folder_name):
        subject_ids.append(folder_name)
        edf_path_oc = join(path_data, folder_name, "eeg", f"{folder_name}_task-oc_eeg.edf")
        edf_path_oa = edf_path_oc.replace('oc', 'oa')

        try:
            data = mne.io.read_raw_edf(edf_path_oc, preload=True, verbose=False)
            data_processed = process_eeg(data, samplerate)
            data_array_oc.append(data_processed)
        except FileNotFoundError:
            print(f'OC data missing for {folder_name}')
            data_array_oc.append(None)
            invalid_indexes.append(len(data_array_oc) - 1)

        try:
            data = mne.io.read_raw_edf(edf_path_oa, preload=True, verbose=False)
            data_processed = process_eeg(data, samplerate)
            data_array_oa.append(data_processed)
        except FileNotFoundError:
            print(f'OA data missing for {folder_name}')
            data_array_oa.append(None)
            invalid_indexes.append(len(data_array_oc) - 1)

        assert len(data_array_oc) == len(data_array_oa)

for i, index in enumerate(invalid_indexes):
    data_array_oc.pop(index - i)
    data_array_oa.pop(index - i)
    subject_ids.pop(index - i)


# In[4]:


def plot_raw_data(subject_ids, data_array_oc, data_array_oa, subject_slice, channel_slice, filter_values, plot_time,
                  average_psd=False):
    warnings.filterwarnings("ignore")
    for name, arr_oc, arr_oa in zip(subject_ids, data_array_oc[subject_slice], data_array_oa[subject_slice]):
        data_filtered_oc = arr_oc.copy().filter(*filter_values, fir_design='firwin', phase='zero', verbose=False).pick(
            channel_slice)
        if plot_time:
            print(f"OC for {name}")
            data_filtered_oc.plot()
        else:
            data_filtered_oc.compute_psd(verbose=False).plot(average=average_psd, picks="data", amplitude=False)
            plt.title(f"OC for {name}")
            plt.show()

        data_filtered_oa = arr_oa.copy().filter(*filter_values, fir_design='firwin', phase='zero', verbose=False).pick(
            channel_slice)
        if plot_time:
            print(f"OA for {name}")
            data_filtered_oa.plot()
        else:
            data_filtered_oa.compute_psd(verbose=False).plot(average=average_psd, picks="data", amplitude=False)
            plt.title(f"OA for {name}")
            plt.show()
    warnings.filterwarnings("default")


# In[5]:


channel_slice = slice(0, -1)
subject_slice = slice(1, 1)
filter_values = 1, 40
plot_raw_data(subject_ids, data_array_oc, data_array_oa, subject_slice, channel_slice, filter_values, plot_time=True)

# In[6]:


import warnings

channel_slice = slice(0, -1)
subject_slice = slice(1, 1)
filter_values = 1, 40

plot_raw_data(subject_ids, data_array_oc, data_array_oa, subject_slice, channel_slice, filter_values, plot_time=False)

# Calculate Alpha frequency

# In[7]:


filter_alpha = (8, 12)
channel_slice = slice(17, 19)
alphas_oc, alphas_oa = [], []
section_size = 300 * samplerate  # seconds * sample_rate

for name, data_oc, data_oa in tqdm(zip(subject_ids, data_array_oc, data_array_oa), total=len(subject_ids)):
    data_filtered_oc_alpha = data_oc.copy().filter(*filter_alpha, fir_design='firwin', phase='zero',
                                                   verbose=False).pick(channel_slice)
    data_filtered_oa_alpha = data_oa.copy().filter(*filter_alpha, fir_design='firwin', phase='zero',
                                                   verbose=False).pick(channel_slice)

    arr_oc = data_filtered_oc_alpha.get_data()
    acc_oa = data_filtered_oa_alpha.get_data()

    num_sections = arr_oc.shape[1] // section_size
    for i in range(1):
        alpha_oc = np.abs(data_filtered_oc_alpha.get_data()[:, i:(i + 1) * section_size]).mean()
        alpha_oa = np.abs(data_filtered_oa_alpha.get_data()[:, i:(i + 1) * section_size]).mean()
        alphas_oc.append(alpha_oc)
        alphas_oa.append(alpha_oa)

alphas_oc, alphas_oa = np.array(alphas_oc).flatten(), np.array(alphas_oa).flatten()

s = 10
fig = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(range(len(alphas_oc)), alphas_oc, label='OC', color='blue', s=s)
plt.scatter(range(len(alphas_oa)), alphas_oa, label='OA', color='orange', s=s)
plt.hlines(3.0 * 1e-6, 0, len(alphas_oc), linestyles='dashed', color='red')
plt.title('OA and OC sum of alpha values compared')
plt.xlabel('Subject')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(range(len(alphas_oc)), alphas_oc / alphas_oa, label='Ratio', color='red', s=s)
plt.hlines(1, 0, len(alphas_oc), linestyles='dashed', color='red')
plt.xlabel('Subject')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()

# In[8]:


indexes_for_exercise = np.argwhere(alphas_oc > 3 * 1e-6).astype(int).flatten()


# In[12]:


def save_subject_data(data_array_oc, data_array_oa, subject_ids, indexes, output_folder_name, section_size):
    for idx in tqdm(indexes, desc="Saving Subject Data"):
        path_subject_data = join(f"{output_folder_name}-{section_size}", subject_ids[idx])
        os.makedirs(path_subject_data, exist_ok=True)
        arr_oc = data_array_oc[idx].get_data()
        arr_oa = data_array_oa[idx].get_data()

        num_sections = arr_oc.shape[1] // section_size
        for i in range(num_sections):
            df_oc = pd.DataFrame(arr_oc[:, i * section_size:(i + 1) * section_size].astype(np.float32))
            df_oa = pd.DataFrame(arr_oa[:, i * section_size:(i + 1) * section_size].astype(np.float32))

            df_oc.to_csv(join(path_subject_data, f'oc_{i}.csv'))
            df_oa.to_csv(join(path_subject_data, f'oa_{i}.csv'))


save_subject_data(
    data_array_oc,
    data_array_oa,
    subject_ids,
    indexes=indexes_for_exercise,
    output_folder_name="data_for_exercise",
    section_size=30 * samplerate
)
