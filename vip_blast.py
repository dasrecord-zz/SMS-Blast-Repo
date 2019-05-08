import requests
import sys
from vip import vip as VIP
event = #TYPE EVENT NAME HERE
key = #PLACE KEY HERE
url = 'https://maker.ifttt.com/trigger/{' + event + '}/with/key/' + key
while True:
    print('***'*10)
    message_text = input('Enter message text:   ')
    population = str(len(VIP))
    warning = 'Send "%s" to %s people in VIP...' % (message_text, population)
    print(warning)
    confirmation = str(input('''Are You Sure?
    Enter 1 for Yes
    Enter 0 for No
    Enter x  to Exit:   '''))
    if confirmation == '1':
        for name in VIP:
            phone_number = VIP[name]
            params = {'value1': phone_number, 'value2': message_text}
            # SEND REQUEST TO IFTTT WEBHOOK
            requests.get(url, params)
            # print(name,phone_number)
        print("Message Sent Successfully!")
        break
    elif confirmation == '0':
        print("Message Not Sent.")
    else:
        break
print('***'*10)
sys.exit()
