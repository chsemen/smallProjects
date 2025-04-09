import ezgmail

# ezgmail.send('ch-semen@rambler.ru', 'Subject line', 'Body of the email')
# ezgmail.send('ch-semen@rambler.ru', 'Subject line', 'Body of the email', ['allminutes.pdf'])
ezgmail.send('ch-semen@rambler.ru', 'Subject line', 'Body of the email', 
             cc='chsemen2014@gmail.com', bcc='ch_semen@mail.ru')
print(f'ezgmail.EMAIL_ADDRESS {ezgmail.EMAIL_ADDRESS}')