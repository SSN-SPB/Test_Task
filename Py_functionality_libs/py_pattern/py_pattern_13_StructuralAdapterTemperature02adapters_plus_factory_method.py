# Legacy system: Fahrenheit thermometer (unchanged)
class FahrenheitThermometer:
    def get_temperature(self):
        return 98.6  # Temperature in Fahrenheit


# Target interface: All adapters implement this
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


# 🚀 Factory: Creates the correct adapter based on the desired unit
class TemperatureAdapterFactory:
    @staticmethod
    def get_adapter(unit, fahrenheit_thermometer):
        if unit.lower() == "celsius":
            return FahrenheitToCelsiusAdapter(fahrenheit_thermometer)
        elif unit.lower() == "kelvin":
            return FahrenheitToKelvinAdapter(fahrenheit_thermometer)
        else:
            raise ValueError(f"Unsupported temperature unit: {unit}")


# Client code
fahrenheit_thermometer = FahrenheitThermometer()

# Dynamic adapter creation using the factory
unit = input("Enter the desired unit (Celsius/Kelvin): ")

try:
    adapter = TemperatureAdapterFactory.get_adapter(unit, fahrenheit_thermometer)
    print(f"Temperature in {unit}: {adapter.get_temperature()}")
except ValueError as e:
    print(e)


# ✅ Sample Run 1 (User inputs "Celsius"):
# mathematica
# Copy
# Edit
# Enter the desired unit (Celsius/Kelvin): Celsius
# Temperature in Celsius: 37.00°C
# ✅ Sample Run 2 (User inputs "Kelvin"):
# mathematica
# Copy
# Edit
# Enter the desired unit (Celsius/Kelvin): Kelvin
# Temperature in Kelvin: 310.15K
# ❌ Sample Run 3 (Invalid Input):
# java
# Copy
# Edit
# Enter the desired unit (Celsius/Kelvin): Rankine
# Unsupported temperature unit: Rankine
# 🚀 How This Design Works:
# FahrenheitThermometer: Legacy code remains unchanged.
# TemperatureAdapter: Interface for all adapters.
# Adapters (FahrenheitToCelsiusAdapter, FahrenheitToKelvinAdapter): Handle specific conversions.
# TemperatureAdapterFactory: Dynamically returns the appropriate adapter based on the user's choice.
# Client Code: Only interacts with the factory—no need to worry about adapter details.
# ⚡ Advantages of Using the Factory Pattern Here:
# Dynamic Adapter Creation: No hard-coded adapter classes in client code.
# Open for Extension: Adding new units (like Rankine) requires just creating a new adapter and updating the factory—no changes to client code.
# Improved Error Handling: Centralizes logic to handle unsupported units gracefully.
