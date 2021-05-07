from constants import machines, alpha
from Utils import *
from HTMLGenerator import *
import numpy as np
import glob
import matplotlib.pyplot as plt

#TODO: handle crashed host / host not available 

class DataProcessor:
        def __init__(self):
            self.machineData =  [ ['Host', '# of Users', 'Load Average (1/5/15 minutes)'] ]
            self.times = [ ]
            self.htmlGenerator = HTMLGenerator()
            # sourced from: https://uwaterloo.ca/computer-science-computing-facility/teaching-hosts
            self.machineSpecs = [
                                    ['Host', 'CPU Type', '# of CPUs', 'Cores/CPU', 'Threads/Core', 'RAM (GB)', 'Make', 'Model'],
                                    [machines[0], 'Intel(R) Xeon(R) Gold 6148 @ 2.40GHz', 2, 20, 2, 384,'Supermicro','SYS-1029U-E1CR25M'],
                                    [machines[1], 'Intel(R) Xeon(R) CPU E5-2697A v4 @ 2.60GHz', 2, 16, 2, 256, 'Dell Inc.', 'PowerEdge R730'],
                                    [machines[2], 'AMD EPYC 7532', 2, 32, 2, 256, 'Dell Inc.', 'PowerEdge R7525'],
                                    [machines[3], 'AMD EPYC 7532', 2, 32, 2, 256, 'Dell Inc.', 'PowerEdge R7525']
                                    
                            ]
            HTMLGenerator.generateStaticBody(self.machineSpecs)
            self.graphData = {
                    machines[0]: {'numUsers':0, 'loadAverage':0},
                    machines[1]: {'numUsers':0, 'loadAverage':0},
                    machines[2]: {'numUsers':0, 'loadAverage':0},
                    machines[3]: {'numUsers':0, 'loadAverage':0}
                    }
            
            if not glob.glob('*.npz'): # no historical data available
                # machine_x, machine_i_y, 0 <= i < 4
                print('No historical data found...')
                time = np.array([])
                machine0_users, machine0_loadAverage = np.array([]), np.array([])
                machine1_users, machine1_loadAverage = np.array([]), np.array([])
                machine2_users, machine2_loadAverage = np.array([]), np.array([])
                machine3_users, machine3_loadAverage = np.array([]), np.array([])
                
                np.savez('timeSeries_numUsers.npz', time=time, machine0_users=machine0_users, machine1_users=machine1_users, 
                        machine2_users=machine2_users, machine3_users=machine3_users)

                np.savez('timeSeries_loadAverage.npz', time=time, machine0_loadAverage=machine0_loadAverage, machine1_loadAverage=machine1_loadAverage,
                       machine2_loadAverage=machine2_loadAverage, machine3_loadAverage=machine3_loadAverage)

        def process(self, machine, data):
                def getNumUsers():
                    top_users = data[0].split(',')[2].split(' ')
                    print(top_users)
                    return float(top_users[len(top_users)-2])

                def getLoadAverage():
                        loadAverage = ['0']*3
                        load_avg = data[0].split(',')[3:]
                        loadAverage[0] = float(load_avg[0].split(' ')[-1]) # 1 minute
                        loadAverage[1] = float(load_avg[1]) # 5 minutes
                        loadAverage[2] = float(load_avg[2][:-1]) # 15 minutes
                        return loadAverage[1]

                def getCPU_Usage():
                        CPU_usage = ['0']*3
                        usage = data[2].split(',')[:4]
                        CPU_usage[0] = float(usage[0].split(' ')[2]) # user
                        CPU_usage[1] = float(usage[1].split(' ')[2]) # sys
                        CPU_usage[2] = float(usage[3].split(' ')[1]) # idle
                        return CPU_usage

                def getTime():
                    time = data[0].split('-')[1].split('up')[0][1:-1]
                    return time # time of top
                
                numUsers = getNumUsers()
                loadAverage = getLoadAverage()
                self.times.append(getTime())
                self.machineData.append([machine, numUsers, loadAverage])
                self.graphData[machine] = {'numUsers':numUsers, 'loadAverage':loadAverage}

        def updateCharts(self):
            meanTime = Utils.meanTime(self.times)
            numUsers_data = np.load('timeSeries_numUsers.npz')
            loadAverage_data = np.load('timeSeries_loadAverage.npz')

            time = numUsers_data['time'] # same as loadAverage_data['time']
            time = np.append(time,meanTime)

            machine0_users = numUsers_data['machine0_users']
            machine0_users = np.append(machine0_users,self.graphData[machines[0]]['numUsers'])

            machine1_users = numUsers_data['machine1_users']
            machine1_users = np.append(machine1_users,self.graphData[machines[1]]['numUsers'])

            machine2_users = numUsers_data['machine2_users']
            machine2_users = np.append(machine2_users,self.graphData[machines[2]]['numUsers'])

            machine3_users = numUsers_data['machine3_users']
            machine3_users = np.append(machine3_users,self.graphData[machines[3]]['numUsers'])

            np.savez('timeSeries_numUsers.npz', time=time, machine0_users=machine0_users, machine1_users=machine1_users, 
                    machine2_users=machine2_users, machine3_users=machine3_users)
            
            machine0_loadAverage = loadAverage_data['machine0_loadAverage']
            machine0_loadAverage = np.append(machine0_loadAverage,self.graphData[machines[0]]['loadAverage'])

            machine1_loadAverage = loadAverage_data['machine1_loadAverage']
            machine1_loadAverage = np.append(machine1_loadAverage,self.graphData[machines[1]]['loadAverage'])

            machine2_loadAverage = loadAverage_data['machine2_loadAverage']
            machine2_loadAverage = np.append(machine2_loadAverage,self.graphData[machines[2]]['loadAverage'])

            machine3_loadAverage = loadAverage_data['machine3_loadAverage']
            machine3_loadAverage = np.append(machine3_loadAverage,self.graphData[machines[3]]['loadAverage'])

            np.savez('timeSeries_loadAverage.npz', time=time, machine0_loadAverage=machine0_loadAverage, machine1_loadAverage=machine1_loadAverage, 
                        machine2_loadAverage=machine2_loadAverage, machine3_loadAverage=machine3_loadAverage)

            m0, = plt.plot(time, machine0_users, label='1804-002', linestyle=':', marker='o', alpha=alpha)
            m1, = plt.plot(time, machine1_users, label='1804-010', linestyle='-.', marker='o',alpha=alpha)
            m2, = plt.plot(time, machine2_users, label='2004-002', linestyle='--', marker='o',alpha=alpha)
            m3, = plt.plot(time, machine3_users, label='2004-004', marker='o')
            plt.legend(handles=[m0, m1, m2, m3], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='xx-small')
            ax = plt.gca()
            ax.axes.xaxis.set_ticks([])
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            plt.title('Active Users on CS Student Servers')
            plt.savefig('users_vs_time.png', dpi=300, bbox_inches='tight')
            plt.close()

            m0, = plt.plot(time, machine0_loadAverage, label='1804-002', linestyle=':', marker='o', alpha=alpha)
            m1, = plt.plot(time, machine1_loadAverage, label='1804-010', linestyle='-.', marker='o', alpha=alpha)
            m2, = plt.plot(time, machine2_loadAverage, label='2004-002', linestyle='--', marker='o', alpha=alpha)
            m3, = plt.plot(time, machine3_loadAverage, label='2004-004', marker='o',alpha=alpha)
            plt.legend(handles=[m0, m1, m2, m3], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='xx-small')
            ax = plt.gca()
            ax.axes.xaxis.set_ticks([])
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            plt.title('CS Student Server Load Average')
            plt.savefig('load_vs_time.png', dpi=300, bbox_inches='tight')
            plt.close()
            
            HTMLGenerator.generateDynamicBody(self.machineData,meanTime)
            self.machineData =  [self.machineData[0]]
