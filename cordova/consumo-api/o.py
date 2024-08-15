from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def fetch_user_data():
    url = 'https://davidsousaplay.pythonanywhere.com/users/name/s'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vai levantar uma exceção para erros HTTP
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
