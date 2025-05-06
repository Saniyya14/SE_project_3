from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monolith.db'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    device_id = db.Column(db.String(64), nullable=False)

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "User already exists"}), 409
    user = User(email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered"}), 201

# Device Login with 2-device limit
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    device_id = data['device_id']

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    user_devices = Device.query.filter_by(user_email=email).all()
    if device_id not in [d.device_id for d in user_devices]:
        if len(user_devices) >= 2:
            return jsonify({"message": "Device limit exceeded"}), 403
        db.session.add(Device(user_email=email, device_id=device_id))
        db.session.commit()
    return jsonify({"message": "Login successful"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)

