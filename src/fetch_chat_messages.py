import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

# Leggi il token di accesso dal file
with open("access_token.txt", "r") as token_file:
    access_token = token_file.read().strip()

# Leggi l'ID della chat dal file
with open("chat_id.txt", "r") as chat_id_file:
    chat_id = chat_id_file.read().strip()

def get_chat_messages(access_token, chat_id):
    url = f'https://graph.microsoft.com/v1.0/chats/{chat_id}/messages'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    all_messages = []
    retries = 3  # Numero di tentativi di retry

    while url:
        for attempt in range(retries):
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                messages = data.get('value', [])
                all_messages.extend(messages)
                url = data.get('@odata.nextLink')  # Recupera il link per la pagina successiva
                break  # Esce dal ciclo di retry se la richiesta è andata a buon fine
            else:
                print(f"Errore: {response.status_code}, {response.text}")
                time.sleep(2 ** attempt)  # Aumenta il tempo di attesa tra i retry
                if attempt == retries - 1:  # Dopo l'ultimo tentativo, interrompe il ciclo
                    return all_messages

    return all_messages

# Ottieni i messaggi della chat
print("Scaricamento messaggi in corso...")
messages = get_chat_messages(access_token, chat_id)

# Salva i messaggi in un file di testo
with open('chat_messages.txt', 'w', encoding='utf-8') as f:
    for message in messages:
        sender = message.get('from', {}).get('user', {}).get('displayName', 'Unknown')
        raw_content = message.get('body', {}).get('content', 'No content')
        # Usa BeautifulSoup per rimuovere i tag HTML
        soup = BeautifulSoup(raw_content, "html.parser")
        content = soup.get_text()
        # Aggiungi data e ora al messaggio
        timestamp = message.get('createdDateTime', 'Unknown time')
        f.write(f"Sender: {sender}\nTime: {timestamp}\nMessage: {content}\n\n")

print("I messaggi sono stati salvati in 'chat_messages.txt'")
