# creato da mio account ChatGPT
from flask import Flask, request, jsonify
import subprocess

# Inizializzazione dell'app Flask
app = Flask(__name__)

# Endpoint di test per verificare che il server sia attivo
@app.route('/')
def home():
    return "Server is running!"

# Endpoint per il download e la conversione
@app.route('/download', methods=['POST'])
def download():
    # Ottieni l'URL di YouTube dal JSON della richiesta
    youtube_url = request.json.get('url')
    if not youtube_url:
        return jsonify({'error': 'Missing URL'}), 400

    try:
        # Comando per yt-dlp
        command = ["yt-dlp", "-x", "--audio-format", "wav", youtube_url]
        subprocess.run(command, check=True)
        return jsonify({'status': 'success'}), 200
    except subprocess.CalledProcessError as e:
        # Gestione degli errori del comando yt-dlp
        return jsonify({'error': str(e)}), 500

# Punto di ingresso dell'app
if __name__ == '__main__':
    import os
    # Porta fornita da Heroku o di default a 5000
    port = int(os.environ.get('PORT', 5000))
    # Avvio del server Flask con debug abilitato
    app.run(debug=True, host='0.0.0.0', port=port)
