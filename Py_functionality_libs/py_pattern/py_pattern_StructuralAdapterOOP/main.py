from temperature_factory import TemperatureAdapterFactory
from thermometer import FahrenheitThermometer


def main():
    fahrenheit_thermometer = FahrenheitThermometer()

    print("Temperature Converter (Fahrenheit → Celsius/Kelvin/Rankine/Reaumur)")
    unit = input("Enter the desired unit (Celsius/Kelvin/Rankine/Reaumur): ")

    try:
        adapter = TemperatureAdapterFactory.get_adapter(unit, fahrenheit_thermometer)
        print(f"Temperature in {unit.capitalize()}: {adapter.get_temperature()}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
