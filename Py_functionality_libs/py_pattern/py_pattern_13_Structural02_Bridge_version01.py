class Device:
    def turn_on(self):
        pass


class TV(Device):
    def turn_on(self):
        return "TV turned on"


class Radio(Device):
    def turn_on(self):
        return "Radio turned on"


class Remote:
    def __init__(self, device):
        self.device = device

    def press_power(self):
        return self.device.turn_on()


tv_remote = Remote(TV())
radio_remote = Remote(Radio())

print(tv_remote.press_power())  # Output: TV turned on
print(radio_remote.press_power())  # Output: Radio turned on


# If you later add a SmartRemote, you don’t need to change the TV or Radio classes.

# Avoids Inheritance Explosion
# Without the bridge pattern, you may need to create multiple subclasses to handle combinations.
# Instead of having:
# BasicTVRemote
# AdvancedTVRemote
# BasicRadioRemote
# AdvancedRadioRemote
# You simply combine abstraction (Remote) with implementation (Device).

# Advantages of the Bridge Pattern in Python
# The Bridge Pattern is used to decouple abstraction from implementation,
# allowing them to evolve independently. This is useful when dealing with
# systems that may have multiple variants of an abstraction and
# multiple implementations.
#
# Here are the key advantages:
#
# 1. Separation of Concerns
# The pattern separates abstraction (high-level control logic) from
# implementation (low-level system details).
# Changes in one part of the system do not affect the other.
#  Example: A Remote (abstraction) should work with different Device types
#  (TV, Radio, etc.), but the way a device turns on should not affect the
#  remote’s structure.
