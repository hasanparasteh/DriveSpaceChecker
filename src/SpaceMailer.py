import smtplib
import sys

import psutil
from win10toast import ToastNotifier


class DriveSpaceChecker:
    def __init__(self):
        self.toaster = ToastNotifier()

    def low_space(self, amount):
        for drive in self.get_all_drives_letter():
            if psutil.disk_usage(drive).free <= amount:
                self.toaster.show_toast(f"Drive {drive} is running low on space!")
                return False
        return True

    @staticmethod
    def get_all_drives_letter():
        partitions = psutil.disk_partitions()
        drives = [dp.device for dp in partitions if dp.fstype == 'NTFS']
        return drives


class SendMail:
    def __init__(self, usr_email, usr_password):
        self.email = usr_email
        self.password = usr_password

        self.drive = DriveSpaceChecker()

        self.subject = "Critical Error: Server Space Is Running Out!"
        self.message = "We don't have any time please check \'Seal Gostar Salaran\' server for space issue.\n We are " \
                       "having some " \
                       "problem with saving data! "

        self.list = ['mehdialfa2012@gmail.com', 'hasanparasteh@gmail.com', 'parasteh@hotmail.com']

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()

    def email_sender(self):
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.email, self.password)

        for item in self.list:
            mail_content = '\r\n'.join([
                'To: %s' % item,
                'From: %s' % self.email,
                'Subject: %s' % self.subject,
                '',
                self.message
            ])
            self.server.sendmail(self.email, item, mail_content)

    def drive_space_checker(self):
        if not self.drive.low_space(15000000000):
            self.email_sender()
            print("Email sent!")

        print("Everything is ok!")


if __name__ == "__main__":
    password = sys.argv[1]
    email = sys.argv[2]

    mail = SendMail(email, password)
    mail.drive_space_checker()
