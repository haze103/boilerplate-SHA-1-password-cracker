import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # 1. Load the database of top passwords
    with open('top-10000-passwords.txt', 'r') as f:
        # .strip() removes the newline character at the end of each line
        passwords = [line.strip() for line in f]

    # 2. Load the salts if required
    salts = []
    if use_salts:
        with open('known-salts.txt', 'r') as f:
            salts = [line.strip() for line in f]

    # 3. Iterate through every password in the database
    for password in passwords:
        
        # LOGIC FOR SALTED PASSWORDS
        if use_salts:
            for salt in salts:
                # Check 1: Prepend Salt (salt + password)
                term = salt + password
                hashed_term = hashlib.sha1(term.encode('utf-8')).hexdigest()
                if hashed_term == hash:
                    return password

                # Check 2: Append Salt (password + salt)
                term = password + salt
                hashed_term = hashlib.sha1(term.encode('utf-8')).hexdigest()
                if hashed_term == hash:
                    return password

        # LOGIC FOR UNSALTED PASSWORDS
        else:
            # Hash the password directly
            hashed_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
            
            if hashed_pass == hash:
                return password

    # 4. If the loop finishes with no match found
    return "PASSWORD NOT IN DATABASE"