# IBG Network Scanner

Scan hosts within a network to find alive ones. 

1. It will scan specified network
2. Display alive hosts
3. Wait for 30 sec
4. Scan again and display removed and added hosts
5. Return to begining

## Installation
Requirements:
* nmap tool (Debian: apt install nmap)
* IBG Logger Library (IBG_Logger.py)

## Usage
Just run script with a subnet 

eg: python scan_network.py 192.168.1.0/24
