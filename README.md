RPi-Power-Monitor
=================

Code in python for and RPi power monitor with communications to a central server

##Description##

This program reads the data coming in from the serial port from an RF12 interface which receives the information read by an emonTX device designed by open energy monitor.

After reading from the serial port the data is posted to a web service via a JSON API. The stream id's and remote_device_id are sent in the header of the request

##Pre Requisites##

For running the following program some Python libraries are needed. These are **ConfigParse**, **os** and **pyserial**. You must install the last one.

##Instructions##

A run.sh script is provided, you must configure /etc/rc.local to run it every time the os boots. I would also recommend using a monitoring program or running a crontab for checking if the process is running or otherwise reboot the machine. Some changes may be required for this file for it is intended to be used in a Raspbery Pi.

```shell
$ echo ""
```