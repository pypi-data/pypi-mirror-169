#!python
import models
import evaluation
import numpy as np
import torch
from torch.utils.data import TensorDataset, DataLoader
import argparse

parser = argparse.ArgumentParser(description='Evaluate a pre-trained sequential model which can compute sum of two numbers.')
parser.add_argument('-model', default='GRU', type=str, help='select the sequential model to train')
parser.add_argument('-timesteps', default=150, type=int, help='number of timesteps of input')
parser.add_argument('-filepath', default='None', type=str, help='file path of the pre-trained model weights',required=True)
parser.add_argument('-datapath', default='None', type=str, help='path of test data',required=True)
parser.add_argument('-labelpath', default='None', type=str, help='path of test labels',required=True)

args = parser.parse_args()

if __name__ == '__main__':
    model_type, t, filepath, datapath, labelpath= args.model, args.timesteps, args.filepath, args.datapath, args.labelpath

    #If no datapath or labelpath provided from the user, it uses default data and label paths
    #if datapath=='None' or labelpath=='None':
    #    datapath='data/t_{}/test_data.npy'.format(t)
    #    labelpath='data/t_{}/test_labels.npy'.format(t)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open(datapath, 'rb') as file:
        test_data = np.load(file)
    with open(labelpath, 'rb') as file2:
        test_labels = np.load(file2)

    X_test = torch.from_numpy(test_data).double()
    y_test = torch.from_numpy(test_labels).double()
    test_dataset = TensorDataset(X_test, y_test)
    test_dataloader = DataLoader(test_dataset, batch_size=64)
    model = models.Model(2, 100, 1,model_type=model_type)
    #Loading the model weights from the model file, through the "filepath" user passed as an argument
    model = evaluation.load_checkpoint(model,filepath)
    model = model.double()
    mse_loss = torch.nn.MSELoss()
    model.to(device)
    mse_loss.to(device)
    #Calling the method "test_model" from the module "evaluation"
    test_rmse_loss, test_mse_loss = evaluation.test_model(model, test_dataloader)