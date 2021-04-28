#!/usr/bin/python3

from DataProcessor import *
from HTMLGenerator import *
from constants import machines, port, refreshRate
from getpass import getpass
import threading
import paramiko
import time

class Manager:
        def __init__(self, username, password):
                self.username = username
                self.password = password
                self.threads = [ ]
                self.dataProcessor = DataProcessor()
                self.htmlGenerator = HTMLGenerator()
                self.htmlGenerator.generatePage()

        """
        ssh into target machine and fetch data
        """
        def getMachineActivity(self, i):
                machine = machines[i]
                command = f"top -b -n 1 > top_{i}.txt && cat top_{i}.txt"
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(machine, port, self.username, self.password)
                stdin, stdout, stderr = ssh.exec_command(command)
                machineActivity = stdout.readlines()
                ssh.close()
                self.dataProcessor.process(machine, machineActivity[0:5])
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
                                

if __name__ == "__main__":
        username = input("Enter your quest user ID:\n")
        password = getpass("Enter the corresponding password:\n")
        manager = Manager(username,password)
        manager.run()
