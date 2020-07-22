from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
from communication import Communication
import math
from dataBase import db
from PyQt5.QtWidgets import QPushButton

pg.setConfigOption('background', (33, 33, 33))
pg.setConfigOption('foreground', (197, 198, 199))
# UI interface Variables
app = QtGui.QApplication([])
view = pg.GraphicsView()
GraphicUI = pg.GraphicsLayout()
view.setCentralItem(GraphicUI)
view.show()
view.setWindowTitle('Project BAKU: DASHBOARD')
view.resize(1200, 700)


# the class that communicates with the serial port is declared
ser = Communication()
# class that saves in a csv file
db = db()
# Fonts to display only a number
font = QtGui.QFont()
font.setPixelSize(90)


# Title at the top
text = """
\t\tPROJECT:BAKU\t\tGROUND STATION
\t\t\tDashboard of all relevant control data along with real time sensor data
"""
GraphicUI.addLabel(text, col=1, colspan=21)
GraphicUI.nextRow()

# Vertical label on left side
GraphicUI.addLabel('BAKU: GROUND STATION TELEMETRY',
                 angle=-90, rowspan=3)

GraphicUI.nextRow()
# Save Data Buttons

# buttons style
ButtonStyle = "background-color:rgb(29, 185, 84);color:rgb(0,0,0);font-size:24px;"

lb = GraphicUI.addLayout(colspan=21)
proxy = QtGui.QGraphicsProxyWidget()
savebutton = QtGui.QPushButton('Begin Data Logging')
savebutton.setStyleSheet(ButtonStyle)
savebutton.clicked.connect(db.start)
proxy.setWidget(savebutton)
lb.addItem(proxy)
lb.nextCol()


proxy2 = QtGui.QGraphicsProxyWidget()
endbutton = QtGui.QPushButton('End Data Logging')
endbutton.setStyleSheet(ButtonStyle)
endbutton.clicked.connect(db.end)
proxy2.setWidget(endbutton)
lb.addItem(proxy2)


GraphicUI.nextRow()

# GraphicUI
# Distance Graph
l1 = GraphicUI.addLayout(colspan=20, rowspan=2)
l11 = l1.addLayout(rowspan=1, border=(83, 83, 83))
# l1.setContentsMargins(10, 10, 10, 10)
p1 = l11.addPlot(title="Distance Traveled (m)")
# p1.hideAxis('bottom')
curveheight = p1.plot(pen=(29, 185, 84))
dataheight = np.linspace(0, 0, 30)
ptr1 = 0


def updateheight(value):
    global curveheight, dataheight,  ptr1
    dataheight[:-1] = dataheight[1:]
    # value = ser.getData()
    dataheight[-1] = float(value[1])
    ptr1 += 1
    curveheight.setData(dataheight)
    curveheight.setPos(ptr1, 0)


# Velocity Graph
p2 = l11.addPlot(title="Velocity (m/s)")
curva_vel = p2.plot(pen=(29, 185, 84))
datos_vel = np.linspace(0, 0, 30)
ptr6 = 0
vx = 0
vy = 0
vz = 0
vel = 0


def update_vel(value):
    global curva_vel, datos_vel, ptr6, vx, vy, vz, vel
    # 500 es dt
    i = 0
    if(i == 0):
        vzo = float(value[10])
        i += 1

    vx += (float(value[8])) * 500
    vy += (float(value[9])) * 500
    vz += (float(value[10]) - vzo) * 500
    sum = math.pow(vx, 2) + math.pow(vy, 2) + math.pow(vz, 2)
    vel = math.sqrt(sum)
    datos_vel[:-1] = datos_vel[1:]
    datos_vel[-1] = vel
    ptr6 += 1
    curva_vel.setData(datos_vel)
    curva_vel.setPos(ptr6, 0)


l1.nextRow()
l12 = l1.addLayout(rowspan=1, border=(83, 83, 83))

# GraphicUI
# de aceleraciones
GrafAcel = l12.addPlot(title="Acceleration (m/s²)")
# añadiendo leyenda
GrafAcel.addLegend()
GrafAcel.hideAxis('bottom')
curvaAcelX = GrafAcel.plot(pen=(102, 252, 241), name="X")
curvaAcelY = GrafAcel.plot(pen=(29, 185, 84), name="Y")
curvaAcelZ = GrafAcel.plot(pen=(203, 45, 111), name="Z")

DatosAcelX = np.linspace(0, 0)
DatosAcelY = np.linspace(0, 0)
DatosAcelZ = np.linspace(0, 0)
ptr2 = 0


def update_acc(value):
    global curvaAcelX, curvaAcelY, curvaAcelZ, DatosAcelX, DatosAcelY, DatosAcelZ, ptr2
    DatosAcelX[:-1] = DatosAcelX[1:]
    DatosAcelY[:-1] = DatosAcelY[1:]
    DatosAcelZ[:-1] = DatosAcelZ[1:]

    DatosAcelX[-1] = float(value[8])
    DatosAcelY[-1] = float(value[9])
    DatosAcelZ[-1] = float(value[10])
    ptr2 += 1

    curvaAcelX.setData(DatosAcelX)
    curvaAcelY.setData(DatosAcelY)
    curvaAcelZ.setData(DatosAcelZ)

    curvaAcelX.setPos(ptr2, 0)
    curvaAcelY.setPos(ptr2, 0)
    curvaAcelZ.setPos(ptr2, 0)


