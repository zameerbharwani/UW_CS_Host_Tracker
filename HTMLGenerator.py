from tabulate import tabulate
from constants import machines

class HTMLGenerator:
    def __init__(self):
        self.machineSpecs = [
                                    ['Host', 'CPU Type', '# of CPUs', 'Cores/CPU', 'Threads/Core', 'RAM (GB)', 'Make', 'Model'],
                                    [machines[0], 'Interl(R) Xeon(R) Gold 6148 @ 2.40GHz', 2, 20, 2, 384, 'Supermicro', 'SYS-1029U-E1CR25M'],
                                    [machines[1], 'Interl(R) Xeon(R) Gold 6148 @ 2.40GHz', 2, 20, 2, 384, 'Supermicro', 'SYS-6029P-WTRT'],
                                    [machines[2], 'Intel(R) Xeon(R) CPU E5-2697A v4 @ 2.60GHz', 2, 16, 2, 256, 'Dell Inc.', 'PowerEdge R730'],
                                    [machines[3], 'Intel(R) Xeon(R) CPU E5-2697A v4 @ 2.60GHz', 2, 16, 2, 256, 'Dell Inc.', 'PowerEdge R730'] 
                                    
                            ]
    
    def generateHeader(self):
        return """ 
                <head>
		    <style>
			footer {
	  			text-align: center;
		    		padding: 3px;
				color: #A9A9A9;
				position: fixed;
				left: 0;
				bottom: 0;
				width: 100%;
			}
		</style>
	    </head>
        """
    def generateBody(self):
        return f"""
                    <body>
		        <h1> UWaterloo CS Machine Status </h1>
                        {tabulate(self.machineSpecs, headers='firstrow', tablefmt='html')}
		        <footer>
			    <p>Author: Zameer Bharwani</p>
		        </footer>
	            </body>
                """
    def generatePage(self):
        with open('index.html', 'w+') as file:
            file.write('<!DOCTYPE html>')
            file.write('\n<html>')
            file.write(f'{self.generateHeader()}')
            file.write(f'{self.generateBody()}')
            file.write('\n</html>')

