#!/usr/bin/evn python

import subprocess

print("Easier than running nmap scans manually")
directory_name = input("Enter Directory Name ")
IP = input("Enter IP Address ")



# Makes Directory to put nmap scans.
subprocess.call("mkdir -p " + directory_name + "/nmap", shell=True)

# Nmap commands that I like to run.
subprocess.call("nmap -sS -oA " + directory_name + "/nmap/Silent " + IP, shell=True)
subprocess.call("nmap -A -T4 -p- -oA " + directory_name + "/nmap/Monster " + IP, shell=True)
subprocess.call("nmap --script vuln -oA " + directory_name + "/nmap/Vuln " + IP, shell=True)
subprocess.call("nmap -sU -oA " + directory_name + "/nmap/UDP " + IP, shell=True)
