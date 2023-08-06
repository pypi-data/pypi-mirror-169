import torch

def init_weights(m):
    """Initializing the model weights according to the parameter (layer) names.
    Parameters
        ----------
        m : models.Model
            The model whose weights are to be initialized
    """
    classname = m.__class__.__name__
    #Initializing Linear layer weights and biases from Gaussian Distribution with zero mean and std of 0.001
    if classname == "Linear":
        torch.nn.init.normal_(m.weight,mean=0,std=0.001)
        torch.nn.init.normal_(m.bias,mean=0,std=0.001)
    elif classname == "RNN":
    #Initializing non-recurrent (input-to-hidden) weights and biases from
    #Gaussian Distribution with zero mean and std of 0.001
        torch.nn.init.normal_(m.weight_ih_l0,mean=0,std=0.001)
        torch.nn.init.normal_(m.bias_ih_l0,mean=0,std=0.001)
    #Initializing recurrent (hidden-to-hidden) weights from
    #identity matrix and biases as full of zeros
        torch.nn.init.eye_(m.weight_hh_l0)
        torch.nn.init.zeros_(m.bias_hh_l0)
    #Initializing LSTM forget gate biases as full of ones
    elif classname == "LSTM":
        m.bias_ih_l0.data[25:50].fill_(1)
        m.bias_hh_l0.data[25:50].fill_(1)

def optimizer_to(optim, device):
    """Passing optimizer to a device (CPU/CUDA etc.)
    Parameters
        ----------
        optim : any optimizer from torch.optim
            The optimizer to be moved to a device
        device : torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            The target device
    """
    for param in optim.state.values():
        if isinstance(param, torch.Tensor):
            param.data = param.data.to(device)
            if param._grad is not None:
                param._grad.data = param._grad.data.to(device)
        elif isinstance(param, dict):
            for subparam in param.values():
                if isinstance(subparam, torch.Tensor):
                    subparam.data = subparam.data.to(device)
                    if subparam._grad is not None:
                        subparam._grad.data = subparam._grad.data.to(device)

class Model(torch.nn.Module):
    """The model class which consists of an/a IRNN/GRU/LSTM and a Linear layer.
    Initialization Arguments
        ----------
        input_size : int
            The number of features in the input
        hidden_size : int
            The number of features in the hidden layer
        output_size : int
            Length of the output tensor
        model_type : str
            Which model to train/evaluate: IRNN, LSTM or GRU
    Returns
        -------
        sum_out : torch tensor
            output of the model with the size of [batch_size,output_size]
    """
    def __init__(self, input_size, hidden_size, output_size, model_type):
        super(Model, self).__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.model_type = model_type
        if self.model_type == "IRNN":
            self.rnn = torch.nn.RNN(self.input_size, self.hidden_size, nonlinearity='relu',batch_first=True)
        elif self.model_type == "LSTM":
            self.lstm = torch.nn.LSTM(self.input_size, self.hidden_size, batch_first=True)
        else:
            self.gru = torch.nn.GRU(self.input_size, self.hidden_size, batch_first=True)
        self.sum_linear = torch.nn.Linear(self.hidden_size, self.output_size)
    def forward(self, input):
        if self.model_type == "LSTM":
            lstm_out, (h_,c_) = self.lstm(input)
        elif self.model_type == "IRNN":
            rnn_out, h_ = self.rnn(input)
        else:
            gru_out, h_ = self.gru(input)
        sum_out = self.sum_linear(h_)
        return sum_out


"""
class Model_IRNN(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Model_IRNN, self).__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.rnn = torch.nn.RNN(2, 100, nonlinearity='relu',batch_first=True)
        self.sum_linear = torch.nn.Linear(self.hidden_size, self.output_size)
    def forward(self, input):
        rnn_out, h_ = self.rnn(input)
        sum_out = self.sum_linear(h_)
        return sum_out

class Model_GRU(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Model_GRU, self).__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.gru = torch.nn.GRU(2, 100, batch_first=True)
        self.sum_linear = torch.nn.Linear(self.hidden_size, self.output_size)
    def forward(self, input):
        rnn_out, h_ = self.gru(input)
        sum_out = self.sum_linear(h_)
        return sum_out

class Model_LSTM(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Model_LSTM, self).__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.sum_linear = torch.nn.Linear(self.hidden_size, self.output_size)
        self.lstm = torch.nn.LSTM(2, 100, batch_first=True)
    def forward(self, input):
        lstm_out, (h_,c_) = self.lstm(input)
        sum_out = self.sum_linear(h_)
        return sum_out
"""


