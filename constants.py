MACHINE_PREFIX = 'ubuntu'
MACHINE_SUFFIX = '.student.cs.uwaterloo.ca'
machines = [
		    f'{MACHINE_PREFIX}1804-002{MACHINE_SUFFIX}', 
		    f'{MACHINE_PREFIX}1804-010{MACHINE_SUFFIX}',
                    f'{MACHINE_PREFIX}2004-002{MACHINE_SUFFIX}',
		    f'{MACHINE_PREFIX}2004-004{MACHINE_SUFFIX}'
	    ]

port = 22
refreshRate = 300 # seconds (5 minutes)

## Graphing ##
alpha = 0.5
markersize = 2
markers = ['.','*','o','3']
