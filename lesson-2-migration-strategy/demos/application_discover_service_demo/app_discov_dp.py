import pandas as pd

def process_sales_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Perform some data processing
    df['total_sales'] = df['quantity'] * df['price']
    df['sales_category'] = pd.cut(df['total_sales'], bins=[0, 100, 1000, float('inf')], labels=['Low', 'Medium', 'High'])
    
    # Save the processed data
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    process_sales_data('sales_data.csv', 'processed_sales_data.csv')