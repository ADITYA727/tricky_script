# import library 
import math, random
# importing twilio 
from twilio.rest import Client

# function to generate OTP 
def generateOTP():
        num = '+91'
        num = num + input("enter number ..")
        string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        OTP = "Wellcome to freebazar.com, and your otp is "
        length = len(string)
        for i in range(6):
                OTP += string[math.floor(random.random() * length)]
        OTP = OTP + " Thank you for connecting us..\n hope all is well"                
        account_sid = 'ACab7dd9e6fb0cadfaf3286e5ceec09aec'
        auth_token = 'f033559efa1a93f0177a3113edabc6eb'
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=OTP,from_='+12568264574',to=num)
        print(message.sid)
        return OTP


# Driver code 
if __name__ == "__main__" :
        print("OTP of length 6:", generateOTP())



 


 

 

	
