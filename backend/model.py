from datetime import date
from config import db

class TransactData(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date = db.Column(db.Date, nullable=True)
    category = db.Column(db.String(50), nullable = True)
    amount = db.Column(db.Float,nullable = True)

    def __rep__(self):
        return f'<TransactDate id={self.id} date={self.date} category={self.category} amount={self.amount}>'