import smtplib
from email.mime.text import MIMEText
from loginy_poczta import login, haslo

# dane nizbedne do wyslania maila
odbiorca = login
nadawca = login
haslo = haslo
temat = 'Hello znowu z Pythona Arek'
tresc = 'To jest wiadomość z polskimi znakami óóóóó'

# # wiadomosc w formacie MIME, okreslam kodowanie na utf8
# # dzieki temu moge wysylac polskie znaki
wiadomosc = MIMEText(tresc, _charset='utf-8')
wiadomosc['Subject'] = temat
wiadomosc['From'] = nadawca
wiadomosc['To'] = odbiorca

# nawiazuje polaczenie z serwerem, autoryzacja i wysylam maila
mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()
mailer.starttls()
mailer.login(login, haslo)
mailer.sendmail(nadawca, odbiorca, wiadomosc.as_string())

print('Wyslano maila')
mailer.close()
