import tkinter as tk
from tkinter import simpledialog
import pyperclip
import pyautogui
import time

def getInitialSubject(clientName, bdc):
    return f'Olá, {clientName}, sou {bdc}, especialista em soluções técnicas, uma dúvida...'

def getExpiredSubject(clientName, bdc):
    return f'Olá, {clientName}, agradecemos sua parceiria com a Oracle, gostaria de conversar?'

def getFinalSubject(clientName, bdc):
    return f'Olá, {clientName}, sou {bdc}, especialista em soluções técnicas, uma dúvida...'

def getDefaultSubject(clientName, bdc):
    return f'Olá, {clientName}, sou {bdc}, especialista em soluções técnicas, uma dúvida...'

def getInitialBody(clientName,  rowDate, secondDate, bdc):
    return f'''Fala {clientName}, tudo bem?

Meu nome é {bdc}, faço parte da equipe que dá apoio aos ambientes de teste na Oracle Cloud. 
Gostaria de compartilhar cases de empresas que reduziram seus custos operacionais em 30% ao migrar para a OCI.

O período de 30 dias é curto, por isso, gostaria de te ajudar na implementação. 
Estou à disposição para conversar sobre como vamos maximizar sua experiência. 
Podemos agendar um horário no Zoom em um dos seguintes horários:
{rowDate} ou {secondDate} o que acha melhor?

Aguardo seu retorno, {clientName}.
Abraço,
''' + getFooter(bdc)

def getExpiredBody(clientName, bdc):
    return f'''Fala {clientName}, tudo bem?

Meu nome é {bdc}, e sou especialista em soluções técnicas.
Notei que sua conta expirou recentemente e gostaria de expressar que sinto muito por vocês não terem continuado conosco.
Valorizamos muito a sua parceria e estamos sempre em busca de melhorias.

Para que possamos entender melhor sua experiência e identificar oportunidades de aprimoramento, gostaria de pedir um feedback sobre o que motivou a sua decisão. 
Suas opiniões são fundamentais para nós.

Caso tenha interesse em retomar a conversa ou discutir como podemos atender melhor suas necessidades no futuro, estou à disposição!

Aguardo seu retorno, {clientName}.

Abraço,
''' + getFooter(bdc)

def getFinalBody(clientName,  rowDate, secondDate, bdc):
    return f'''Fala {clientName}, tudo bem?

Meu nome é {bdc}, faço parte da equipe que dá apoio aos ambientes de teste na Oracle Cloud. 
Gostaria de compartilhar cases de empresas que reduziram seus custos operacionais em 30% ao migrar para a OCI.

O período de 30 dias é curto, por isso, gostaria de te ajudar na implementação. 
Estou à disposição para conversar sobre como vamos maximizar sua experiência. 
Podemos agendar um horário no Zoom em um dos seguintes horários:
{rowDate} ou {secondDate} o que acha melhor?

Aguardo seu retorno, {clientName}.
Abraço,
''' + getFooter(bdc)

def getDefaultBody(clientName,  rowDate, secondDate, bdc):
    return f'''
Fala {clientName}, tudo bem?

Meu nome é {bdc}, faço parte da equipe que dá apoio aos ambientes de teste na Oracle Cloud. 
Gostaria de compartilhar cases de empresas que reduziram seus custos operacionais em 30% ao migrar para a OCI.

O período de 30 dias é curto, por isso, gostaria de te ajudar na implementação. 
Estou à disposição para conversar sobre como vamos maximizar sua experiência. 
Podemos agendar um horário no Zoom em um dos seguintes horários:
{rowDate} ou {secondDate} o que acha melhor?

Aguardo seu retorno, {clientName}.
Abraço,
''' + getFooter(bdc)

def getFooter(bdc):
    if bdc == "Gustavo Almeida":
       return '''

Atenciosamente | Saludos | Regards,
Gustavo Almeida (he/el/ele)
Oracle | Cloud Solution Engineer
Mobile: +55 11 96783-3245 | gustavo.de.jesus@oracle.com
Rua Dr. José Áureo Bustamante, 455 | 04710-090 - São Paulo, SP - Brasil'''
    
    elif bdc == "Lidiane Faria":
        return '''

Atenciosamente | Saludos | Regards,
Lidiane Faria (she/ella/ela)
Oracle | Cloud Solution Engineer 
Mobile: +55 (11) 96391-4399 | lidiane.faria@oracle.com
Rua Dr. José Áureo Bustamante, 455 | 04710-090 - São Paulo, SP - Brasil'''
    
    elif bdc == "Melissa Cruz":
        return '''

Atenciosamente | Saludos | Regards,
Melissa Cruz (she/ella/ela)
Oracle | Cloud Solution Engineer 
Mobile: +55 11 99723-8621 | melissa.c.cruz@oracle.com
Rua Dr. José Áureo Bustamante, 455 | 04710-090 - São Paulo, SP - Brasil'''
    else: return ' '

def getSubject(row, subject_option, bdc):
    if subject_option == "Primeiro Contato":
        return getInitialSubject(row['Nome'], bdc)
    elif subject_option == "Segundo Contato":
        return getDefaultSubject(row['Nome'], bdc)
    elif subject_option == "Contato Final":
        return getFinalSubject(row['Nome'], bdc)
    elif subject_option == "Expirado":
        return getExpiredSubject(row['Nome'], bdc)

def getBody(row, body_option, bdc):
    if body_option == "Primeiro Contato":
        return getInitialBody(row['Nome'],row['Data1'],row['Data2'], bdc)
    elif body_option == "Segundo Contato":
        return getInitialBody(row['Nome'],row['Data1'],row['Data2'], bdc)
    elif body_option == "Contato Final":
        return getInitialBody(row['Nome'],row['Data1'],row['Data2'], bdc)
    elif body_option == "Expirado":
        return getExpiredBody(row['Nome'], bdc)

def sendEmail(row, subject, body):
        Email = str(row['Email'])

        pyautogui.press('n')
        time.sleep(1)

        pyperclip.copy(Email)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyperclip.copy(subject)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('tab')
        pyperclip.copy(body)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('ctrl', 'enter')
     
def goToOutlook():
    pyautogui.alert("O robo vai comecar a mandar emails. Aproveite para tomar um café e não mexa no pc.")
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://outlook.office.com/mail/')
    pyautogui.press('enter')
    time.sleep(3)
