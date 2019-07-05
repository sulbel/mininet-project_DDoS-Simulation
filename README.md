# mininet-project

Final project from CSC4501 - Fall '17; using Mininet and Python socket API to simulate a DDoS attack.


## Contents

### Instructions Folder

Contains a .pdf copy of the project instructions.

### Code Folder

Contains the .py source code for accomplishing this task.  
A brief overview of each code file:
  * UDPServer.py - simple UDP server; socket receives a message from client, then sends message.upper() back to client
  * UDPClient.py - simple UDP client; sends a specified number of messages (controlled by loop parameter) to server 
  * myMininet.py - simulates DDOS; class myDataCenterTopo() configures data center topology 

## Testing

### Scenarios/Parameters

The following scenarios were used for testing performance:
  * Scale the number of connected hosts over the range: 8, 16, 32, 64, 128
  * Record data center bandwidth when each host sends 2, 20, 200 messages with content "junk"
  * Record data center bandwidth when each host sends 2, 20, 200 messages with content "junk " * 600


### Results

The data center bandwidth results for each test case are contained in the `/results` folder
