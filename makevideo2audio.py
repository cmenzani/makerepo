# creato da mio account ChatGPT
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    youtube_url = request.json.get('url')
    if not youtube_url:
        return jsonify({'error': 'Missing URL'}), 400

    try:
        command = ["yt-dlp", "-x", "--audio-format", "wav", youtube_url]
        subprocess.run(command, check=True)
        return jsonify({'status': 'success'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
