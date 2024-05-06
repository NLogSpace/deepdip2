from dataclasses import dataclass
import random

def lin_prob(alpha, beta, maximum, attempt):
    return min(alpha + beta*attempt, maximum)

@dataclass
class Floor:
    alpha: float
    beta: float
    maximum: float
    attempts: int

    def prob(self):
        return min(self.alpha + self.beta*self.attempts, self.maximum)


floors = []
for i in range(17):
    floors.append(Floor(0.45, 0.05, 0.9, 0))

current_floor = 0
finished = False
for i in range(8000):
    if finished:
        break
    current_floor = 0
    while True:
        prob = floors[current_floor].prob()
        floors[current_floor].attempts += 1
        if random.random() < prob:
            current_floor += 1
            if current_floor == 17:
                print(f"Attempt {i}: FINISHED THE TOWER")
                finished = True
                break
        else:
            print(f"Attempt {i}: Failed at floor {current_floor}.")
            break
