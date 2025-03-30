#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Existing class (incompatible interface)
class FahrenheitThermometer:
    def get_temperature(self):
        return 98.6  # Temperature in Fahrenheit

# Target interface (expected by the client)
class CelsiusThermometer:
    def get_temperature(self):
        raise NotImplementedError

# Adapter class to convert Fahrenheit to Celsius
class TemperatureAdapter(CelsiusThermometer):
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        fahrenheit = self.fahrenheit_thermometer.get_temperature()
        return (fahrenheit - 32) * 5.0 / 9.0  # Convert to Celsius

# Client code
fahrenheit_thermometer = FahrenheitThermometer()
adapter = TemperatureAdapter(fahrenheit_thermometer)

print(f"Temperature in Celsius: {adapter.get_temperature():.2f}°C")


# The key advantage of using the Adapter Pattern over directly modifying
# or creating a new CelsiusThermometer class lies in flexibility,
# reusability, and maintainability, especially in larger,
# real-world applications.
#
# ✅ Benefits of the Adapter Pattern in the Example:
# Separation of Concerns (Clean Architecture):
#
# The FahrenheitThermometer is a legacy class, possibly
# part of an external library or critical system you
# don’t want to (or can’t) modify.
# The Adapter allows you to keep the original code untouched while seamlessly
# integrating it with the new system.
# Reusability:
#
# You can reuse the TemperatureAdapter for any other FahrenheitThermometer
# objects without rewriting conversion logic each time.
# This is especially useful when multiple components rely on
# different temperature formats.
# Single Responsibility Principle (SRP):
#
# The FahrenheitThermometer focuses on providing data in Fahrenheit.
# The Adapter handles the conversion logic.
# Each class has a clear, isolated responsibility.
# Plug-and-Play Flexibility:
#
# If you decide to switch to another temperature source in the future
# (say, KelvinThermometer), you can simply write another adapter without
# affecting the existing client code.
# Interfacing with Third-Party or Legacy Code:
#
# In real-world scenarios, you often deal with third-party libraries where
# modifying source code isn't an option.
# The Adapter pattern lets you integrate such code without needing access
# to its internal implementation.
# ❌ What If You Skip the Adapter?
# If you simply modified or created a CelsiusThermometer that directly
# outputs Celsius:
#
# You’d have to rewrite the conversion logic every time you encounter
# a new Fahrenheit source.
# If the legacy FahrenheitThermometer changes, you'd need to update every
# client that directly interacts with it.
# Tightly coupled code reduces flexibility and increases maintenance costs.
# 🔑 Summary:
# Adapter Pattern = Flexible Bridge between incompatible interfaces.
# It’s especially valuable when working with legacy systems, third-party
# libraries, or different data formats.
# The adapter keeps code modular, testable, and easy to maintain.