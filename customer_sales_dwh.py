from etl.extract import extract
from etl.transform import transform_data
from etl.load import load_data

def main():
    print("✅ Customer Sales ETL Started")

    # Extract
    customers, products, sales, stores = extract()

    # Transform
    customers, products, sales, stores = transform_data(
        customers, products, sales, stores
    )

    # Load
    load_data(customers, products, sales, stores)

    print("✅ Project Executed Successfully")

if __name__ == "__main__":
    main() 
    
    



  