from math import pi

def tire_volume(width,aspect_ratio,diameter):
    volume = float((pi*(width**2)*aspect_ratio*(width*aspect_ratio+2540*diameter))/10000000000)
    return volume

def main():
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = tire_volume(width,aspect_ratio,diameter)
    print(f"The approximate volume is {volume:.2f} liters")

if __name__ == "__main__":
    main()