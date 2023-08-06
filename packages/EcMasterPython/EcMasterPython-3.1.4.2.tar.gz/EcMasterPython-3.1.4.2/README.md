# EC-Master-Python

The wrapper provides a Python interface to use the acontis EtherCAT Master stack (EC-Master),
acontis EtherCAT Simulator (EC-Simulator) and RAS Client/Server.

Introduction
------------

Similar to the other demos the EcMasterDemoPython shows how to call the EtherCAT Master API. 
There is also a Python demo for the EC-Simulator. The python demos can also run in interactive 
mode e.g. to set an output of the EtherCAT network or something else. This is very useful to 
quickly test different behaviors of the EtherCAT network e.g. with the EC-Simulator.

For more information please refer the user manual:
https://public.acontis.com/manuals/EC-Master/3.1/html/ec-master-python/index.html

The binaries are not included into the package. 

Please contact our support to request an EVAL version:
https://www.acontis.com/ 

Operating systems and tools
---------------------------

* Supported Operating Systems: Windows (Python 3.7), Linux (Python 3.7)
* Supported IDE: Python IDLE Shell, Microsoft Visual Studio 2019, Microsoft Visual Studio Code

Example
-------

After installation, the demo can be used e.g. by creating a new file "demo.py"
and insert the following code:

from EcMasterPython import *
demo = EcMasterDemoPython()
demo.pAppParms.tRunMode = RunMode.Master
demo.pAppParms.dwBusCycleTimeUsec = 4000
demo.pAppParms.szENIFilename = "ENI.xml"
demo.pAppParms.szLinkLayer = "winpcap 127.0.0.1 1"
demo.pAppParms.nVerbose = 3
demo.startDemo()
print("EcMasterDemoPython is running.")
print("Type demo.help() for interactive help.")
#demo.processImage.variables.Slave_1005__EL2008_.Channel_1.Output.set(1)
#demo.processImage.variables.Slave_1005__EL2008_.Channel_1.Output.get()
#demo.processImage.variables.Slave_1005__EL2008_.Channel_1.Output.dmp()
#demo.stopDemo()
