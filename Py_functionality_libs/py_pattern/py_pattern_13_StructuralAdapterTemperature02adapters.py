# Legacy system: Fahrenheit thermometer (cannot be modified)
class FahrenheitThermometer:
    def get_temperature(self):
        return 98.6  # Temperature in Fahrenheit


# Target interface: All adapters will implement this
class TemperatureAdapter:
    def get_temperature(self):
        raise NotImplementedError


# Adapter 1: Fahrenheit to Celsius
class FahrenheitToCelsiusAdapter(TemperatureAdapter):
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        fahrenheit = self.fahrenheit_thermometer.get_temperature()
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        return f"{celsius:.2f}°C"


# Adapter 2: Fahrenheit to Kelvin
class FahrenheitToKelvinAdapter(TemperatureAdapter):
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        fahrenheit = self.fahrenheit_thermometer.get_temperature()
        kelvin = (fahrenheit - 32) * 5.0 / 9.0 + 273.15
        return f"{kelvin:.2f}K"


# Client code
fahrenheit_thermometer = FahrenheitThermometer()

# Using both adapters
celsius_adapter = FahrenheitToCelsiusAdapter(fahrenheit_thermometer)
kelvin_adapter = FahrenheitToKelvinAdapter(fahrenheit_thermometer)

# Display temperatures in both Celsius and Kelvin
print("Temperature in Celsius:", celsius_adapter.get_temperature())
print("Temperature in Kelvin:", kelvin_adapter.get_temperature())
