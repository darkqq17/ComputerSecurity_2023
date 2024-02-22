# Makefile for Assembling, Linking, and Extracting Shellcode

# Assembler, Linker, and Objcopy
ASM = nasm
LD = ld
OBJCOPY = objcopy

# Source, Object, Executable, and Shellcode Binary
SRC = shellcode.asm
OBJ = shellcode.o
EXECUTABLE = shellcode_executable
SHELLCODE_BIN = shellcode.bin

# Assembly Flags
ASM_FLAGS = -f elf64

# Linker Flags
LD_FLAGS = 

# Default target
all: $(SHELLCODE_BIN)

# Step 1: Assemble the source file into an object file
$(OBJ): $(SRC)
	$(ASM) $(ASM_FLAGS) $(SRC) -o $(OBJ)

# Step 2: Link the object file to create an executable
$(EXECUTABLE): $(OBJ)
	$(LD) $(LD_FLAGS) $(OBJ) -o $(EXECUTABLE)

# Step 3: Extract raw shellcode from the executable
$(SHELLCODE_BIN): $(EXECUTABLE)
	$(OBJCOPY) -O binary -j .text $(EXECUTABLE) $(SHELLCODE_BIN)

# Clean up
clean:
	rm -f $(OBJ) $(EXECUTABLE) $(SHELLCODE_BIN)

# Phony targets
.PHONY: all clean
