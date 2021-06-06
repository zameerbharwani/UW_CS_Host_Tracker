# UW CS Host Tracker
The following repository contains the scripts used to track the status of all the UW CS machines available for student usage.
There are several machines available for student use, though the load is not evenly distributed.
The data generated is hosted [here](http://csclub.uwaterloo.ca/~zfbharwa/uw_cs_host_tracker/), which you can reference to decide which machine to choose.

 ## Usage
 The script is meant to be running in the background, around the clock. The current refresh or update rate, as specified in the _constants.py_ file, 
 is set to 5 minutes. The account which executes this script must be that of a CS student, or someone with access to the CS linux machines, else the _ssh_ will fail.

 ## Preview

 ![image](/preview.png)
