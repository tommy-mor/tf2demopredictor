import torch
import torch.nn as nn
import numpy as np

dataset1 = np.load('file.txt.bin')

training_x = torch.tensor([[1],[2],[3],[4],[5]], dtype=torch.float32)
training_y = torch.tensor([[2],[4],[6],[8],[10]], dtype=torch.float32)

x_test = torch.tensor([5.0], dtype=torch.float32)

n_samples, n_features = training_x.shape
print(n_samples, n_features)


class LinearRegression(nn.Module):
    def __init__(self, input, output):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input, output)

    def forward(self, x):
        return self.linear(x)

model = LinearRegression(1, 1)

print(f'Prediction before training: f(5) = {model(x_test)}')

learning_rate = 0.03
n_iters = 100

loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

for epoch in range(n_iters):
    y_pred = model(training_x)

    l = loss(training_y, y_pred)
    l.backward()

    optimizer.step()
    optimizer.zero_grad()

    if epoch % 10 == 0:
        [w, bias] = model.parameters()
        w = w.item()
        print(f'epoch {epoch+1}: w = {w:.3f}, loss = {l:.8f}')