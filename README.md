# E-Commerce Cart System with Real-Time Discounts 🛒💸                                                                                                                                                                   
This solution was developed as part of a 3-hour challenge provided by Infinite Locus. The goal was to design and implement a functional e-commerce cart system with dynamic discount functionality. Here's an overview of our solution and its features:

---

## Problem Statement 📝

The task was to create a system that simulates the core functionalities of an e-commerce cart, including adding products, viewing cart details, and applying discounts dynamically based on the cart's total value.

**Key Requirements:**
1. **Backend:** 
   - RESTful APIs to:
     - Add a product to the cart.
     - Remove a product from the cart.
     - View cart details (including product list, total price, and discounts).
   - Use a database to manage product and cart details.

2. **Frontend:**
   - Simple web interface to:
     - Display available products.
     - Add/remove products from the cart.
     - Show cart value and applied discounts in real-time.

3. **Discount Logic:** 
   - ₹0 - ₹1000: No discount.
   - ₹1000 - ₹5000: 10% discount.
   - Above ₹5000: 20% discount.

4. **Deployment:** 
   - Deploy the application locally (or host in cloud).

5. **Bonus Features (Optional):**
   - User login to maintain individual carts.
   - Unit tests for API endpoints.

---

## Solution Overview 🔧

### Technologies Used:
- **Frontend:** HTML, CSS, JavaScript 🎨
- **Backend:** Python, Flask 🐍
- **Database:** SQLite, SQLAlchemy 💾

### Key Components:
- **Backend APIs:**
  - RESTful APIs built using Flask to handle cart operations such as adding, removing, and viewing products.
  - SQLAlchemy was used as the ORM to manage SQLite, ensuring efficient data storage and retrieval.

- **Frontend Interface:**
  - A responsive and user-friendly web interface using HTML, CSS, and JavaScript for managing products and viewing cart details.

- **Discount Logic:**
  - Integrated dynamic discount logic into the backend to compute real-time discounts as products were added to or removed from the cart.

- **Deployment:**
  - Hosted locally for development and testing purposes.

---

## Features and Highlights ✨
- **Dynamic Discounts:** Cart updates dynamically with applicable discounts based on value thresholds. 💰
- **Interactive Interface:** Intuitive design for smooth cart management. 🖥️
- **Scalable Backend:** Designed for future enhancements such as user authentication and advanced discount policies. 🔝

---

### Experience 🚀
This project demonstrates our ability to rapidly build, test, and deliver a fully functional solution within a tight 3-hour deadline. Despite the time constraint, we ensured that the solution was robust, efficient, and scalable. Future iterations could include features like user accounts, enhanced UI/UX, and cloud deployment.  

**Crafted with precision and dedication under 3 hours.** ⏳
