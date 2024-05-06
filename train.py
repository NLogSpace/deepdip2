import numpy as np
from scipy.optimize import minimize

# which floor did wirtual reach?
# data until 2:01:05
wirtual1 = np.array([0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 2, 1, 1, 2, 2, 1]) # until 1:01:20
wirtual2 = np.array([2, 1, 1, 1, 1, 1, 2, 0, 2, 2, 2, 2, 0, 2]) # until 2:01:05
wirtual3 = np.array([0, 0, 2, 2, 1, 1, 1, 0, 2, 0, 0, 2, 1, 2, 2, 0, 0, 0, 2, 1, 2]) # until 3:00:14
wirtual4 = np.array([2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2]) # until 4:00:04
wirtual = np.concatenate((wirtual1, wirtual2, wirtual3, wirtual4), axis=0)
floor = 3
wirtual_floor_success = np.sign(wirtual[wirtual >= floor] - floor)
print(wirtual_floor_success)

sequence = wirtual_floor_success


# Probability model function
def prob_model(n, a, b, c):
    return np.minimum(a + n * b, c)

# Loss function to be minimized (Binary Cross Entropy)
def loss(params, sequence):
    a, b, c = params
    n = np.arange(len(sequence))
    predicted_probs = prob_model(n, a, b, c)
    # Binary cross-entropy loss
    loss = -(sequence * np.log(predicted_probs + 1e-9) + (1 - sequence) * np.log(1 - predicted_probs + 1e-9))
    return np.sum(loss)

# Initial guesses for parameters a, b, and c
initial_params = [0.1, 0.1, 0.9]

# Bounds for a, b, and c
bounds = [(0, 1), (0, 1), (0, 1)]

# Run the optimizer
result = minimize(loss, initial_params, args=(sequence,), bounds=bounds, method='L-BFGS-B')

# Print the optimized parameters
if result.success:
    fitted_params = result.x
    print("Optimized parameters (a, b, c):", fitted_params)
else:
    print("Optimization failed:", result.message)
