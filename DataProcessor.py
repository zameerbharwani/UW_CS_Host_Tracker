from tabulate import tabulate
from constants import machines

#TODO: handle crashed host / host not available 

class DataProcessor:
		def __init__(self):
			self.machineData = { }
			self.machineSpecs = [
		    						['Host', 'CPU Type', '# of CPUs', 'Cores/CPU', 'Threads/Core', 'RAM (GB)', 'Make', 'Model'],
									[machines[0],'Interl(R) Xeon(R) Gold 6148 @ 2.40GHz', 2, 20, 2, 384, 'Supermicro', 'SYS-1029U-E1CR25M'],
									[machines[2],'Interl(R) Xeon(R) Gold 6148 @ 2.40GHz', 2, 20, 2, 384, 'Supermicro', 'SYS-6029P-WTRT'],
									[machines[2], 'Intel(R) Xeon(R) CPU E5-2697A v4 @ 2.60GHz', 2, 16, 2, 256,	'Dell Inc. PowerEdge R730'],
									[machines[3], 'Intel(R) Xeon(R) CPU E5-2697A v4 @ 2.60GHz', 2, 16, 2, 256, 'Dell Inc.	PowerEdge R730'] 
									
                                ]

		def process(self, machine, data):
				def getNumUsers():
						return data[0].split(',')[2].split(' ')[1]

				def getLoadAverage():
						loadAverage = ['0']*3
						load_avg = data[0].split(',')[3:]
						loadAverage[0] = load_avg[0].split(' ')[-1] # 1 minute
						loadAverage[1] = load_avg[1] # 5 minutes
						loadAverage[2] = load_avg[2][:-1] # 15 minutes
						return loadAverage

				def getCPU_Usage():
						CPU_usage = ['0']*3
						usage = data[2].split(',')[:4]
						CPU_usage[0] = usage[0].split(' ')[2] # user
						CPU_usage[1] = usage[1].split(' ')[2] # sys
						CPU_usage[2] = usage[3].split(' ')[1] # idle
						return CPU_usage

				def getTime():
					time = data[0].split('-')[1].split('up')[0][1:-1]
					return time # time of top
				
				numUsers = getNumUsers()
				loadAverage = getLoadAverage()
				time = getTime()
				self.machineData[machine] = {'time': time, 'users':numUsers, 'load':loadAverage} 

		def publish(self):

				"""
				Table of machine specs
				"""

				"""
				TODO
				1) generate table with specs
				2) time vs # users graph (legend is each machine)
				3) time vs load avg (legend is each machine, time interval)
				"""



