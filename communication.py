import serial
import serial.tools.list_ports


class Communication:
    baudrate = ''
    portName = ''
    ports = serial.tools.list_ports.comports()
    ser = serial.Serial()

    def __init__(self):
        self.baudrate = 9600
        print("Available Ports: ")
        for port in sorted(self.ports):
            # List of ports: https://stackoverflow.com/a/52809180
            print(("{}".format(port)))
        self.portName = input("Specify Serial port (eg: /dev/ttyUSB0 or COM8): ")
        try:
            self.ser = serial.Serial(self.portName, self.baudrate)
        except serial.serialutil.SerialException:
            print("Could not open: ", self.portName)

    def cerrar(self):
        if(self.ser.isOpen()):
            self.ser.close()
        else:
            print("Already closed")

    def getData(self):
        value = self.ser.readline()  # read line (single value) from the serial port
        decoded_bytes = str(value[0:len(value) - 2].decode("utf-8"))
        # print(decoded_bytes)
        valor = decoded_bytes.split(",")
        return valor

    def isOpen(self):
        return self.ser.isOpen()
