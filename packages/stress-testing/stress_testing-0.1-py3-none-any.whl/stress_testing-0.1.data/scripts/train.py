#!python
import dataset
import models
import evaluation
import numpy as np
import torch
from torch.utils.data import TensorDataset, DataLoader
import os
import argparse

parser = argparse.ArgumentParser(description='Train a sequential model which can compute sum of two numbers.')
parser.add_argument('-model', default='GRU', type=str, help='select the sequential model to train')
parser.add_argument('-timesteps', default=150, type=int, help='number of timesteps of input')
parser.add_argument('-epochs', default=50, type=int, help='number of epochs to train the model')
parser.add_argument('-lr', default=0.01, type=float, help='learning rate')
parser.add_argument('-g_clip', default=10, type=int, help='gradient clipping value')
parser.add_argument('-train_data_path', default='None', type=str, help='training data path')
parser.add_argument('-train_label_path', default='None', type=str, help='training label path')
parser.add_argument('-test_data_path', default='None', type=str, help='testing data path')
parser.add_argument('-test_label_path', default='None', type=str, help='testing label path')
parser.add_argument('-model_save_directory',default='None', type=str, help='path to save trained models')

args = parser.parse_args()

if __name__ == '__main__':
    model_type, t, epochs, lr, g_clip, train_data_path, train_label_path, test_data_path, test_label_path, model_save_directory= args.model, args.timesteps, args.epochs, args.lr, args.g_clip, args.train_data_path, args.train_label_path, args.test_data_path, args.test_label_path, args.model_save_directory
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # I have already provided my (1) training and (2) testing datasets.
    # If you would like to create your custom datasets, you can un-comment and use the lines below.
    #train_data, train_labels = dataset.create_dataset(100000,t)
    #test_data, test_labels = dataset.create_dataset(10000,t)
    #dataset.save_dataset(train_data, train_data_path, train_labels, train_label_path)
    #dataset.save_dataset(test_data, test_data_path, test_labels, test_label_path)

    #Loading the training and testing data into numpy arrays
    with open(train_data_path, 'rb') as file:
        train_data = np.load(file)
    with open(train_label_path, 'rb') as file1:
        train_labels = np.load(file1)
    with open(test_data_path, 'rb') as file3:
        test_data = np.load(file3)
    with open(test_label_path, 'rb') as file4:
        test_labels = np.load(file4)

    #Converting data numpy arrays into Pytorch tensors
    X_train = torch.from_numpy(train_data).double()
    y_train = torch.from_numpy(train_labels).double()
    X_test = torch.from_numpy(test_data).double()
    y_test = torch.from_numpy(test_labels).double()

    #Converting data tensors into Pytorch Dataset & Dataloader
    train_dataset = TensorDataset(X_train, y_train)
    train_dataloader = DataLoader(train_dataset, batch_size=64)
    test_dataset = TensorDataset(X_test, y_test)
    test_dataloader = DataLoader(test_dataset, batch_size=64)

    #Initializing the model and optimizer
    model = models.Model(2, 100, 1,model_type=model_type)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    #Initializing the model weights if model type is not GRU
    if model_type != 'GRU':
        model.apply(models.init_weights)

    #If you want to load model weights from a saved model file and continue traning,
    #comment out the line below
    #model = evaluation.load_checkpoint(model,filepath)

    #Initializing the MSE loss and passing the model, the loss function and the optimizer
    #to device
    model = model.double()
    mse_loss = torch.nn.MSELoss()
    model.to(device)
    models.optimizer_to(optimizer, device)
    mse_loss.to(device)

    #Initializing training and testing loss arrays
    epoch_rmse_losses = []
    epoch_mse_losses = []
    test_epoch_rmse_losses = []
    test_epoch_mse_losses = []

    #Model training & testing through epochs
    for epoch in range(epochs):
        #Setting model mode as train
        model.train()
        batch_rmse_loss = []
        batch_mse_loss = []
        for data, label in train_dataloader:
            data = data.to(device)
            label = label.to(device)
            y_pred = model(data.double())
            #The objective function is RMSE
            loss = torch.sqrt(mse_loss(np.squeeze(y_pred), label))
            loss.backward() #Computing gradients
            #Gradient clipping with the parameter "g_clip"
            torch.nn.utils.clip_grad_norm_(model.parameters(), g_clip)
            optimizer.step() #Updating the parameters
            optimizer.zero_grad()
            batch_rmse_loss.append(loss.item())
            batch_mse_loss.append(mse_loss(np.squeeze(y_pred), label).item())
        epoch_rmse_loss = sum(batch_rmse_loss) / len(batch_rmse_loss)
        epoch_mse_loss = sum(batch_mse_loss) / len(batch_mse_loss)
        epoch_rmse_losses.append(epoch_rmse_loss)
        epoch_mse_losses.append(epoch_mse_loss)
        print(f'[EPOCH]: {epoch}')
        print(f'[TRAIN RMSE LOSS]: {epoch_rmse_loss:.6f}')
        print(f'[TRAIN MSE LOSS]: {epoch_mse_loss:.6f}')

        #Testing the model
        test_rmse_loss, test_mse_loss = evaluation.test_model(model, test_dataloader)
        test_epoch_rmse_losses.append(test_rmse_loss)
        test_epoch_mse_losses.append(test_mse_loss)

        if model_save_directory != 'None':
            #Saving the state dict of the model and the optimizer under the saved_models directory
            PATH = os.path.join(model_save_directory+'/'+model_type.lower()+'_'+str(t)+'_'+str(epoch)+'.pt')
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'RMSE_loss': epoch_rmse_loss,
                'MSE_loss': epoch_mse_loss,
                'TEST_RMSE_loss': test_rmse_loss,
                'TEST_MSE_loss': test_mse_loss,
            }, PATH)
