

import http.client
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Configurazione delle API di Google Sheets
creds_file = '/Users/federicodonati/Downloads/turnscheduler-21773e70ad4e.json'
spreadsheet_id = '1xGH4PfOp7iwjwiwroBC9CfMx95D0PZ2AAzrvpurfi34'

# Autenticazione con Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
client = gspread.authorize(creds)

try:
    # Apri il foglio di calcolo
    sheet = client.open_by_key(spreadsheet_id).sheet1
except gspread.exceptions.SpreadsheetNotFound:
    print("Errore: Il foglio di calcolo specificato non è stato trovato. Verifica l'ID e i permessi.")

# Funzione per aggiungere i dati nel foglio di Google Sheets
def add_new_row(name, username, followers, following):
    # Aggiungi una nuova riga con i dati specificati
    row_data = [name, username, followers, following, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    sheet.append_row(row_data)

# Richiesta API per ottenere i dati del profilo Instagram
def update_profile(igusername):
    conn = http.client.HTTPSConnection("instagram-looter2.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "756b651f94msh1904bd2df3b6cfap1dcf9ajsn060dec362c83",
        'x-rapidapi-host': "instagram-looter2.p.rapidapi.com"
    }

    conn.request("GET", "/profile?username=" + igusername, headers=headers)

    res = conn.getresponse()
    data = res.read()

    # Decodifica la risposta dell'API
    profile_data = json.loads(data.decode("utf-8"))

    # Estrai i dati necessari
    full_name = profile_data["full_name"]
    username = profile_data["username"]
    followers = profile_data["edge_followed_by"]["count"]
    following = profile_data["edge_follow"]["count"]

    # Aggiungi una nuova riga nel foglio di Google Sheets
    add_new_row(full_name, username, followers, following)

print("Foglio di Google Sheets aggiornato con successo!")
