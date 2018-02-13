#!/usr/bin/env python3
#-*- coding:utf-8 -*-
__author__ = 'Gao Zhengzhong'

import serial
import serial.tools.list_ports

# look for available com port
plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("No availiable com port!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]

    # set serial com port parameter
    serialFd = serial.Serial(port=serialName, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=60)
    print("Available com port name>>>", serialFd.name)
    print("Available com port baudrate>>>", serialFd.baudrate)
    print("Available com port parity>>>", serialFd.parity)
    print("Available com port stopbits>>>", serialFd.stopbits)

    # config D412 device address
    serialFd.write('svc -lab -a 0x50\n'.encode())

    # receive D412 device infomation
    deviceInfo = str(serialFd.read(74))
    index1 = deviceInfo.find("device address")
    index2 = deviceInfo.find("mvbMON")
    print(deviceInfo[index1:index2])     

    # config dynamic BA
    serialFd.write('sva auto\n'.encode()) 

    # receive BA state infomation
    busAdminInfo = str(serialFd.read(61))
    index1 = busAdminInfo.find("Configure dynamic BA")
    index2 = busAdminInfo.find("mvbMON")
    print(busAdminInfo[index1:index2])  

    # scan all devices on MVB bus
    serialFd.write('svd -a\n'.encode()) 

    # receive all devices information on MVB bus
    allDeviceInfo = str(serialFd.readall())
    index1 = allDeviceInfo.find("number of devices")
    index2 = allDeviceInfo.find("mvbMON")
    print(allDeviceInfo[index1:index2])

    # scan all ports on MVB bus
    #serialFd.write('pc -S\n'.encode())

    # receive all ports information on MVB bus
    #print(serialFd.read(100))

# main fuction
if __name__ == '__main__':
    pass

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