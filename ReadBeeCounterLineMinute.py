#!/usr/bin/env python

import serial           ## Load the serial library
import datetime         ## Load the time library
import os

## Select and configure the port
myPort = serial.Serial('/dev/ttyACM0', 9600, timeout = 10)

## Defining variables

Sync = False
## Sync_char = '0000\t9999\t'
Sync_char = 'S,'
DBuff = '111'
lenD = len(DBuff)


## Finding Sync_char Loop


while not DBuff == Sync_char :

        ## Looping a "virtual" Buffer: 
        DBuff = ''.join([DBuff[1:lenD-1], myPort.read()])
        

## When  synchronism is find start saving data:

## Loop for each minute: 

step = 0
timer = datetime.datetime
final = 1435 ##1440 minuts en un dia

## Creem la carpeta 

prepath = "/media/F45C-CD70/BeeCounterSave/"
time_now = timer.now()
minute = time_now.minute
day = "_".join(time_now.isoformat().split(":")[0:2])[0:10]

os.mkdir(prepath + day + "/")


while (step  < final):

        ## Generating a new file for every minute: 

        time_now = timer.now()
        minute = time_now.minute
        date = "_".join(time_now.isoformat().split(":")[0:2])
        if (day == date[0:10]):
                path = prepath + day + "/BeeCounter" + date + ".csv"
                logfile = open(path, "w")

                ## Saving data until is the same minute: 

                minute_local = minute
                while (minute == minute_local) :

                        time_now = timer.now()
                        minute_local = time_now.minute
                        logfile.write(time_now.isoformat()+',')
                        entrada  = myPort.readline()
                        logfile.write(entrada)

                logfile.close
                step += 1
        else:
                step = final

	
	
	

## Close the port so other applications can use it.
myPort.close()

