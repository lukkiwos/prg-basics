import re

email_file = "email.txt"

def email_sender():
    with open(email_file, 'r', encoding="utf-8") as file:
        content = file.read()

        match = re.search(r'^From:.*<([^>]+)>', content, re.MULTILINE)
        return match.group(1)


def email_recipient():
    with open(email_file, 'r', encoding="utf-8") as file:
        content = file.read()

    match = re.search(r'^To:.*<([^>]+)>', content, re.MULTILINE)
    return match.group(1)


def email_subject():
    with open(email_file, 'r', encoding="utf-8") as file:
        content = file.read()

    match = re.search(r'^Subject:\s*(.*)', content, re.MULTILINE)
    return match.group(1)


def email_body():
    with open(email_file, 'r', encoding="utf-8") as file:
        content = file.read()

    match = re.search(r'\n\n(.*)', content, re.DOTALL)
    return match.group(1).strip()



if __name__ == "__main__":
    print(f"Sender: {email_sender()}")
    print(f"Recipient: {email_recipient()}")
    print(f"Subject: {email_recipient()}")
    print(f"Body: {email_body()}")