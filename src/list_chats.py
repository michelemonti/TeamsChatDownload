import requests

# Sostituisci con il tuo token di accesso
access_token = "xxx"

def get_chat_list(access_token):
    url = 'https://graph.microsoft.com/v1.0/me/chats'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('value', [])
    else:
        print(f"Errore: {response.status_code}, {response.text}")
        return []

# Usa il tuo access token
# Ottieni la lista delle chat
chat_list = get_chat_list(access_token)

# Visualizza le chat e i relativi ID
for chat in chat_list:
    print(f"Chat ID: {chat['id']}, Chat Name: {chat.get('topic', 'No Topic')}")
