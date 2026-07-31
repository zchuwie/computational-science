import numpy as np


def main():    
    # Activity 1: Water Pipe Leak Simulation

    # C = np.zeros(21)
    # C[0] = 80
    # D = 0.2
    # dx = 1.0
    # dt = 0.4        
    # r = D * dt / dx**2

    # print(f"r = {r}")  

    # for step in range(21):
    #     t = round(step * dt, 1)
    #     if step % 5 == 0:      
    #         print(f"t={t}s: {C.round(1)}")
    #     C[1:-1] += r * (C[2:] - 2*C[1:-1] + C[:-2])
    #     C[0] = 80 

    # Activity 2: Deep Dish Pizza Baking Simulator

    space_grid = np.linspace(0, 10, 6)
    time_steps = np.arange(0, 11, 2)
    
    temp_matrix = np.zeros((len(time_steps), len(space_grid)))
    temp_matrix[0] = [180.0, 20.0, 20.0, 20.0, 20.0, 20.0]
    
    for t in range(1, len(time_steps)):
        temp_matrix[t] = temp_matrix[t - 1]
        for i in range(1, len(space_grid) - 1):
            conduction = 0.20 * (temp_matrix[t-1, i-1] - 2 * temp_matrix[t-1, i] + temp_matrix[t-1, i+1])
            temp_matrix[t, i] = temp_matrix[t-1, i] + conduction
        temp_matrix[t, 0] = 180.0
    
    print(f"\nTemperature Matrix:\n{temp_matrix}\n")
    
    print(f"Min Temperature : {np.min(temp_matrix)} °C")
    print(f"Max Temperature : {np.max(temp_matrix)} °C")
    print(f"Average Temp at Minute 10 : {np.mean(temp_matrix[-1])} °C")
    
    burn_zones = np.where(temp_matrix[:, 1:] > 75.0)
    print(f"\nBurning Threshold Breached (>75°C) at coordinates:")
    for r, c in zip(burn_zones[0], burn_zones[1]):
        print(f"  Minute {time_steps[r]} | {space_grid[c+1]:.0f}-inch | {temp_matrix[r, c+1]:.3f} °C")
    
    core_temp = temp_matrix[-1, len(space_grid) // 2]
    print(f"\nCore Temp at Minute 10: {core_temp:.3f} °C — {'SAFE' if core_temp >= 50 else 'UNDERCOOKED'}")
    
    clamped = np.clip(temp_matrix, 20.0, 180.0)
    print(f"\nClamped Matrix:\n{clamped}")
    
    gradient = np.gradient(temp_matrix[-1])
    print(f"\nHeat Gradient at Minute 10:\n{gradient}")
                

if __name__ == "__main__":
    main()
