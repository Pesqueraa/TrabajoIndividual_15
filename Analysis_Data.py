# Creo un programa que me grafique un tiro parabólico, aportando los siguientes datos iniciales: velocidad inical, ángulo de tiro y aceleracion de la gravedad.
# Importo el modulo para poder usar las funciones matematicas.
import math
# Importo el modulo para que me pinte la parabola en un grafico.
import matplotlib.pyplot as plt
# Defino la clase que controla los parametros del proyectil.
class Projectile:
# Defino la velocidad inicial, el angulo de tiro y ac.gravedad.
    def __init__(self, v0, theta, g):
        self.v0 = v0
        self.theta = math.radians(theta)  # Convert angle to radians
        self.g = g
# Defino los componentes de la velocidad en ambos ejes.
    def calculate_components(self):
        self.v0x = self.v0 * math.cos(self.theta)
        self.v0y = self.v0 * math.sin(self.theta)
# Defino las ecuaciones de trayectoria dependientes del tiempo y uso return para que me devuelva los datos calculados.
    def calculate_trajectory(self, time):
        x = self.v0x * time
        y = self.v0y * time - 0.5 * self.g * time**2
        return x, y
# Defino la ecuacion de la altura maxima y uso return para que me devuelva los datos calculados.
    def calculate_max_height(self):
        t = self.v0y / self.g
        return self.calculate_trajectory(t)[1]
# Defino la ecuacion del tiempo de vuelo y uso return para que me devuelva los datos calculados.
    def calculate_time_of_flight(self):
        return 2 * self.v0y / self.g
# Defino la ecuacion del alcance máximo y uso return para que me devuelva los datos calculados. 
    def calculate_horizontal_range(self):
        t = self.calculate_time_of_flight()
        return self.v0x * t
# Creo una lista de valores con el tiempo de vuelo
    def plot_trajectory(self):
        t_values = [i for i in range(int(self.calculate_time_of_flight()) + 1)]
        trajectory = [self.calculate_trajectory(t) for t in t_values]
        x, y = zip(*trajectory)
        plt.plot(x, y)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.title("Projectile Trajectory")
        plt.show()

def main():
    while True:
        try:
            v0 = float(input("Enter the initial velocity (m/s): "))
            theta = float(input("Enter the launch angle (degrees): "))
            g = float(input("Enter the gravitational acceleration (m/s^2): "))
            # Si alguno de los parametros es degativo damos un mensaje de error.
            if v0 < 0 or theta < 0 or g < 0:
                raise ValueError("All inputs must be non-negative.")
            else:
                projectile = Projectile(v0, theta, g)
                # Calcula las coponentes de la velocidad en los ejes. 
                projectile.calculate_components()
                # Me pinta la trayectoria
                projectile.plot_trajectory()
                # Me imprime el valor de la altura maxima, del tiempo de vuelo y del alcance maximo.
                print("Maximum Height:", projectile.calculate_max_height(), "m")
                print("Time of Flight:", projectile.calculate_time_of_flight(), "s")
                print("Horizontal Range:", projectile.calculate_horizontal_range(), "m")
                # Pongo un break para parar el bucle.
                break
        except ValueError as ve:
            print("Invalid input:", ve)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
