import smtplib
from loginy_poczta import login, haslo

# dane niezbedne do wyslania maila
odbiorca = login
nadawca = login
haslo = haslo
temat = 'Subject: Hello znowu z Pythona Arek'
tresc = 'To jest wiadomosc bez polskich znakow'
wiadomosc = temat + tresc

mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()
mailer.starttls()
mailer.login(login, haslo)
mailer.sendmail(nadawca, odbiorca, wiadomosc)

print('Wyslano maila')
mailer.close()
