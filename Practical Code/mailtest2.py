import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
print(mail.login('imlegendlzz@gmail.com', 'woaihuanhuan226'))
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

# result, data = mail.search(None, '(FROM "513278236@qq.com")' )
result, data = mail.search(None, '(FROM "noreply@youtube.com")')
# result, data = mail.search(None, '(UNSEEN)') # if you walk through this once the mail will all be read. 
# print(data) # Print the uid of the mail
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
# latest_email_id = id_list[-1] # get the latest

count = 0
print(len(id_list))
for email_id in id_list:
    count = count + 1
    result, data = mail.fetch(email_id, "(RFC822)") # fetch the email body (RFC822)             for the given ID

    raw_email = data[0][1] # here's the body, which is raw text of the whole email

#continue inside the same for loop as above
    raw_email_string = raw_email.decode('utf-8', errors='ignore')
# converts byte literal to string removing b''
    email_message = email.message_from_string(raw_email_string)
# this will loop through all the available multiparts in mail
    for part in email_message.walk():
        if part.get_content_type() == "text/plain": # ignore attachments/html
            body = part.get_payload(decode=True)
            save_string = str("D:Dumpgmailemail_" + str(count) + ".txt")
# location on disk
            myfile = open(save_string, 'a')
            # myfile.write(body.decode('utf-8', errors='ignore'))
            myfile.write(body.decode('gbk', errors='ignore'))
# body is again a byte literal
            myfile.close()
        else:
            continue
