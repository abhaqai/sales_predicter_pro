from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        try:
            # Get all form inputs with defaults
            unit_price = float(request.form.get('unit_price', 0))
            quantity = int(request.form.get('quantity', 0))
            customer_type = int(request.form.get('customer_type', 0))
            gender = int(request.form.get('gender', 0))
            rating = float(request.form.get('rating', 0))
            branch = request.form.get('branch', 'Alex')
            city = request.form.get('city', 'Yangon')
            payment = request.form.get('payment', 'Cash')
            product_line = request.form.get('product_line', 'Health and beauty')
            
            # Create a DataFrame with all features initialized to 0
            input_data = pd.DataFrame(0, index=[0], columns=[
                'Customer type', 'Gender', 'Unit price', 'Quantity', 'Tax 5%', 'cogs',
                'gross margin percentage', 'Rating', 'Branch_Alex', 'Branch_Cairo',
                'Branch_Giza', 'City_Mandalay', 'City_Naypyitaw', 'City_Yangon',
                'Payment_Cash', 'Payment_Credit card', 'Payment_Ewallet',
                'Product line_Electronic accessories', 'Product line_Fashion accessories',
                'Product line_Food and beverages', 'Product line_Health and beauty',
                'Product line_Home and lifestyle', 'Product line_Sports and travel'
            ])
            
            # Set values from form inputs
            input_data['Customer type'] = customer_type
            input_data['Gender'] = gender
            input_data['Unit price'] = unit_price
            input_data['Quantity'] = quantity
            input_data['Rating'] = rating
            
            # Calculate derived fields
            input_data['Tax 5%'] = unit_price * quantity * 0.05
            input_data['cogs'] = unit_price * quantity
            input_data['gross margin percentage'] = 4.761905
            
            # Set categorical features (one-hot encoded)
            input_data[f'Branch_{branch}'] = 1
            input_data[f'City_{city}'] = 1
            input_data[f'Payment_{payment}'] = 1
            input_data[f'Product line_{product_line}'] = 1
            
            # Make prediction
            prediction = model.predict(input_data)[0]
            prediction = round(prediction, 2)
            
        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)