# GraphicUI
# del gyro
GrafEuler = l12.addPlot(title="Gyroscope")
GrafEuler.hideAxis('bottom')
# añadiendo leyenda
GrafEuler.addLegend()
curvaPitch = GrafEuler.plot(pen=(102, 252, 241), name="Pitch")
curvaRoll = GrafEuler.plot(pen=(29, 185, 84), name="Roll")
curvaYaw = GrafEuler.plot(pen=(203, 45, 111), name="Yaw")

DatosPitch = np.linspace(0, 0)
DatosRoll = np.linspace(0, 0)
DatosYaw = np.linspace(0, 0)
ptr3 = 0


def update_gyro(value):
    global curvaPitch, curvaRoll, curvaYaw, DatosPitch, DatosRoll, DatosYaw, ptr3
    DatosPitch[:-1] = DatosPitch[1:]
    DatosRoll[:-1] = DatosRoll[1:]
    DatosYaw[:-1] = DatosYaw[1:]

    DatosPitch[-1] = float(value[5])
    DatosRoll[-1] = float(value[6])
    DatosYaw[-1] = float(value[7])

    ptr3 += 1

    curvaPitch.setData(DatosPitch)
    curvaRoll.setData(DatosRoll)
    curvaYaw.setData(DatosYaw)

    curvaPitch.setPos(ptr3, 0)
    curvaRoll.setPos(ptr3, 0)
    curvaYaw.setPos(ptr3, 0)


# GraphicUI
# Presion
graf_presion = l12.addPlot(title="Magnetometer")
curva_presion = graf_presion.plot(pen=(102, 252, 241))
datos_presion = np.linspace(0, 0, 30)
ptr4 = 0


def update_presion(value):
    global curva_presion, datos_presion,  ptr4
    datos_presion[:-1] = datos_presion[1:]
    datos_presion[-1] = float(value[4])
    ptr4 += 1
    curva_presion.setData(datos_presion)
    curva_presion.setPos(ptr4, 0)


# GraphicUI
# temperatura
graf_temp = l12.addPlot(title="Control Data")
curva_temp = graf_temp.plot(pen=(29, 185, 84))
datos_temp = np.linspace(0, 0, 30)
ptr5 = 0


def update_temp(value):
    global curva_temp, datos_temp,  ptr5
    datos_temp[:-1] = datos_temp[1:]
    datos_temp[-1] = float(value[3])
    ptr5 += 1
    curva_temp.setData(datos_temp)
    curva_temp.setPos(ptr5, 0)


# Graficos de tiempo, bateria y caida
l2 = GraphicUI.addLayout(border=(83, 83, 83))


# GraphicUI
# del tiempo
GrafTiempo = l2.addPlot(title="Elapsed Time (H:M:S)")
GrafTiempo.hideAxis('bottom')
GrafTiempo.hideAxis('left')
textoTiempo = pg.TextItem("0:00:00", anchor=(0.5, 0.5), color="w")
textoTiempo.setFont(font)
GrafTiempo.addItem(textoTiempo)


def update_tiempo(value):
    global textoTiempo
    textoTiempo.setText('')
    tiempo = round(int(value[0]) / 60000, 2)
    textoTiempo.setText(str(tiempo))


l2.nextRow()

# GraphicUI
# de la batería
GrafBateria = l2.addPlot(title="Current System State")
GrafBateria.hideAxis('bottom')
GrafBateria.hideAxis('left')
textoBateria = pg.TextItem("IDLE", anchor=(0.5, 0.5), color="w")
textoBateria.setFont(font)
GrafBateria.addItem(textoBateria)


def update_bateria(value):
    pass


l2.nextRow()

graf_clibre = l2.addPlot(title="Heading (degrees)")
graf_clibre.hideAxis('bottom')
graf_clibre.hideAxis('left')
text_clibre = pg.TextItem("0.00°", anchor=(0.5, 0.5), color="w")
text_clibre.setFont(font)
graf_clibre.addItem(text_clibre)


def update_clibre(value):
    global text_clibre
    text_clibre.setText('')
    if(value[2] == '0'):
        text_clibre.setText('No')
    else:
        text_clibre.setText('Si')


def update():
    try:
        value = []
        value = ser.getData()
        updateheight(value)
        update_vel(value)
        update_tiempo(value)
        update_acc(value)
        update_gyro(value)
        update_presion(value)
        update_temp(value)
        update_clibre(value)
        db.save(value)
    except IndexError:
        print('iniciando')

    # I don't know if this is necessary
    # QtGui.QApplication.processEvents()


if(ser.isOpen()):
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(2000)
else:
    print("The selected port is not open")
# Start Qt event loop unless running in interactive mode.

if __name__ == '__main__':

    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
