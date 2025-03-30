import usb.core
import usb.util

dev = usb.core.find(find_all=True)  # найдет подключенные USB-устройства

#  device.write(drive_name, data.txt)  # Запишет на носитель