import streamlit as st
import random
import pandas as pd

class ProductNode:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.next = None

class ProductLinkedList:
    def __init__(self):
        self.head = None

    def insert_product(self, product_id, name, price, category):
        new_node = ProductNode(product_id, name, price, category)
        new_node.next = self.head
        self.head = new_node

    def display_products(self):
        products = []
        current = self.head
        while current:
            products.append({
                "Product ID": current.product_id,
                "Name": current.name,
                "Price": current.price,
                "Category": current.category
            })
            current = current.next
        return products

    def get_recommendations(self, liked_product):
        recommendations = []
        current = self.head
        while current:
            if current.category == liked_product.category and current.product_id != liked_product.product_id:
                recommendations.append(current)
            current = current.next
        return recommendations


def generate_random_products(product_list, num_products=100):
    categories = ['Electronics', 'Home Appliances', 'Books', 'Clothing', 'Sports Equipment', 'Toys']
    names = {
        'Electronics': ['Smartphone', 'Laptop', 'Tablet', 'Camera', 'Smartwatch', 'Wireless Headphones'],
        'Home Appliances': ['Blender', 'Coffee Maker', 'Microwave', 'Vacuum Cleaner', 'Air Purifier'],
        'Books': ['Fiction Book', 'Non-Fiction Book', 'Cookbook', 'Graphic Novel', 'Biography'],
        'Clothing': ['T-shirt', 'Jeans', 'Jacket', 'Sneakers', 'Dress'],
        'Sports Equipment': ['Football', 'Tennis Racket', 'Yoga Mat', 'Dumbbells', 'Bicycle'],
        'Toys': ['Lego Set', 'Puzzle', 'Doll', 'Action Figure', 'Board Game']
    }

    for product_id in range(1, num_products + 1):
        category = random.choice(categories)
        name = random.choice(names[category])
        price = round(random.uniform(10, 1500), 2)  
        product_list.insert_product(product_id, name, price, category)


product_list = ProductLinkedList()
generate_random_products(product_list, 100)


if 'cart' not in st.session_state:
    st.session_state.cart = []

# header 
st.sidebar.header("DSA BootCamp Minor Project")
st.sidebar.markdown("### E-Commerce Recommendation System Using Linked-List")
st.sidebar.markdown("Team Name")
st.sidebar.text("""
                Anish Kumar     :  2247341
                Preeti kumari   :  2246955
                Ankit Kumar     :  2247340
                """)

st.title("E-Commerce Recommendation System")

# Display all products
# """ st.subheader("Available Products")
# products = product_list.display_products()
# for product in products:
#     st.write(f"**Product ID:** {product['Product ID']}, **Name:** {product['Name']}, **Price:** ${product['Price']}, **Category:** {product['Category']}")
# """

st.subheader("Available Products")
products = product_list.display_products()

# Convert list of products to a DataFrame
products_df = pd.DataFrame(products)

# Display the DataFrame using Streamlit's st.dataframe function
st.dataframe(products_df)


st.subheader("Select a product you like:")
product_ids = [product['Product ID'] for product in products]
selected_product_id = st.selectbox("Choose a Product ID", product_ids)


selected_product = next((p for p in products if p['Product ID'] == selected_product_id), None)

if selected_product:
    st.success(f"You selected: {selected_product['Name']}.")

    if st.button("Recommended"):
        recommendations = product_list.get_recommendations(ProductNode(selected_product['Product ID'], selected_product['Name'], selected_product['Price'], selected_product['Category']))
        
        st.subheader("Recommended Products:")
        
        if recommendations:
            cols = st.columns(3) 
            for index, rec in enumerate(recommendations):
                with cols[index % 3]:  
                    st.markdown(f"**Product ID:** {rec.product_id}")
                    st.markdown(f"**Name:** {rec.name}")
                    st.markdown(f"**Price:** ${rec.price}")
                    st.markdown(f"**Category:** {rec.category}")
                    
                    # Unique key for each button to prevent conflicts
                    add_to_cart_key = f"add_{rec.product_id}"
                    if st.button("Add to Cart", key=add_to_cart_key):  
                        # Add the selected product to the cart
                        st.session_state.cart.append({
                            "Product ID": rec.product_id,
                            "Name": rec.name,
                            "Price": rec.price,
                            "Category": rec.category
                        })
                        st.success(f"{rec.name} has been added to your cart!")
                    st.write("---")  # Divider for better spacing
        else:
            st.warning("No recommendations available.")


st.subheader("Your Cart:")
if st.session_state.cart:
    for item in st.session_state.cart:
        st.write(f"**Product ID:** {item['Product ID']}, **Name:** {item['Name']}, **Price:** ${item['Price']}, **Category:** {item['Category']}")
else:
    st.write("Your cart is empty.")


if st.button("Buy Now"):
    if st.session_state.cart:
        total_price = sum(item['Price'] for item in st.session_state.cart)
        st.success(f"You have purchased {len(st.session_state.cart)} items for a total of ${total_price:.2f}. Thank you for your purchase!")
        st.session_state.cart = [] 
    else:
        st.warning("Your cart is empty. Please add items to your cart before purchasing.")

