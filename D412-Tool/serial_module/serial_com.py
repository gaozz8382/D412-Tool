#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'Gao Zhengzhong'

import serial
import serial.tools.list_ports

# serial communication
class SerialComThread(object):
    def __init__(self):
        # open com port
        self.port = serial.Serial(port='COM6', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=2)

    # define serial com waiting
    def waiting(self):
        if not self.waiting is None:
            self.waiting()        

    # send command
    def sendCommand(self, cmd):
        self.port.write(cmd)
        response = self.port.readall()
        response = self.convertToHex(response)
        return response

    # convert to 0x data 
    def convertToHex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result

# look for available com port
plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("No availiable com port!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]

    # set serial com port parameter
    serialFd = serial.Serial(port=serialName, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=60)
    print("Available com port>>>", serialFd.name)
    print("Available com port baudrate>>>", serialFd.baudrate)

if serialFd.is_open:
    serialFd.write('svc -lab -a 0x50\n'.encode())
 
    # serialFd.write('sva auto\n'.encode())  
    # infoLength = serialFd.in_waiting
    # info = serialFd.read()
    # print("get info from serial port:", infoLength)
    # serialFd.write('svd -a\n'.encode())
else:
    print("No availiable com port!")

# main fuction
if __name__ == '__main__':
    pass