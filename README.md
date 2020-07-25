# Ground station Telemetry UI

![Build Status](https://img.shields.io/github/last-commit/RaymondBello/Telemetry-UI) ![Build Status](https://img.shields.io/github/issues-raw/RaymondBello/Telemetry-UI) ![Build Status](https://img.shields.io/github/contributors/RaymondBello/Telemetry-UI?color) 
![Build Status](https://img.shields.io/github/languages/top/RaymondBello/Telemetry-UI) ![Build Status](https://img.shields.io/github/languages/count/RaymondBello/Telemetry-UI) 
![Build Status](https://img.shields.io/github/repo-size/RaymondBello/Telemetry-UI?color=red) 

This program is designed to be a Ground Station Telemetry Dashboard UI where various sensor data components can be displayed in real time.

![imagen](https://i.imgur.com/RbEPwcC.jpg)

## Table of contents
* [General Info](#general-info)
* [Modules](#modules)
* [Setup](#setup)
* [How does it work?](#how-does-it-work)
* [Sources](#sources)


## General info
The purpose of this project is to make the data transmitted by an OBC (on board computer) or a CanSat understandable at first sight through a text string on a serial port.

## Modules
Modules required for this project:

```
numpy == 1.18.2
PyQt5 == 5.14.2
PyQt5-sip == 12.7.2
pyqtgraph == 0.10.0
pyserial == 3.4
```


## Setup
To run it you have to open the terminal in the folder and type:
```
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python3 interface.py
```
if you don't have the electronics you can still use it! When the terminal asks you to write a serial port, write anything and it will work, obviously it won't trace any data.

## How does it work?
### How does it sample?
Every 500 ms a sample is taken, this number comes from the Arduino data rate. 
The loop is:
```
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(500)
```

### What values uses?
The `update()` function updates the graphics and text of the interface. The first thing it does is get a list of the information to be updated.


### How does it store the information?
Clicking on the **Begin Data Logging** button calls a function of the **db** class that changes a state that determines whether the `save` method writes the information in the list. 

## Sources

*"If I have seen further than others, it is by standing upon the shoulders of giants."*

* Sepúlveda, S. Reyes, P. Weinstein, A. (2015). [Visualizing physiological signals in real-time](https://bit.ly/2XIRzyw). doi: 10.25080/Majora-7b98e3ed-01c
* Golubev, P. (2018). [Run Real-time pyqtgraph in PlotWidget GUI.](https://bit.ly/2VeXSIv)
* Pythonspot.(n.d). [PyQt5.](https://pythonspot.com/pyqt5/)
* [Mr. Tom](https://bit.ly/3amndEZ). (2016). [Calculate speed from accelerometer](https://bit.ly/3acX3nP).
* Selfert, K. Camacho, O. (2007). [Implementing Positioning Algorithms Using Accelerometers](https://bit.ly/2REEH8X). Freescale Semiconductor.
* Many other cool people on stack overflow.
