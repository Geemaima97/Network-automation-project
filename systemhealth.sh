#!/bin/bash

echo "==============================="
echo      "SYSTEM HEALTH CHECKER"
echo "==============================="

echo -e "\nDate\ "
echo $(date)
echo "-------------------------------"
echo -e "\nMemory Usage\ "
free -h
echo "-------------------------------"
echo -e "\nDisk Usage\ "
df -h

echo "-------------------------------"
echo -e "\nUptime\ "
uptime
echo "-------------------------------"
echo -e "\nLogged-in User\ "
who
echo "-------------------------------"

