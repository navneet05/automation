import win32com.client as win32
from datetime import date
excel = win32.gencache.EnsureDispatch('Excel.Application')

to_email = """
Lincoln, Abraham <honest_abe@example.com>; chris@example.com
"""
# Open up an outlook email
outlook = win32.gencache.EnsureDispatch('Outlook.Application')
new_mail = outlook.CreateItem(0)

# Label the subject
new_mail.Subject = "{:%m/%d} Update".format(date.today())
new_mail.Body="hi,\n test 01 "

# Add the to and cc list
new_mail.To = to_email
#new_mail.CC = cc_email
# Display the email
new_mail.Display(True)