import numpy as np

def main():    
    # Activity 1: Water Pipe Leak Simulation

    C = np.zeros(21)
    C[0] = 80
    D = 0.2
    dx = 1.0
    dt = 0.4        
    r = D * dt / dx**2

    print(f"r = {r}")  

    for step in range(21):
        t = round(step * dt, 1)
        if step % 5 == 0:      
            print(f"t={t}s: {C.round(1)}")
        C[1:-1] += r * (C[2:] - 2*C[1:-1] + C[:-2])
        C[0] = 80 
        

if __name__ == "__main__":
    main()
