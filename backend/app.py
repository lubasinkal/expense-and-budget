from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from config import db, app
from model import TransactData


UPLOAD_FOLDER = 'uploads'  # Directory to save uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create all tables (optional if you run this script standalone)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start')
def init():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
     # Extract data from the form
    date_str = request.form.get('date')
    category = request.form.get('category')
    amount = request.form.get('amount')
    
    # Convert the date string to a Python date object
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    # Create a new TransactData instance
    new_transaction = TransactData(
        date=date_obj,
        category=category,
        amount=float(amount)  # Convert amount to float
    )
    
    # Add and commit the new transaction to the database
    db.session.add(new_transaction)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    
    if file:
        filename = file.filename
        if filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return "Unsupported file format", 400
        
        # Assuming the dataframe has columns 'Date', 'Category', 'Amount'
        for index, row in df.iterrows():
            date_obj = pd.to_datetime(row['Date']).date()
            category = row['Category']
            amount = float(row['Amount'])
            
            new_transaction = TransactData(
                date=date_obj,
                category=category,
                amount=amount
            )
            db.session.add(new_transaction)
        
        db.session.commit()
        return redirect(url_for('view_transactions'))
    
    return "No file uploaded", 400

@app.route('/view')
def view_transactions():
    transactions = TransactData.query.all()  # Query all transactions
    return render_template('view.html', transactions=transactions)

@app.route('/report/monthly')
def monthly_report():
    from sqlalchemy import func
    result = db.session.query(
        func.strftime('%Y-%m', TransactData.date).label('month'),
        func.sum(TransactData.amount).label('total_amount')
    ).group_by('month').all()
    
    return render_template('monthly_report.html', results=result)

@app.route('/report/category')
def category_report():
    from sqlalchemy import func
    result = db.session.query(
        TransactData.category,
        func.sum(TransactData.amount).label('total_amount')
    ).group_by(TransactData.category).all()
    
    return render_template('category_report.html', results=result)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    transaction = TransactData.query.get_or_404(id)

    if request.method == 'POST':
        date_str = request.form.get('date')
        category = request.form.get('category')
        amount = request.form.get('amount')
        
        # Convert the date string to a Python date object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        transaction.date = date_obj
        transaction.category = category
        transaction.amount = float(amount)  # Convert amount to float
        
        db.session.commit()
        return redirect(url_for('view_transactions'))
    
    return render_template('edit.html', transaction=transaction)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    transaction = TransactData.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for('view_transactions'))


if __name__ == '__main__':
    app.run(debug=True)
