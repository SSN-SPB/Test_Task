from temperature_adapters \
    import \
    FahrenheitToCelsiusAdapter,\
    FahrenheitToKelvinAdapter, \
    FahrenheitToRankineAdapter, \
    FahrenheitToReaumurAdapter

class TemperatureAdapterFactory:
    @staticmethod
    def get_adapter(unit, fahrenheit_thermometer):
        unit = unit.lower()
        if unit == "celsius":
            return FahrenheitToCelsiusAdapter(fahrenheit_thermometer)
        elif unit == "kelvin":
            return FahrenheitToKelvinAdapter(fahrenheit_thermometer)
        elif unit == "rankine":
            return FahrenheitToRankineAdapter(fahrenheit_thermometer)
        elif unit == "reaumur":
            return FahrenheitToReaumurAdapter(fahrenheit_thermometer)
        else:
            raise ValueError(f"Unsupported temperature unit: {unit}")