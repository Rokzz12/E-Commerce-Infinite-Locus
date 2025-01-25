# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    product = db.relationship('Product', backref=db.backref('cart_items', lazy=True))

def calculate_discount(total_price):
    if total_price < 1000:
        return 0
    elif 1000 <= total_price < 5000:
        return 0.1  # 10% discount
    else:
        return 0.2  # 20% discount

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id, 
        'name': p.name, 
        'price': p.price,
        'image_url': p.image_url
    } for p in products])

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.json
    product_id = data.get('product_id')
    product = Product.query.get(product_id)
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    cart_item = CartItem(product_id=product_id)
    db.session.add(cart_item)
    db.session.commit()
    
    return jsonify({'message': 'Product added to cart'})

@app.route('/cart/remove/<int:cart_item_id>', methods=['DELETE'])
def remove_from_cart(cart_item_id):
    cart_item = CartItem.query.get(cart_item_id)
    
    if not cart_item:
        return jsonify({'error': 'Cart item not found'}), 404
    
    db.session.delete(cart_item)
    db.session.commit()
    
    return jsonify({'message': 'Product removed from cart'})

@app.route('/cart/details', methods=['GET'])
def get_cart_details():
    cart_items = CartItem.query.all()
    total_price = sum(item.product.price for item in cart_items)
    
    discount_rate = calculate_discount(total_price)
    discounted_price = total_price * (1 - discount_rate)
    
    return jsonify({
        'items': [{
            'id': item.id,
            'product_id': item.product_id,
            'name': item.product.name,
            'price': item.product.price,
            'image_url': item.product.image_url
        } for item in cart_items],
        'total_price': total_price,
        'discount_rate': discount_rate,
        'discounted_price': discounted_price
    })

def init_db():
    with app.app_context():
        
        db.drop_all()
        db.create_all()
        
       
        if Product.query.count() == 0:
            sample_products = [
                Product(name='Laptop', price=45000, image_url='https://m.media-amazon.com/images/I/510uTHyDqGL.jpg'),
                Product(name='Smartphone', price=25000, image_url='https://m.media-amazon.com/images/I/61bK6PMOC3L.jpg'),
                Product(name='Headphones', price=3000, image_url='https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/MQTQ3?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1687660671363'),
                Product(name='Smartwatch', price=5000, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGG5lq3cYs7C71iSV1A2KiXy9SSc66lE5pyQ&s')
            ]
            db.session.bulk_save_objects(sample_products)
            db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

