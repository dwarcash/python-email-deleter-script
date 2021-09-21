import imaplib
import email
from email.header import decode_header

# account credentials
username = ""
password = ""


# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

# select the mailbox You want to delete in
# if you want SPAM, use imap.select("SPAM") instead
imap.select("INBOX")

# search for specific mails by sender
# status, messages = imap.search(None, 'FROM "googlealerts-noreply@google.com"')

# to get mails by subject
# status, messages = imap.search(None, 'SUBJECT "Thanks for Subscribing to our Newsletter !"')

# to get mails after a specific date
# status, messages = imap.search(None, 'SINCE "01-JAN-2020"')

# to get mails before a specific date
status, messages_id_list = imap.search(None, 'BEFORE "01-JAN-2017"')

# to get all mails
# status, messages = imap.search(None, "ALL")

# convert messages to a list of email IDs
messages = messages_id_list[0].split(b' ')

print("Deleting mails")
count =1
for mail in messages:
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")

    print(count, "mail(s) deleted")
    count +=1
print("All selected mails has been deleted")

# delete all the selected messages 
imap.expunge()
# close the mailbox
imap.close()

# logout form the server
imap.logout()