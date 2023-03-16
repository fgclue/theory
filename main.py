#/bin/python3

# Imports
import os, sys, subprocess

shellc = "theory"
ver = "0.1"
print(f"Theory v{ver}")
i = 0
while(i==0):
    command = input(f"{shellc}% ")
    commandd = command.split()
    if command == "quit":
        exit();
    if commandd[0] == "config":
        if commandd[1]:
            if command[1] == "edit":
                print("CONFIG\n\nSHELL - What shows in your shell (default=theory1, NO SPACES)")
                if commandd[2]:
                    if commandd[3]:
                        if commandd[3] == "shell":
                            shellc = commandd[3]
