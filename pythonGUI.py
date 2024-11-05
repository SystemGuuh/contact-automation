import pyautogui
from assets.email_functions import *
from assets.data_functions import *
from assets.trello_functions import *


pyautogui.alert("O robo vai comecar a mandar emails com os dados do arquivo ./data.xlsx")
pyautogui.PAUSE = 0.5

data = getData('./src/data/data.xlsx')

if data is not None:
    required_columns = ['Nome', 'Email', 'Data1', 'Data2', 'Tipo']
    if missing_columns := checkColumns(data, required_columns):
        pyautogui.alert(f"Opa, parece que está faltando a coluna {missing_columns}.")
        exit()

goToOutlook()
for index, row in data.iterrows():
    if index <= 80:
        sendEmail(row)
    else: break

goToTrello()
for index, row in data.iterrows():
    if index <= 80:
        name = str(row['Nome'])
        if index == 0: createFirstCard(name)
        else: createNextCard(name)
    else: break
        
