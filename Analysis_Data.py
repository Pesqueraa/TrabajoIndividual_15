import math
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, theta, g):
        self.v0 = v0
        self.theta = theta
        self.g = g

    def trajectory(self):
        v0x = self.v0 * math.cos(math.radians(self.theta))
        v0y = self.v0 * math.sin(math.radians(self.theta))

        t = []
        x = []
        y = []

        while v0y >= 0:
            t.append(len(t))
            x.append(v0x * len(t))
            y.append(v0y * len(t) - 0.5 * self.g * len(t) ** 2)

            v0y = v0y - self.g

        return x, y

    def max_height(self):
        t = self.v0 * math.sin(math.radians(self.theta)) / self.g
        y = self.v0 * math.sin(math.radians(self.theta)) * t - 0.5 * self.g * t ** 2
        return y

    def time_of_flight(self):
        t = self.v0 * math.sin(math.radians(self.theta)) / self.g
        return t

    def horizontal_range(self):
        t = self.v0 * math.sin(math.radians(self.theta)) / self.g
        x = self.v0 * math.cos(math.radians(self.theta)) * t
        return x

def main():
    while True:
        try:
            v0 = float(input("Enter the initial velocity (m/s): "))
            theta = float(input("Enter the launch angle (degrees): "))
            g = float(input("Enter the gravitational acceleration (m/s^2): "))
            if v0 < 0 or theta < 0 or g < 0:
                raise ValueError("All inputs must be non-negative.")
            else:
                projectile = Projectile(v0, theta, g)
                x, y = projectile.trajectory()
                plt.plot(x, y)
                plt.xlabel("x (m)")
                plt.ylabel("y (m)")
                plt.title("Projectile Trajectory")
                plt.show()
                print("Maximum Height: ", projectile.max_height(), "m")
                print("Time of Flight: ", projectile.time_of_flight(), "s")
                print("Horizontal Range: ", projectile.horizontal_range(), "m")
                break
        except ValueError as ve:
            print("Invalid input:", ve)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
