
file ./donut-verifier
set logging file my_gdb_output.txt
set logging enabled on
starti
b *$rebase(0x1550)
continue
python
memory_values = []
print("Entering Python script")
for i in range(1025):
    try:
        gdb.execute("ni")
        memory_value = gdb.execute("x/1b $rbp - 0x74", to_string=True)
        print(f"Memory Value at $rbp - 0x74: {memory_value}")
        memory_values.append(memory_value)
        
    except gdb.error as e:
        print(f"Error during execution: {e}")
        
    gdb.execute("continue")
with open('memory_values.txt', 'w') as file:
    file.write(str(memory_values))
end
set logging enabled off
quit
