import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

class Poczta(object):

    def __init__(self, login, haslo, server='smtp.gmail.com'):
        self.login = login
        self.haslo = haslo
        self.server = server

    def wyslij_wiadomosc(self, adresaci, temat,
                         tresc, pliki=None):
        print('Wyslij wiadomosc')
        assert isinstance(adresaci, list)

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = COMMASPACE.join(adresaci)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = temat
        print('Wyslij wiadomosc 2')
        tresc = MIMEText(tresc, _charset='utf-8')
        msg.attach(tresc)

        for plik in pliki or []:
            print('for')
            with open(plik, 'rb') as zalacznik:
                part = MIMEApplication(
                    zalacznik.read(),
                    Name=basename(plik)
                )
                print('part')
                part['Content-Disposition'] = \
                    f'attachment; filename="{basename(plik)}"'
                print(part)
                msg.attach(part)
        print('po for')
        mailer = smtplib.SMTP(self.server, 587)
        print('po mailer')
        mailer.ehlo()
        print('po ehlo')
        mailer.starttls()
        print('po starttls')
        mailer.login(self.login, self.haslo)
        print('po login')
        mailer.sendmail(self.login, adresaci, msg.as_string())
        print('po sendmail')
        mailer.close()
        print('po close')
def main():
    import secrets as secret

    spamer = Poczta(secret.login, secret.haslo)
    print(spamer)
    adresat = secret.login
    odbiorcy = [adresat]
    pliki = [r'C:\Users\mlys\Desktop\My_stuff\PYTHON_KURS\hi.png']
    temat = 'Hey ho lets go'
    tresc = 'Sesesesese'

    spamer.wyslij_wiadomosc(odbiorcy, temat, tresc, pliki)

if __name__ == '__main__':
    main()