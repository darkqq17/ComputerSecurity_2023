## Notepad-Stage1

### Steps:

1. **Retrieve Port Number:**
   - Run the following command to obtain the port number:
     ```
     python3 get_ip.py
     ```
   - Take note of the port number displayed by this script.

2. **Execute Stage 1 Exploit:**
   - Use the port number obtained from the previous step as an argument in the following command:
     ```
     python3 exploit_s1.py [port]
     ```
   - Replace `[port]` with the actual port number.

## Notepad-Stage2

### Steps:

1. **Compile Shellcode:**
   - Run the `make` command to convert the assembly code into raw shellcode:
     ```
     make
     ```

2. **Retrieve Port Number:**
   - Run the `get_ip.py` script again to get the current port number:
     ```
     python3 get_ip.py
     ```
   - Note down the port number provided by the script.

3. **Execute Stage 2 Exploit:**
   - With the new port number, run the Stage 2 exploit script:
     ```
     python3 exploit_s2.py [port]
     ```
   - Ensure to replace `[port]` with the port number you just obtained.

## Notepad-Stage3

### Steps:

1. **Retrieve Port Number:**
   - Run the `get_ip.py` script again to get the current port number:
     ```
     python3 get_ip.py
     ```
   - Note down the port number provided by the script.

2. **Execute get_backend Exploit:**
   - With the new port number, run the Stage 3 exploit script:
     ```
     python3 get_backend.py [port]
     ```
   - Ensure to replace `[port]` with the port number you just obtained.