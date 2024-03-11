import math
pi = math.pi
time = None
length = float(input("Length of pendulum (meters): "))
time = (2*pi)*(math.sqrt(length/9.81))
print(f"Time (Seconds): {time:.2f}")