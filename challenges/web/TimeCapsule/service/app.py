from flask import Flask, request, jsonify, render_template
import datetime

app = Flask(__name__)
otp = "8911"

@app.route('/timestamp-endpoint', methods=['POST'])
def timestamp_endpoint():
    data = request.json
    opt_value = data.get('opt') if data else None

    client_timestamp = request.headers.get('timestamp')

    if not opt_value:
        return jsonify({"error": "'opt' parameter not provided in the request body"}), 400

    if not client_timestamp:
        return jsonify({"error": "Timestamp header not provided"}), 400

    if opt_value != otp:
        return jsonify({"error": "OTP is invalid"}), 403

    try:
        client_datetime = datetime.datetime.fromtimestamp(int(client_timestamp))
    except ValueError:
        return jsonify({"error": "Invalid timestamp format."}), 400

    today = datetime.date.today()
    required_date = today.replace(year=today.year + 100)

    if client_datetime.date() != required_date:
        return jsonify({"error": "Please try again in 100 years from today."}), 400

    message = "YCEP25{w3b_1n_1h3_fTR25743}"
    return jsonify({"message": message}), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31000)

