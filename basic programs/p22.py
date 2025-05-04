stock_available = input("The product is available? (Yes/No):").strip().lower()
area_pincode = input("The product is available in that area?: (Yes/No)").strip().lower()

if stock_available == 'yes' and area_pincode == 'yes':
    print("The product is available")
else:
    print("The product is not available")