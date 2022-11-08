from abc import ABC, abstractmethod


"""Sort of acts as DTO (Data transfer object) for our notification"""
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


"""Parent class from which Email and SMS notification subclasses"""
class Notification(ABC):

    @abstractmethod
    def notify(self, message, email) -> int:
        pass


"""Subclassed from Notification class"""
class Email(Notification):

    def notify(self, message, email):
        print(f"Sent {message} to {email}")
        

"""Subclassed from Notification class"""
class SMS(Notification):
    def notify(self, message, phone):
        print(f"Sent {message} to {phone}")


"""
Manager class utillizing the subclasses of Notification object.

To vidate the Liskov substitution principle,
this class should act same for the objects of the classes
that subclass the Notificaton class
"""
class NotificationManager:
    def __init__(self, notification, contact):
        self.contact = contact
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, self.contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, self.contact.phone)
        else:
            raise Exception('The notification is not supported')

"""
What's the issue with this implementation.
-> Main issue is, if we have other notification service, the send method needs to be modified (reactive)
   for other objects of classes subclassing from Notification class. This violates the open close principle as well
   as liskov substitutoin principle.

   i.e. following portion of code needs to be added to send method of NotificationManager class.
        elif isinstance(self.notification, <SUBCLASS_OF_NOTIFICATION>):
            self.notification.notify(message, self.contact.<CONTACT_OPTION>)
"""

if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')
    sms = SMS()
    email = Email()
    notification_manager = NotificationManager(sms, contact)

    # Though this is possible it also voilates open closed principle.
    notification_manager.notification = email
    notification_manager.send('Hello John')
