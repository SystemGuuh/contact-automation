import pandas as pd
import pyautogui

def getData(file_path):
    try:
        df = pd.read_excel(file_path)
        return df

    except FileNotFoundError:
        pyautogui.alert(f'Erro: O arquivo {file_path} não foi encontrado.')
    except pd.errors.EmptyDataError:
        pyautogui.alert('Erro: O arquivo XLSX está vazio.')
    except pd.errors.ParserError:
        pyautogui.alert('Erro ao analisar o arquivo XLSX.')
    except Exception as e:
        pyautogui.alert(f'Ocorreu um erro inesperado: {e}')

def checkColumns(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    return missing_columns
