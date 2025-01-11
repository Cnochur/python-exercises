import time, csv


easy_questions = [
    {"question": "What is the primary purpose of a firewall?", "answers": ["To protect against viruses", "To block unauthorized access", "To monitor network traffic", "To improve internet speed"], "correct": 1},
    {"question": "Which of the following is an example of multi-factor authentication?", "answers": ["Username and password", "Password and email", "Password and fingerprint", "Username and security question"], "correct": 2},
    {"question": "What does HTTPS stand for?", "answers": ["HyperText Transfer Protocol", "HyperText Transmission Protocol", "HyperText Transfer Protocol Secure", "Hyper Transfer Protocol Secure"], "correct": 2},
    {"question": "What is phishing?", "answers": ["A method to secure passwords", "A type of virus", "A social engineering attack", "A form of encryption"], "correct": 2},
    {"question": "What is the purpose of encryption?", "answers": ["To speed up data transfer", "To protect data confidentiality", "To prevent data from being corrupted", "To increase data storage space"], "correct": 1},
    {"question": "What does the term 'malware' refer to?", "answers": ["A type of hardware", "A malicious software", "A type of virus scanner", "A backup software"], "correct": 1},
    {"question": "Which of the following is a strong password example?", "answers": ["12345", "password", "P@ssw0rd!22", "abcdefg"], "correct": 2},
    {"question": "What is the primary function of an antivirus program?", "answers": ["To clean hard drive", "To protect against malware", "To speed up computer", "To manage system updates"], "correct": 1},
    {"question": "What is a DDoS attack?", "answers": ["Data-driven attack", "Distributed denial of service attack", "Direct data overloading service", "Distributed data offloading system"], "correct": 1},
    {"question": "What is a VPN used for?", "answers": ["To speed up internet connection", "To secure your internet connection", "To increase bandwidth", "To monitor network traffic"], "correct": 1},
    {"question": "Which of these is a form of social engineering?", "answers": ["Brute force attack", "Phishing", "Ransomware", "SQL Injection"], "correct": 1},
    {"question": "What does the term 'zero-day exploit' mean?", "answers": ["A well-known vulnerability", "An attack after a vulnerability is discovered", "An attack using a newly discovered vulnerability", "A defensive measure against malware"], "correct": 2},
    {"question": "What is two-factor authentication?", "answers": ["A method to scan for viruses", "Using two passwords", "A way to encrypt files", "A security method requiring two forms of verification"], "correct": 3},
    {"question": "What is ransomware?", "answers": ["A type of password manager", "A software that encrypts data and demands payment", "A form of malware that improves computer speed", "A tool for system updates"], "correct": 1},
    {"question": "What is a botnet?", "answers": ["A collection of infected computers used for malicious purposes", "A type of firewall", "A form of encryption", "A type of antivirus software"], "correct": 0},
    {"question": "Which of the following is a typical sign of a phishing email?", "answers": ["Personalized greeting", "A request for sensitive information", "Spelling and grammar checks", "Professional signature"], "correct": 1},
    {"question": "What is a VPN's main purpose?", "answers": ["To block malicious websites", "To mask your IP address and encrypt your connection", "To manage network traffic", "To detect cyber threats"], "correct": 1},
    {"question": "Which of the following is a good practice for securing a password?", "answers": ["Use personal information", "Use the same password across multiple sites", "Use a mix of characters and symbols", "Write it down on paper"], "correct": 2},
    {"question": "What is a common way to prevent SQL injection?", "answers": ["Use encrypted passwords", "Use firewalls", "Sanitize input data", "Disable all ports"], "correct": 2},
    {"question": "What does 'patching' refer to in cybersecurity?", "answers": ["Installing software updates", "Clearing browser history", "Changing system passwords", "Disabling unused accounts"], "correct": 0},
    {"question": "What is the purpose of a security audit?", "answers": ["To review and improve an organization's cybersecurity practices", "To install antivirus software", "To generate network traffic reports", "To create system backups"], "correct": 0},
    {"question": "What is the main purpose of a honeypot in cybersecurity?", "answers": ["To attract and trap hackers", "To encrypt data", "To monitor system performance", "To store sensitive information"], "correct": 0},
    {"question": "What is a Trojan horse in cybersecurity?", "answers": ["A type of password manager", "A form of social engineering", "A type of malware that disguises itself as legitimate software", "A software firewall"], "correct": 2},
    {"question": "What is the main goal of cybersecurity?", "answers": ["To prevent data loss and unauthorized access", "To monitor network traffic", "To improve internet speed", "To install firewalls"], "correct": 0},
    {"question": "What does the term 'patch Tuesday' refer to?", "answers": ["A regular update cycle for Microsoft software", "A virus scan tool", "A method for data recovery", "A type of backup solution"], "correct": 0},
    {"question": "What is a brute force attack?", "answers": ["A method of social engineering", "An attempt to gain unauthorized access through trial and error", "An attack on a network's physical infrastructure", "A method for data encryption"], "correct": 1}
]
medium_questions = [
    {"question": "What is the primary difference between a virus and a worm?", "answers": ["A virus requires user interaction to spread, a worm does not", "A virus is used to encrypt data, a worm is used to steal passwords", "A virus spreads via email, a worm spreads via websites", "A virus can only infect Windows systems, a worm can infect all operating systems"], "correct": 0},
    {"question": "Which of the following is a method for preventing cross-site scripting (XSS) attacks?", "answers": ["Input validation and sanitization", "Using CAPTCHA forms", "Using two-factor authentication", "Encrypting passwords"], "correct": 0},
    {"question": "What is the purpose of the 'principle of least privilege'?", "answers": ["Allow users to access as much information as they need", "Limit users' access to the minimum amount of resources required", "Grant administrative access to all users", "Increase access to critical resources"], "correct": 1},
    {"question": "Which of the following is a key component of public key infrastructure (PKI)?", "answers": ["Symmetric encryption", "Certificate authorities (CAs)", "Secure hash algorithms", "Token-based authentication"], "correct": 1},
    {"question": "What is a man-in-the-middle (MITM) attack?", "answers": ["An attack where the attacker intercepts communication between two parties", "An attack where malware infects both parties in a conversation", "An attack where the attacker sends phishing emails", "An attack that prevents access to a website by flooding it with traffic"], "correct": 0},
    {"question": "What is a common use of hashing algorithms in cybersecurity?", "answers": ["To verify data integrity", "To encrypt sensitive data", "To generate secure passwords", "To generate public keys"], "correct": 0},
    {"question": "Which of the following protocols is used for secure communication over the internet?", "answers": ["FTP", "HTTP", "SMTP", "TLS/SSL"], "correct": 3},
    {"question": "Which type of attack is an SQL injection?", "answers": ["DoS attack", "Network sniffing", "Input validation attack", "Social engineering attack"], "correct": 2},
    {"question": "What is the purpose of a security information and event management (SIEM) system?", "answers": ["To store passwords securely", "To detect and analyze security threats in real time", "To perform network traffic analysis", "To block unauthorized access to systems"], "correct": 1},
    {"question": "Which of the following is an example of a privilege escalation attack?", "answers": ["An attacker uses a user’s credentials to access their email", "An attacker exploits a bug to gain higher-level system access", "An attacker intercepts data during transmission", "An attacker sends a phishing email"], "correct": 1},
    {"question": "What is the function of a sandbox in cybersecurity?", "answers": ["A tool for scanning network traffic", "A restricted environment for safely testing potentially harmful software", "A method for encrypting communications", "A backup solution"], "correct": 1},
    {"question": "What does 'endpoint security' typically protect?", "answers": ["Network routers", "Servers", "User devices such as laptops and smartphones", "Cloud infrastructure"], "correct": 2},
    {"question": "Which of the following is an example of a 'zero-day' vulnerability?", "answers": ["A flaw that is discovered and exploited before a patch is released", "A vulnerability that has been known for years", "A vulnerability that is intentionally left in the software", "A vulnerability that is fixed in an upcoming update"], "correct": 0},
    {"question": "What does the term 'social engineering' refer to?", "answers": ["Using technical exploits to gain unauthorized access", "Manipulating people into divulging confidential information", "Encrypting sensitive information", "Blocking malicious websites"], "correct": 1},
    {"question": "What is a common defense against DNS spoofing?", "answers": ["Using a VPN", "Using DNSSEC (DNS Security Extensions)", "Encrypting DNS queries", "Blocking outbound DNS traffic"], "correct": 1},
    {"question": "Which of the following best describes a ransomware attack?", "answers": ["A virus that corrupts system files", "Malware that encrypts files and demands payment", "A method to steal login credentials", "An attack that floods a system with traffic"], "correct": 1},
    {"question": "Which of these is a strong indicator that an email is a phishing attempt?", "answers": ["It comes from a known contact", "It asks for sensitive personal information", "It is sent at a scheduled time", "It contains no spelling or grammar mistakes"], "correct": 1},
    {"question": "Which of the following is a key function of a proxy server?", "answers": ["Encrypting network traffic", "Acting as an intermediary between users and the internet", "Blocking all incoming traffic", "Detecting malware on a network"], "correct": 1},
    {"question": "Which of the following types of malware is designed to record your keystrokes?", "answers": ["Spyware", "Ransomware", "Trojan", "Rootkit"], "correct": 0},
    {"question": "What is the main purpose of an intrusion detection system (IDS)?", "answers": ["To block unauthorized users from accessing the network", "To monitor and analyze network traffic for suspicious activity", "To encrypt sensitive data", "To provide antivirus protection"], "correct": 1},
    {"question": "What does 'data exfiltration' mean?", "answers": ["Deleting data from a system", "Encrypting data for ransom", "Illegally transferring data from a system to an external location", "Monitoring data traffic for anomalies"], "correct": 2},
    {"question": "What is the purpose of a digital certificate in public key cryptography?", "answers": ["To ensure the integrity of a public key", "To encrypt data", "To sign data with a private key", "To provide an access control list"], "correct": 0},
    {"question": "Which of the following is an example of a denial-of-service (DoS) attack?", "answers": ["An attacker intercepts communication between two parties", "An attacker floods a server with traffic to make it unavailable", "An attacker uses phishing emails to steal user credentials", "An attacker exploits a vulnerability to gain system access"], "correct": 1},
    {"question": "Which of the following is a characteristic of a secure website?", "answers": ["The URL starts with 'http'", "The URL starts with 'https'", "The website is only accessible from certain countries", "The website asks for a username and password"], "correct": 1},
    {"question": "What is the function of a data loss prevention (DLP) system?", "answers": ["To back up data regularly", "To prevent unauthorized access to sensitive data", "To encrypt all network traffic", "To monitor network speeds"], "correct": 1},
    {"question": "What does the term 'steganography' refer to in cybersecurity?", "answers": ["A method for encrypting sensitive information", "A method for hiding data within other data", "A tool for scanning files for viruses", "A technique for blocking unauthorized users"], "correct": 1},
    {"question": "What is an example of an application layer attack?", "answers": ["SQL injection", "Distributed denial of service (DDoS)", "Buffer overflow", "Malware transmission via email"], "correct": 0},
    {"question": "Which of the following is a reason why patch management is important?", "answers": ["It prevents unauthorized access to a system", "It ensures the system remains up-to-date with security fixes", "It reduces the system's memory usage", "It improves the system's processing speed"], "correct": 1}
]
hard_questions = [
    {"question": "What is the primary purpose of a buffer overflow attack?", "answers": ["To execute arbitrary code by overwriting memory", "To increase the size of a data buffer", "To monitor network traffic", "To encrypt data in memory"], "correct": 0},
    {"question": "Which of the following cryptographic algorithms is commonly used for digital signatures?", "answers": ["RSA", "DES", "MD5", "AES"], "correct": 0},
    {"question": "What is the primary security concern with SQL injection attacks?", "answers": ["Unauthorized access to a web server", "Manipulation of database queries to gain unauthorized access", "Exfiltration of files from the system", "Password cracking through brute force"], "correct": 1},
    {"question": "What is the purpose of a Distributed Denial of Service (DDoS) attack?", "answers": ["To steal sensitive information from a server", "To overwhelm a system with traffic, rendering it unavailable", "To encrypt files and demand ransom", "To exploit unpatched vulnerabilities"], "correct": 1},
    {"question": "What type of attack uses weaknesses in the SSL/TLS protocol to intercept encrypted data?", "answers": ["Man-in-the-middle (MITM)", "Cross-site scripting (XSS)", "Privilege escalation", "SQL injection"], "correct": 0},
    {"question": "Which of the following best describes a side-channel attack?", "answers": ["An attack that targets the input validation process", "An attack that uses indirect information such as timing or power consumption to extract data", "An attack that disrupts network traffic", "An attack that targets physical devices directly"], "correct": 1},
    {"question": "What is the main security risk associated with the use of weak entropy in key generation?", "answers": ["The key becomes predictable and easier to brute force", "The key is susceptible to rainbow table attacks", "The key is not stored securely", "The key has insufficient length"], "correct": 0},
    {"question": "Which cryptographic attack can be used to find the secret key from a public key?", "answers": ["Birthday attack", "Brute-force attack", "Chosen-plaintext attack", "Known-plaintext attack"], "correct": 1},
    {"question": "Which of the following is a type of attack that targets DNS servers to redirect users to malicious websites?", "answers": ["DNS cache poisoning", "Man-in-the-middle attack", "Cross-site scripting (XSS)", "Session hijacking"], "correct": 0},
    {"question": "In the context of a Public Key Infrastructure (PKI), what is the role of a certificate authority (CA)?", "answers": ["To validate the encryption key size", "To issue and manage digital certificates", "To encrypt private keys", "To store encrypted data for the client"], "correct": 1},
    {"question": "Which of the following attacks can be mitigated using HSTS (HTTP Strict Transport Security)?", "answers": ["Man-in-the-middle (MITM) attacks", "Cross-site scripting (XSS) attacks", "DNS poisoning", "Privilege escalation"], "correct": 0},
    {"question": "What is a common vulnerability in OAuth 2.0 implementations that can lead to access token leakage?", "answers": ["Improper use of state parameter", "Weak encryption of refresh tokens", "Authorization code interception", "Insufficient API rate limiting"], "correct": 2},
    {"question": "What is the main difference between AES and RSA encryption algorithms?", "answers": ["AES is asymmetric and RSA is symmetric", "AES is used for encryption, RSA is used for signatures", "AES uses symmetric keys and RSA uses asymmetric keys", "AES is slower than RSA"], "correct": 2},
    {"question": "Which of the following is a known attack vector for the WannaCry ransomware?", "answers": ["Zero-day vulnerabilities in Windows SMB protocol", "Exploitation of weak passwords", "Malicious email attachments", "Cross-site scripting (XSS)"], "correct": 0},
    {"question": "What is the primary objective of a cross-site request forgery (CSRF) attack?", "answers": ["To inject malicious code into a website", "To trick users into performing unintended actions on a website", "To steal cookies from users", "To execute SQL injection on a backend server"], "correct": 1},
    {"question": "Which of the following cryptographic methods is vulnerable to a quantum computing attack?", "answers": ["RSA", "AES", "ECC", "SHA-256"], "correct": 0},
    {"question": "What is the purpose of the 'nonce' in authentication protocols?", "answers": ["To ensure that messages are encrypted", "To prevent replay attacks by providing a unique value for each request", "To authenticate the sender's identity", "To ensure that messages are decrypted"], "correct": 1},
    {"question": "Which attack relies on manipulating the input data to modify the behavior of the software?", "answers": ["SQL injection", "Phishing", "Man-in-the-middle", "Cross-site scripting (XSS)"], "correct": 0},
    {"question": "What is the primary function of a Zero Trust security model?", "answers": ["To assume that all users and devices are trusted until proven otherwise", "To grant access based on user roles", "To block all external communication", "To continuously verify the identity and trustworthiness of users and devices"], "correct": 3},
    {"question": "What is the purpose of a hash collision attack?", "answers": ["To reverse the hash function and retrieve original data", "To find two different inputs that produce the same hash output", "To decrypt hashed passwords", "To increase the length of hash values"], "correct": 1},
    {"question": "What is the most effective defense against password spraying attacks?", "answers": ["Enabling two-factor authentication (2FA)", "Using password hashing algorithms", "Regular password changes", "Blocking IP addresses after multiple login attempts"], "correct": 0},
    {"question": "What type of malware specifically targets cloud infrastructures?", "answers": ["Cloud malware", "Ransomware", "Cryptojacking", "Fileless malware"], "correct": 2},
    {"question": "What is the role of a vulnerability scanner in cybersecurity?", "answers": ["To identify weaknesses in an application or system", "To encrypt sensitive data", "To monitor traffic for malicious activity", "To block incoming network threats"], "correct": 0},
    {"question": "What does the term 'Evil Twin' refer to in a wireless network attack?", "answers": ["A rogue access point set up to trick users into connecting to it", "A man-in-the-middle attack on wireless networks", "An exploit that targets a vulnerable router", "A brute force attack on wireless passwords"], "correct": 0},
    {"question": "Which of the following techniques can help protect against a brute force attack?", "answers": ["Implementing CAPTCHA on login pages", "Using short passwords", "Requiring frequent password changes", "Allowing unlimited login attempts"], "correct": 0},
    {"question": "What is the main vulnerability that allows Cross-Site Scripting (XSS) attacks?", "answers": ["Improper input validation", "Weak encryption algorithms", "Improper session management", "Weak server authentication"], "correct": 0},
    {"question": "What is the primary goal of a privilege escalation attack?", "answers": ["To capture sensitive data during transmission", "To gain higher-level access to a system", "To disrupt system operations", "To modify configuration files"], "correct": 1},
    {"question": "What is a significant risk associated with misconfigured cloud storage services?", "answers": ["Loss of network connectivity", "Unintentional exposure of sensitive data", "Increased power consumption", "Failure to meet regulatory compliance"], "correct": 1},
    {"question": "What type of vulnerability is targeted by a privilege escalation attack?", "answers": ["Flaw in encryption algorithms", "Weak authentication mechanisms", "Flaw in system design allowing unauthorized access", "Flaw in password storage mechanisms"], "correct": 2},
    {"question": "What is the purpose of the security header 'Content-Security-Policy' (CSP)?", "answers": ["To prevent cross-site request forgery (CSRF)", "To prevent cross-site scripting (XSS)", "To ensure secure cookie storage", "To manage HTTP connections"], "correct": 1},
    {"question": "What is the primary purpose of a Web Application Firewall (WAF)?", "answers": ["To monitor network traffic", "To detect and block malicious requests to a web application", "To encrypt web traffic", "To provide anti-virus protection"], "correct": 1}
]

