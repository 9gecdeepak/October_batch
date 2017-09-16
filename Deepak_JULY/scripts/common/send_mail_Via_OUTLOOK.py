import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'Deepakkumar.Behera@ABC.com'
#mail.CC = "moreaddresses here"
#mail.BCC = "address"
mail.Subject = 'Message subject'
mail.Body = 'Message body'
mail.HTMLBody = '<h2>HTML Message body</h2>'# this field is optional

#In case you want to attach a file to the email
attachment1  = "D:\\DESKTOP_STICKY.txt"
mail.Attachments.Add(attachment1)

mail.Send()
