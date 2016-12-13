import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
# imaplib module implements connection based on IMAPv4 protocol
print(mail.login('imlegendlzz@gmail.com', 'woaihuanhuan226'))
# print(mail.list())    # Lists all labels in GMail
mail.select('inbox') # Connected to inbox.
# result, data = mail.uid('search', None, "All")
# search and return uids instead
result, data = mail.search(None, '(FROM "513278236@qq.com")')

i = len(data[0].split()) # data[0] is a space separate string
count = 0
for x in range(i):
    latest_email_uid = data[0].split()[x] # unique ids wrt label selected
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
   # fetch the email body (RFC822) for the given ID
    raw_email = email_data[0][1]
    count = count + 1
    print(count)
    if count == 2:
    	break

#continue inside the same for loop as above
raw_email_string = raw_email.decode('utf-8', errors='ignore')
# converts byte literal to string removing b''
email_message = email.message_from_string(raw_email_string)
# this will loop through all the available multiparts in mail
for part in email_message.walk():
    if part.get_content_type() == "text/plain": # ignore attachments/html
        body = part.get_payload(decode=True)
        save_string = str("D:Dumpgmailemail_" + str(x) + ".txt")
# location on disk
        myfile = open(save_string, 'a')
# myfile.write(body.decode('utf-8', errors='ignore'))
        myfile.write(body.decode('gbk', errors='ignore'))
# body is again a byte literal
        myfile.close()
    else:
        continue
