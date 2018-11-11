import smtplib                                      # Импортируем библиотеку по работе с SMTP

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_message(filepath):
    addr_from = "Aerodynamicss@yandex.ru"
    addr_to = "semien9797@gmail.com"
    password = "27011997AAA"

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = 'Расчет'

    body = "Текст сообщения"
    msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

    fp = open('aero_calculation/tmpfiles/'+filepath, 'rb')
    xls = MIMEBase('application', 'vnd.ms-excel')
    xls.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(xls)
    xls.add_header('Content-Disposition', 'attachment', filename='result')
    msg.attach(xls)

    server = smtplib.SMTP_SSL('smtp.yandex.ru')
    server.set_debuglevel(True)
    server.login(addr_from, password)
    server.send_message(msg)

    server.quit()
