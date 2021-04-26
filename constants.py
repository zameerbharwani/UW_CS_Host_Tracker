MACHINE_PREFIX = 'ubuntu1804'
MACHINE_SUFFIX = '.student.cs.uwaterloo.ca'
machines = [
		f'{MACHINE_PREFIX}-002{MACHINE_SUFFIX}', 
        	f'{MACHINE_PREFIX}-004{MACHINE_SUFFIX}',
		f'{MACHINE_PREFIX}-008{MACHINE_SUFFIX}',
		f'{MACHINE_PREFIX}-010{MACHINE_SUFFIX}'
	    ]

port = 22
refreshRate = 300 # seconds (5 minutes)
