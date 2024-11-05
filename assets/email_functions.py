import tkinter as tk
from tkinter import simpledialog
import pyperclip
import pyautogui
import time

def getInitialSubject(clientName):
    return f'Olá, {clientName}, sou Gustavo, especialista em soluções técnicas, uma dúvida...'

def getExpiredSubject(clientName):
    return f'Olá, {clientName}, agradecemos sua parceiria com a Oracle, gostaria de conversar?'

def getFinalSubject(clientName):
    return f'Olá, {clientName}, sou Gustavo, especialista em soluções técnicas, uma dúvida...'

def getDefaultSubject(clientName):
    return f'Olá, {clientName}, sou Gustavo, especialista em soluções técnicas, uma dúvida...'

def getInitialBody(clientName,  firstDate, secondDate):
    return f'''Fala {clientName}, tudo bem?

Meu nome é Gustavo Almeida, faço parte da equipe que dá apoio aos ambientes de teste na Oracle Cloud. 
Gostaria de compartilhar cases' 'de empresas que reduziram seus custos operacionais em 30% ao migrar para a OCI.

O período de 30 dias é curto, por isso, gostaria de te ajudar na implementação. 
Estou à disposição para conversar sobre como vamos maximizar sua experiência. 
Podemos agendar um horário no Zoom em um dos seguintes horários:
{firstDate} ou {secondDate} o que acha melhor?

Aguardo seu retorno, {clientName}.
Abraço,

Atenciosamente | Saludos | Regards,
Gustavo Almeida (he/el/ele)
Oracle | Cloud Solution Engineer
Mobile: +55 11 96783-3245 | gustavo.de.jesus@oracle.com
Rua Dr. José Áureo Bustamante, 455 | 04710-090 - São Paulo, SP - Brasil'''

def getExpiredBody(clientName):
    return f'''Fala {clientName}, tudo bem?

Meu nome é Gustavo Almeida, e sou especialista em soluções técnicas.
Notei que sua conta expirou recentemente e gostaria de expressar que sinto muito por vocês não terem continuado conosco.
Valorizamos muito a sua parceria e estamos sempre em busca de melhorias.

Para que possamos entender melhor sua experiência e identificar oportunidades de aprimoramento, gostaria de pedir um feedback sobre o que motivou a sua decisão. 
Suas opiniões são fundamentais para nós.

Caso tenha interesse em retomar a conversa ou discutir como podemos atender melhor suas necessidades no futuro, estou à disposição!

Aguardo seu retorno, {clientName}.

Abraço,

Atenciosamente | Saludos | Regards,
Gustavo Almeida (he/el/ele)
Oracle | Cloud Solution Engineer
Mobile: +55 11 96783-3245 | gustavo.de.jesus@oracle.com
Rua Dr. José Áureo Bustamante, 455 | 04710-090 - São Paulo, SP - Brasil'''

def getFinalBody(clientName,  firstDate, secondDate):
    return f'''Fala {clientName}, tudo bem?

Meu nome é Gustavo Almeida, faço parte da equipe que dá apoio aos ambientes de teste na Oracle Cloud. 
Gostaria de compartilhar cases' 'de empresas que reduziram seus custos operacionais em 30% ao migrar para a OCI.

O período de 30 dias é curto, por isso, gostaria de te ajudar na implementação. 
Estou à disposição para conversar sobre como vamos maximizar sua experiência. 
Podemos agendar um horário no Zoom em um dos seguintes horários:
{firstDate} ou {secondDate} o que acha melhor?

Aguardo seu retorno, {clientName}.
Abraço,

Atenciosamente | Saludos | Regards,
Gustavo Almeida (he/el/ele)
Oracle | Cloud Solution Engineer
Mobile: +55 11 96783-3245 | gustavo.de.jesus@oracle.com
Rua Dr. José Áureo Bustamante, 455 | 04710-090 - São Paulo, SP - Brasil'''

def getDefaultBody(clientName,  firstDate, secondDate):
    return f'''Fala {clientName}, tudo bem?

Meu nome é Gustavo Almeida, faço parte da equipe que dá apoio aos ambientes de teste na Oracle Cloud. 
Gostaria de compartilhar cases' 'de empresas que reduziram seus custos operacionais em 30% ao migrar para a OCI.

O período de 30 dias é curto, por isso, gostaria de te ajudar na implementação. 
Estou à disposição para conversar sobre como vamos maximizar sua experiência. 
Podemos agendar um horário no Zoom em um dos seguintes horários:
{firstDate} ou {secondDate} o que acha melhor?

Aguardo seu retorno, {clientName}.
Abraço,

Atenciosamente | Saludos | Regards,
Gustavo Almeida (he/el/ele)
Oracle | Cloud Solution Engineer
Mobile: +55 11 96783-3245 | gustavo.de.jesus@oracle.com
Rua Dr. José Áureo Bustamante, 455 | 04710-090 - São Paulo, SP - Brasil'''

def sendEmail(row):
    
        firstName = row['Nome'].split()[0]
        if str(row['Tipo'])=='1':
            subject = getInitialSubject(firstName)
            msg_body = getInitialBody(row['Nome'], row['Data1'], row['Data2'])
        elif str(row['Tipo'])=='2':
            subject = getDefaultSubject(firstName)
            msg_body = getDefaultBody(row['Nome'], row['Data1'], row['Data2'])
        elif str(row['Tipo'])=='3':
            subject = getFinalSubject(firstName)
            msg_body = getFinalBody(row['Nome'], row['Data1'], row['Data2'])
        elif str(row['Tipo'])=='4':
            subject = getExpiredSubject(row['Nome'])
            msg_body = getExpiredBody(row['Nome'])
        else:
            return
        
        email = str(row['Email'])

        pyautogui.press('n')
        time.sleep(1)

        pyperclip.copy(email)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.press('enter')

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyperclip.copy(subject)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('tab')
        pyperclip.copy(msg_body)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('ctrl', 'enter')
     

def goToOutlook():
    pyautogui.press('winleft')
    pyautogui.write('edge')
    pyautogui.press('enter')
    pyautogui.write('https://outlook.office.com/mail/')
    pyautogui.press('enter')
    time.sleep(2)

