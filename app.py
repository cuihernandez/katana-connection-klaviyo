import requests

# Replace with your actual API key
API_KEY = '1fa7c34f-9711-43c4-a73e-7f961e76ec58'

# Katana API base URL
BASE_URL = 'https://api.katanamrp.com'

# Headers for authentication
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

def get_sales_orders():
    # Endpoint to retrieve sales orders
    endpoint = f'{BASE_URL}/sales-orders'
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def check_make_to_order_sales_orders():
    sales_orders = get_sales_orders()
    if sales_orders:
        for order in sales_orders:
            if order.get('production') == 'make to order':
                print(f"Order ID {order['id']} is marked as 'make to order'.")

if __name__ == "__main__":
    check_make_to_order_sales_orders()
