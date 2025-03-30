from abc import ABC, abstractmethod

# Abstract base class for adapters
class TemperatureAdapter(ABC):
    @abstractmethod
    def get_temperature(self):
        pass

# Fahrenheit to Celsius Adapter
class FahrenheitToCelsiusAdapter(TemperatureAdapter):
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        fahrenheit = self.fahrenheit_thermometer.get_temperature()
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        return f"{celsius:.2f}°C"


# Fahrenheit to Kelvin Adapter
class FahrenheitToKelvinAdapter(TemperatureAdapter):
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        fahrenheit = self.fahrenheit_thermometer.get_temperature()
        kelvin = (fahrenheit - 32) * 5.0 / 9.0 + 273.15
        return f"{kelvin:.2f}K"


# Fahrenheit to Reaumur Adapter
class FahrenheitToReaumurAdapter(TemperatureAdapter):
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        fahrenheit = self.fahrenheit_thermometer.get_temperature()
        reaumur = (fahrenheit - 32) * 4.0 / 9.0
        return f"{reaumur:.2f}Re"


# Fahrenheit to Rankine Adapter
class FahrenheitToRankineAdapter(TemperatureAdapter):
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        fahrenheit = self.fahrenheit_thermometer.get_temperature()
        rankine = fahrenheit + 459.67
        return f"{rankine:.2f}R"
