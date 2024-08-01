from msal import ConfidentialClientApplication
from flask import Flask, request, redirect
import os

app = Flask(__name__)

# Configurazioni dell'applicazione
client_id = 'xxx'  # Application ID
client_secret = 'xxx'  # Client Secret
tenant_id = 'xxx'  # Directory ID
redirect_uri = 'http://localhost:5500/get_token'  # Redirect URI
authority = f"https://login.microsoftonline.com/{tenant_id}"
scopes = ["https://graph.microsoft.com/.default"]

client_app = ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

@app.route('/')
def home():
    auth_url = client_app.get_authorization_request_url(scopes, redirect_uri=redirect_uri)
    return redirect(auth_url)

@app.route('/get_token')
def get_token():
    code = request.args.get('code')
    if not code:
        return "Error: No code provided", 400

    token_response = client_app.acquire_token_by_authorization_code(code, scopes=scopes, redirect_uri=redirect_uri)
    access_token = token_response.get("access_token")

    if access_token:
        with open("access_token.txt", "w") as token_file:
            token_file.write(access_token)
        return f"Access Token salvato in 'access_token.txt': {access_token}"
    else:
        error = token_response.get("error")
        error_description = token_response.get("error_description")
        return f"Error: {error}, Description: {error_description}", 400

if __name__ == '__main__':
    app.run(port=5500)
