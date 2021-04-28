from constants import machines

#TODO: handle crashed host / host not available 

class DataProcessor:
        def __init__(self):
            self.machineData = { }
            
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

        def updateCharts(self):

                """
                TODO
                2) time vs # users graph (legend is each machine)
                3) time vs load avg (legend is each machine, time interval)
                """



