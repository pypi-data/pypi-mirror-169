import random
import numpy as np

# To create training dataset I have used 42,
# to create test dataset 1 I have used 42
# and to create test dataset 2 I have used 77.
# Defining the random seed as a global variable is healthier than passing it as a parameter;
# so please change it through the line down below when it's needed:
random.seed(42)

def create_dataset(n_of_data,t):
    """Creating a dataset which will have shape of [n_of_data,t,2]
    Parameters
        ----------
        n_of_data : int
            number of data points in created dataset
        t : int
            sequence length of the data points in created dataset
    Returns
        -------
        np.array(data) : numpy array
            the numpy array version of the data points
        np.array(labels) : numpy array
            the numpy array version of the data points' labels
    """
    data = []
    labels = []
    for i in range(n_of_data):
        #Sampling sequence (t) of numbers from a uniform distribution
        s = np.random.uniform(0, 1, t).round(1)
        #Initializing a mask array (full of zeros)
        mask = np.zeros(t, dtype=int)
        #Random sampling two indices which will be the 1's in the mask array
        indice = random.sample(range(t), 2)
        mask[indice] = 1
        #Merging the data array (sequence of numbers) and the mask element-wise
        fin = np.dstack((s, mask)).squeeze()
        #Calculating the sum of the two elements (in our case this is the label)
        #which has 1 as the mask value
        label = s[indice].sum().round(1)
        data.append(fin)
        labels.append(label)
    return np.array(data), np.array(labels)

def save_dataset(data,filename,data2,filename2,data3,filename3):
    """Saves dataset as .npy files (saves data, labels and indices separately)
    Parameters
        ----------
        data : numpy array
            data array
        filename : str
            .npy ending path to save the data array
        data2 : numpy array
            data (label) array
        filename2 : str
            .npy ending path to save the data (label) array
        data3 : numpy array
            data (indices) array
        filename3 : str
            .npy ending path to save the data (indices) array

    """
    with open(filename, 'wb') as file:
        np.save(file, data)
    with open(filename2, 'wb') as file2:
        np.save(file2, data2)
    with open(filename3, 'wb') as file3:
        np.save(file3, data3)