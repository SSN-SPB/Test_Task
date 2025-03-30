# Legacy system: Old Charging Station
class USB_A_ChargingStation:
    def provide_power(self):
        return "Power from USB-A"

# Target interface: Modern Electric Car
class ElectricCar:
    def charge(self):
        raise NotImplementedError

# Adapter: Converts USB-A to Type-C
class USB_A_to_Type_C_Adapter(ElectricCar):
    def __init__(self, charging_station):
        self.charging_station = charging_station

    def charge(self):
        power = self.charging_station.provide_power()
        return f"Converting to Type-C -> {power} used to charge the car."

# Client code
old_station = USB_A_ChargingStation()
adapter = USB_A_to_Type_C_Adapter(old_station)

print(adapter.charge())