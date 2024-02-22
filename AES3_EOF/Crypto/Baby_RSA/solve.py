import logging
from functools import reduce
from pwn import remote
import gmpy2
from Crypto.Util.number import inverse, long_to_bytes

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

NUM_SAMPLES = 3  # Number of samples to collect for CRT

def fetch_rsa_components():
    """
    Fetches RSA components (modulus, exponent, encrypted flag) from the remote server.
    Returns:
        tuple: A tuple (n, e, encrypted_flag).
    """
    try:
        r = remote("chal1.eof.ais3.org", 10002)
        n_e_line = r.recvline().decode().split(", ")
        n = int(n_e_line[0].split("=")[1])
        e = int(n_e_line[1].split("=")[1])
        encrypted_flag = int(r.recvline().decode().split(": ")[1])
        r.close()
        return n, e, encrypted_flag
    except Exception as e:
        logger.error(f"Error fetching data from server: {e}")
        raise

def crt_solve(moduli, remainders):
    """
    Solves the Chinese Remainder Theorem for given moduli and remainders.
    Args:
        moduli (list): List of moduli.
        remainders (list): List of remainders.
    Returns:
        int: Solution of the CRT.
    """
    product = reduce(lambda x, y: x * y, moduli)
    result = 0
    for modulus, remainder in zip(moduli, remainders):
        partial_product = product // modulus
        inverse_element = inverse(partial_product, modulus)
        result += remainder * partial_product * inverse_element
    return result % product

def main():
    """
    Main function to execute the RSA decryption challenge.
    """
    moduli, encrypted_flags = [], []
    for _ in range(NUM_SAMPLES):
        n, e, encrypted_flag = fetch_rsa_components()
        moduli.append(n)
        encrypted_flags.append(encrypted_flag)
    
    combined_solution = crt_solve(moduli, encrypted_flags)
    cube_root, is_exact = gmpy2.iroot(combined_solution, 3)

    if is_exact:
        decrypted_flag = long_to_bytes(cube_root)
        logger.info(f"Decrypted Flag: {decrypted_flag.decode()}")
    else:
        logger.warning("Failed to find exact cube root for decryption.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unexpected error: {e}")