from abc import ABC, abstractmethod

class Contact:

    def __init__(self, name, email, phone) -> None:
        self.name = name
        self.email= email
        self.phone = phone


class Notificaion:

    @abstractmethod
    def notify(self, message):
        pass


class Email(Notificaion):

    def __init__(self,email) -> None:
        self.email = email
    
    def notify(self, message):
        print(f"Sent {message} to {self.email}")


class SMS(Notificaion):

    def __init__(self, phone) -> None:
        self.phone = phone
    
    def notify(self, message):
        print(f"Sent {message} to {self.phone}")


class NotificationManager:
    """It can be a facade containing multiple functionality"""

    def __init__(self, notification) -> None:
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)
    
if __name__ == "__main__":
    contact = Contact("Ram kuwar", "ram@gmail.com", "984523135")

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send("sms")

    # now pointing to different subclass of same parent
    notification_manager.notification = email_notification
    notification_manager.send("email")
