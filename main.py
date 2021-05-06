#!/usr/bin/python3

from DataProcessor import *
from HTMLGenerator import *

from constants import machines, port, refreshRate
from getpass import getpass

import threading
import paramiko
import time
import sys

class Manager:
        def __init__(self, username, password):
                self.username = username
                self.password = password
                self.threads = [ ]
                self.dataProcessor = DataProcessor()
                HTMLGenerator().generateHeader()

        """
        ssh into target machine and fetch data
        """
        def getMachineActivity(self, i):
                machine = machines[i]
                command = f"top -b -n 1 > top_{i}.txt && cat top_{i}.txt"
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    ssh.connect(machine, port, self.username, self.password)
                    stdin, stdout, stderr = ssh.exec_command(command)
                    machineActivity = stdout.readlines()
                    ssh.close()
                    self.dataProcessor.process(machine, machineActivity[0:5])
                except Exception as e:
                    print(f'Failed to ssh into {machine} with error:\n{e}')
                    sys.exit()
        """
        API to get the program running
        """
        def run(self):
                while True:
                        for i in range(len(machines)):
                                thread = threading.Thread(target = self.getMachineActivity, args=(i,))
                                self.threads.append(thread)
                                thread.start()
                        for thread in self.threads:
                            thread.join()
                                
                        self.dataProcessor.updateCharts()
                        time.sleep(refreshRate)
                        self.threads.clear()
                                

if __name__ == "__main__":
    #  username = input("Enter your quest user ID:\n")
        username = 'zfbharwa'
        password = getpass("Enter the corresponding password:\n")
        manager = Manager(username,password)
        manager.run()
