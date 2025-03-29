from rocketpy import Environment, SolidMotor, Rocket, Flight
import datetime
import rocketpy

# Definir el entorno
env = Environment(latitude=31.865858, longitude=-116.607681, elevation=1400)
tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))
env.set_atmospheric_model("Forecast", file="GFS")


# Definir el motor sólido
motor = rocketpy.SolidMotor(
    thrust_source=[(0, 0), (0.1, 50), (0.5, 200), (1, 300), (1.5, 200), (2, 100), (2.5, 50), (3, 0)],
    burn_time=3,
    grain_number=5,
    grain_separation=5e-3,
    grain_initial_inner_radius=0.02,  
    grain_outer_radius=0.04,  
    grain_initial_height=0.1,
    nozzle_radius=0.02,
    throat_radius=0.01,
    interpolation_method='linear',
    dry_mass=0.3,  
    dry_inertia=(0.0005, 0.0005, 0.001),
    grain_density=1800,
    grains_center_of_mass_position=0.15,
    center_of_dry_mass_position=0.1
)
# Definir el CanSat como un pequeño cohete
cansat = Rocket(
    radius=127/2000,
    mass=14.426,
    inertia=(6.321, 6.321, 0.034),
    power_off_drag=0.5,
    power_on_drag=0.6,
    center_of_mass_without_motor = (0.0, 0.0, 0.0), 
    coordinate_system_orientation = "tail_to_nose"
)

# Configurar el paracaídas
cansat.add_parachute(
    name='Main',
    CdS=1.2,
    trigger=lambda f, h, v: h < 300,  # Se despliega a 300 m
    sampling_rate=100,
    lag=1.0
)

# Simulación del vuelo
flight = Flight(rocket=cansat, environment=env, inclination=90, heading=0)

# Mostrar resultados clave
print("Altura máxima:", flight.apogee)
print("Tiempo de vuelo:", flight.out_of_launch_rail_time)
print("Velocidad máxima:", flight.max_speed)
print("Aterrizaje en:", flight.impact_point)
