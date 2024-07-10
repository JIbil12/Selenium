from win10toast import ToastNotifier
import time

toaster=ToastNotifier()

titile=input("\nEnter the title of notification :")
msg=input("\nEnter the msg of notification :")
min=float(input("\nHow many minutes :"))
seconds=min*60

print("\nRemainder set successfully")
time.sleep(seconds)
toaster.show_toast(titile,msg,duration=10,threaded=True)

while toaster.notification_active():
    time.sleep(0.1)

