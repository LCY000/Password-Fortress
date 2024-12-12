# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # 新增 email 欄位
    salt = db.Column(db.String(32), nullable=False)  # 專屬鹽值

# 新增的密碼儲存 Model
class PasswordEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    site_name = db.Column(db.String(150), nullable=False)
    site_username = db.Column(db.String(150), nullable=False)
    site_password = db.Column(db.String(300), nullable=False)  # 儲存經加鹽哈希過的密碼
    strength_score = db.Column(db.Integer, default=0)  # 預設強度分數為0
    user = db.relationship('User', backref='password_entries', lazy=True)