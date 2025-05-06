from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_micro.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # ✅ Ensures the 'user' table is created
    app.run(port=5001, debug=True)
