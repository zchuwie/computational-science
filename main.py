import numpy as np
from scipy.integrate import odeint
from scipy.spatial.distance import euclidean, cityblock
from scipy.interpolate import interp1d


def activity_1():
    """
    Activity 1: Water Pipe Leak Simulation
    Simulates diffusion/conduction across a 1D pipe grid over time.
    """
    C = np.zeros(21)
    C[0] = 80
    D = 0.2
    dx = 1.0
    dt = 0.4
    r = D * dt / dx**2

    print("\n" + "=" * 60)
    print("--- Activity 1: Water Pipe Leak Simulation ---")
    print(f"r = {r}")

    for step in range(21):
        t = round(step * dt, 1)
        if step % 5 == 0:
            print(f"t={t}s: {C.round(1)}")
        C[1:-1] += r * (C[2:] - 2 * C[1:-1] + C[:-2])
        C[0] = 80

    return C


def activity_2_3():
    """
    Activity 2/3: Deep Dish Pizza Baking Simulator (Finite Difference with Loops)
    Simulates 1D heat conduction through a deep dish pizza over time.
    """
    oven_temp = 74.0
    initial_temp = 20.0
    total_time = 106
    time_step = 2
    size = 10
    sampling = 6

    space_grid = np.linspace(0, size, sampling)
    time_steps = np.arange(0, total_time + 1, time_step)

    temp_matrix = np.full((len(time_steps), len(space_grid)), initial_temp)
    temp_matrix[:, 0] = oven_temp

    for t in range(1, len(time_steps)):
        temp_matrix[t] = temp_matrix[t - 1]
        for i in range(1, len(space_grid) - 1):
            conduction = 0.20 * (
                temp_matrix[t - 1, i - 1]
                - 2 * temp_matrix[t - 1, i]
                + temp_matrix[t - 1, i + 1]
            )
            temp_matrix[t, i] = temp_matrix[t - 1, i] + conduction

        conduction_core = 0.20 * 2 * (temp_matrix[t - 1, -2] - temp_matrix[t - 1, -1])
        temp_matrix[t, -1] = temp_matrix[t - 1, -1] + conduction_core
        temp_matrix[t, 0] = oven_temp

    np.set_printoptions(precision=2, suppress=True)

    print("\n" + "=" * 60)
    print("--- Activity 2/3: Deep Dish Pizza Simulator (Finite Difference) ---")
    print(f"\nTemperature Matrix:\n{temp_matrix}\n")

    print(f"Min Temperature : {np.min(temp_matrix):.2f} °C")
    print(f"Max Temperature : {np.max(temp_matrix):.2f} °C")
    print(f"Average Temp at Minute {time_steps[-1]} : {np.mean(temp_matrix[-1]):.2f} °C")

    burn_zones = np.where(temp_matrix[:, 1:] > 75.0)
    if len(burn_zones[0]) > 0:
        print("\nBurning Threshold Breached at coordinates:")
        for r, c in zip(burn_zones[0], burn_zones[1]):
            print(f"  Minute {time_steps[r]} | {space_grid[c+1]:.0f}-inch | {temp_matrix[r, c+1]:.2f} °C")
    else:
        print("\nBurning Threshold Breached: None")

    core_temp = temp_matrix[-1, len(space_grid) // 2]
    status = "SAFE" if core_temp >= 50 else "UNDERCOOKED"
    print(f"\nCore Temp at Minute {time_steps[-1]}: {core_temp:.2f} °C — {status}")

    clamped = np.clip(temp_matrix, initial_temp, oven_temp)
    print(f"\nClamped Matrix:\n{clamped}")

    gradient = np.gradient(temp_matrix[-1])
    print(f"\nHeat Gradient at Minute {time_steps[-1]}:\n{gradient}")

    return temp_matrix


def activity_4():
    """
    Activity 4: Simulates 1D heat conduction in deep dish pizza using SciPy's ODE solver (odeint)
    without using any time or spatial loops.
    """
    oven_temp = 74.0
    initial_temp = 20.0
    total_time = 108
    time_step = 2
    size = 10
    sampling = 6

    space_grid = np.linspace(0, size, sampling)
    time_steps = np.arange(0, total_time + 1, time_step)

    rate = 0.20 / time_step

    def heat_ode(T, t):
        dT = np.zeros_like(T)
        dT[0] = 0.0
        dT[1:-1] = rate * (T[:-2] - 2 * T[1:-1] + T[2:])
        dT[-1] = 2 * rate * (T[-2] - T[-1])
        return dT

    T0 = np.full(sampling, initial_temp)
    T0[0] = oven_temp

    temp_matrix = odeint(heat_ode, T0, time_steps)

    np.set_printoptions(precision=2, suppress=True)

    print("\n" + "=" * 60)
    print("--- Activity 4: SciPy Simulation (No Loops) ---")
    print(f"\nTemperature Matrix:\n{temp_matrix}\n")
    print(f"Min Temperature : {np.min(temp_matrix):.2f} °C")
    print(f"Max Temperature : {np.max(temp_matrix):.2f} °C")
    print(f"Average Temp at Minute {time_steps[-1]} : {np.mean(temp_matrix[-1]):.2f} °C")

    burn_mask = temp_matrix[:, 1:] > 75.0
    if np.any(burn_mask):
        r_idx, c_idx = np.where(burn_mask)
        print("\nBurning Threshold Breached at coordinates:")
        for r, c in zip(r_idx, c_idx):
            print(f"  Minute {time_steps[r]} | {space_grid[c+1]:.0f}-inch | {temp_matrix[r, c+1]:.2f} °C")
    else:
        print("\nBurning Threshold Breached: None")

    core_temp = temp_matrix[-1, len(space_grid) // 2]
    status = "SAFE" if core_temp >= 50 else "UNDERCOOKED"
    print(f"\nCore Temp at Minute {time_steps[-1]}: {core_temp:.2f} °C — {status}")

    clamped = np.clip(temp_matrix, initial_temp, oven_temp)
    print(f"\nClamped Matrix:\n{clamped}")

    gradient = np.gradient(temp_matrix[-1])
    print(f"\nHeat Gradient at Minute {time_steps[-1]}:\n{gradient}")

    return temp_matrix

def activity_5():
    warehouse = [0, 0]
    locations = [[2,3], [4,2], [5,5], [7,5], [8,8]]
    fuel_consumed = np.array([0.6, 0.8, 1.2, 1.5, 2.0])

    euclidean_distances = np.array([euclidean(warehouse, loc) for loc in locations])

    cityblock_distances = np.array([cityblock(warehouse, loc) for loc in locations])

    print(f"Euclidean Distances (km): {np.round(euclidean_distances, 2)}")
    print(f"Cityblock Distances (km): {cityblock_distances}")

    fuel_estimator = interp1d(cityblock_distances, fuel_consumed, kind='linear')

    new_location = [6, 4]
    new_cb_distance = cityblock(warehouse, new_location)
    estimated_fuel = fuel_estimator(new_cb_distance)

    print(f"\nNew Location {new_location}:")
    print(f"  -> Cityblock Distance: {new_cb_distance} blocks")
    print(f"  -> Estimated Fuel: {float(estimated_fuel):.2f} Liters")


def main():
    activity_5()


if __name__ == "__main__":
    main()
