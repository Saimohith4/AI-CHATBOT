import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(BASE_DIR, 'survey.xlsx')

try:
    df = pd.read_excel(excel_path, engine='openpyxl')
    df.columns = df.columns.str.strip()

    print(df.head())
    print(df.columns)
    print("Dataset Loaded Successfully")
except Exception as e:
    import traceback
    traceback.print_exc()
    df = pd.DataFrame()


def find_customers_by_interest(product_name):

    if df.empty:
        return "Dataset could not be loaded."

    product_name = product_name.lower()

    matches = df[df['Interested Products'].str.lower().str.contains(product_name, na=False)]

    if matches.empty:
        return "No customers found for that product."

    response = ""

    for _, row in matches.iterrows():

        response += f"""
    <div class="customer-card">
        <p><strong>👤 Customer Name:</strong> {row['Customer Name']}</p>
        <p><strong>📧 Email:</strong> {row['Email']}</p>
        <p><strong>📞 Phone:</strong> {row['Phone']}</p>
        <p><strong>🎯 Interested Products:</strong> {row['Interested Products']}</p>
    </div>
    """

    return response