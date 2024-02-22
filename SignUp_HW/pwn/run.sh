#!/bin/bash

# Step 1: Compile sleep.c into exploit.so
gcc -shared -o exploit.so sleep.c

# Check if the compilation was successful
if [ $? -eq 0 ]; then
    echo "Successfully compiled sleep.c into exploit.so"
else
    echo "Compilation failed"
    exit 1
fi

# Step 2: Execute hw0-4.py
python3 hw0-4.py

# Check if the Python script executed successfully
if [ $? -eq 0 ]; then
    echo "Successfully executed hw0-4.py"
else
    echo "Execution of hw0-4.py failed"
    exit 1
fi