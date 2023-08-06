import torch
import numpy as np

def test_model(model,test_dataloader):
    """Testing the model with test_dataloader. No training in this function, just evaluation.
    Parameters
        ----------
        model : models.Model
            the trained model to evaluate
        test_dataloader: torch.utils.data.DataLoader
            test dataloader to use in evaluation
    Returns
        -------
        rmse_loss : float
            the average RMSE loss calculated during the evaluation
        mse_loss : float
            the average MSE loss calculated during the evaluation
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # Setting model mode as evaluation
    model.eval()
    test_mse_loss = torch.nn.MSELoss()
    test_batch_rmse_loss=[]
    test_batch_mse_loss=[]
    for data,label in test_dataloader:
        with torch.set_grad_enabled(False):
            data = data.to(device)
            label = label.to(device)
            y_pred = model(data.double())
            loss = torch.sqrt(test_mse_loss(np.squeeze(y_pred), label))
            test_batch_rmse_loss.append(loss.item())
            test_batch_mse_loss.append(test_mse_loss(np.squeeze(y_pred), label).item())
    rmse_loss = sum(test_batch_rmse_loss) / len(test_batch_rmse_loss)
    tmse_loss = sum(test_batch_mse_loss) / len(test_batch_mse_loss)
    print(f"[TEST RMSE LOSS]: {rmse_loss:.6f}",flush=True)
    print(f"[TEST MSE LOSS]: {tmse_loss:.6f}",flush=True)
    print()
    return rmse_loss, tmse_loss

def load_checkpoint(model,filepath):
    """Loading the model weights from a pre-saved model file.
    Parameters
        ----------
        model : models.Model
            the initialized Model class to load the weights to
        filepath: str
            path of the saved model file
    Returns
        -------
        model : models.Model
            weight-loaded model
    """
    checkpoint = torch.load(filepath, map_location=torch.device('cpu'))
    model.load_state_dict(checkpoint['model_state_dict'])
    return model