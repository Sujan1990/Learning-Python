import qrcode

#This is a python code to generate qr code that redirects user to thier email application automatically 
# and autofills the subject and body of the email. 

email_address = "sujankhadka1990@gmail.com"
subject = "My First Email Using Python"
body = "Hello, this is my first email using Python. \n\nBest Regards, \nSujan Khadka"

mail = f"mailto:{email_address}?subject={subject}&body={body}"

img = qrcode.make(mail)
type(img)
img.save("Emailqr.png")

print("Your auto email qr has been saved as Emailqr.png")