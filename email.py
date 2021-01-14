"""Module that does regex on emails"""


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

def find_uniq_emails(n):
    valid_emails = []
    for i in range(len(n)):
        splitted_email = n[i].split("@")
        domain = splitted_email[-1]
        address = splitted_email[0].replace(".", "").split("+")[0]
        valid_address = address + "@" + domain
        if valid_address not in valid_emails:
            valid_emails.append(valid_address)

    print(valid_emails)
    return len(valid_emails)

    # print(valid_emails)
if __name__ == "__main__":
    find_uniq_emails(emails)
