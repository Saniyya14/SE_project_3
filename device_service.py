from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devices_micro.db'
db = SQLAlchemy(app)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    device_id = db.Column(db.String(64), nullable=False)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    device_id = data['device_id']
    user_devices = Device.query.filter_by(user_email=email).all()
    if device_id not in [d.device_id for d in user_devices]:
        if len(user_devices) >= 2:
            return jsonify({"message": "Device limit exceeded"}), 403
        db.session.add(Device(user_email=email, device_id=device_id))
        db.session.commit()
    return jsonify({"message": "Login successful"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # ✅ Ensures 'device' table is created
    app.run(port=5002, debug=True)
