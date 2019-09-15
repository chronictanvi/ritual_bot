import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

import adafruit_thermal_printer
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

printer = ThermalPrinter(uart)

printer.feed(1)

printer.size = adafruit_thermal_printer.SIZE_LARGE
printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
printer.print("ritualbot")

printer.feed(1)

printer.size = adafruit_thermal_printer.SIZE_SMALL
printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT
printer.print("We all need our daily rituals")
printer.print("that get us through the day.")
printer.feed(1)
printer.print("Looking for a new one?")
printer.print("Look no further!")
printer.feed(1)
printer.print("Press this button down here,")
printer.print("for a ritual of your very own!")
printer.feed(1)

printer.bold = True
printer.print("|||")
printer.print("vvv")
printer.feed(3)
