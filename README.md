# SMS-Blast-Repo
A script that leverages an IFTTT webhook receiver to automate Android SMS.

Step 1.
Configure your (free) IFTTT account at https://ifttt.com/
Once registered, click your account and select New Applet.

Step 2.
Create an applet that uses the Webhooks Receiver module as the THIS trigger.
Select Receive a Web request.

Step 3.
Choose a single string "event_name" and enter it here.
This will be used to correctly aim the web request from vip_blast.py

Step 4.
Select Android SMS as the THAT action and press connect"

Step 5.
The Phone number should receie {{value1}}
NOTE: you may need to add "+" or "1" to the phone number depending on your geolocation.

Step 6.
The Message should receieve {{value2}}

Optional Step: Feel free to format around {{value2}} for further SMS customization.

Step 7.
Configure your vip.py file with names and numbers.

Step 8.
Open vip_blast.py and ensure your "event_name" and "key"
Your "key" information is located in Webhook Receiver Documentaiton on IFTTT.
https://ifttt.com/maker_webhooks

Step 9.
Run vip_blast.py and enjoy.