def load_results(filename="previous-results.csv"):
    previous_results = []

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for line in reader:
                previous_results.append(line)
    except FileNotFoundError:
        print('\nStarting fresh...\n')

    return previous_results

def save_result(previous_results, filename="previous-results.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        result = ["Name", "Score", "Difficulty", "Date"]
        for result in previous_results:
            writer.writerow(result)

def add_result(player_name, score, difficulty, date, previous_results):
    curr_date = date
    name = player_name
    score = score
    difficulty = difficulty
    previous_results.append([name, score, difficulty, curr_date])
    print("---------------------------------------------")
    print(f"\nYou scored {score}!\nName: {name}\nScore: {score}\nDifficulty: {difficulty}\nDate: {curr_date}\n")
    print("---------------------------------------------")
    
def welcome():
    print("\n-----Welcome-------------------------------")
    print("-----------------To------------------------")
    print("-----------------------T-QuIzZiL-----------\n")

def quiz(player_name, score, questions_selection, difficulty, previous_results):

    in_game = True
    score = 0
    questions = questions_selection
    curr_date = time.strftime("%a,%H:%M:%S")

    while in_game:

        for ind, question in enumerate(questions):
            print(f"\n{ind + 1}) {question['question']}\n")
            for index, answer in enumerate(question['answers']):
                print(f"\t{index + 1}) {answer}")
            while True:
                try:
                    guess = int(input("\nEnter guess: ")) - 1
                    if 0 <= guess < len(question["answers"]):
                        break
                    else:
                        print("Invalid entry!!")
                except ValueError:
                    print("Invalid input!")

            if guess == question['correct']:
                score += 100

        save_result(previous_results)
        add_result(player_name, score, difficulty, curr_date, previous_results)
        in_game = False

def main():
    previous_results = load_results()
    score = 0
    player_name = input("Enter name: ")
    print("\nWelcome to T-Quizzil, a quiz on cybersecurity!")
    while True:
        try:
            print("\nPlease enter difficulty:\n\n1) Easy\n2) Medium \n3) Hard\n4) Exit")
            
            while True:
                try:
                    choice = int(input("\nEnter: "))
                    if choice > 0 and choice <= 4:
                        break
                    else:
                        print("Invalid input")
                except ValueError:
                    print("Invalid input")

            if choice == 1:
                difficulty="Easy"
                score = quiz(player_name, score, easy_questions, difficulty, previous_results)
            elif choice == 2:
                difficulty="Medium"
                score = quiz(player_name, score, medium_questions, difficulty, previous_results)
            elif choice == 3:
                difficulty="Hard"
                score = quiz(player_name, score, hard_questions, difficulty, previous_results)
            elif choice == 4:
                print(f"\n....goodbye, {player_name}!\n")
                break
        except ValueError:
            print("Invalid choice")
            continue 



if __name__ == "__main__":
    welcome()
    main()
