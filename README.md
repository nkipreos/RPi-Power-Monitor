RPi-Power-Monitor
=================

Code in python for and RPi power monitor with communications to a central server

**Pre Requisites**

For running the following program some Python libraries are needed. These are ConfigParse, os and pyserial. The last one, you must install it.

**Instructions**

A run.sh script is provided, you must configure /etc/rc.local to run it every time the os boots. I would also recommend using a monitoring program or running a crontab for checking if the process is running or otherwise reboot the machine. Some changes may be required for this file for it is intended to be used in a Raspbery Pi.