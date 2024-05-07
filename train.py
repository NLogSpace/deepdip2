import numpy as np
from scipy.optimize import minimize

# which floor did wirtual reach?
# data until 2:01:05
wirtual1 = np.array([0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 2, 1, 1, 2, 2, 1]) # until 1:01:20
wirtual2 = np.array([2, 1, 1, 1, 1, 1, 2, 0, 2, 2, 2, 2, 0, 2]) # until 2:01:05
wirtual3 = np.array([0, 0, 2, 2, 1, 1, 1, 0, 2, 0, 0, 2, 1, 2, 2, 0, 0, 0, 2, 1, 2]) # until 3:00:14
wirtual4 = np.array([2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2]) # until 4:00:04
wirtual5 = np.array([2, 2, 2, 2, 2, 0, 1, 1, 2, 0, 2, 0, 2, 2]) # until 5:03:00
wirtual6 = np.array([2, 1, 3, 2, 3, 0, 2, 2, 2]) # until 6:10:43
wirtual7 = np.array([0, 1, 3, 2, 2, 2, 2, 1, 2, 0, 3]) # until 7:02:47
wirtual8 = np.array([2, 1, 2, 4, 3, 2]) # until 8:03:00
wirtual9 = np.array([2, 1, 2, 2, 2, 2, 4]) # until 9:00:09
wirtual10= np.array([1, 2, 1, 2, 0, 2, 1, 3, 2, 4, 2, 2]) # until 10:00:00
wirtual11= np.array([1, 2, 0, 1, 4, 2, 1, 2, 4, 4]) # until 11:07:01
wirtual12= np.array([4, 2, 2, 1, 0, 2, 2, 2, 2, 4]) # until 12:25:50

wirtual = np.concatenate((wirtual1, wirtual2, wirtual3, wirtual4, wirtual5, wirtual6, wirtual7, wirtual8, wirtual9, wirtual10), axis=0)
floor = 4
wirtual_floor_success = np.sign(wirtual[wirtual >= floor] - floor)
print(f"Success on floor {floor}:")
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
