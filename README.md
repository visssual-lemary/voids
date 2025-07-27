# 🏢 Business Data Management System
*Because spreadsheets are so last century, and we're not animals* 🦄

Welcome to the most over-engineered customer database you never knew you needed! This project takes the simple task of storing customer information and turns it into a full-blown FastAPI adventure. Because why use a simple CSV when you can have a SQLite database with more tables than a Swedish furniture store?

## 🎭 What Does This Thing Actually Do?

This system helps you manage:
- **Customers** 👥 (the people who pay your bills)
- **Products** 📦 (the things they hopefully buy)
- **Employees** 👔 (the heroes who make it all happen)
- **Sales** 💰 (the reason we're all here)

It's like a CRM system, but with 90% less corporate buzzwords and 100% more Python magic!

## 🚀 Features That Will Blow Your Mind
*(or at least mildly impress your cat)*

- **FastAPI Backend**: Because life's too short for slow APIs
- **SQLite Database**: Lightweight, like your New Year's resolutions
- **Faker Integration**: Generates fake data so realistic, it might fool your accountant
- **Customer Management**: Track customers better than social media tracks you
- **Data Analytics**: Group by customer types (because we love putting people in boxes)
- **RESTful Endpoints**: So RESTful, they're practically napping

## 🛠️ Installation & Setup
*Don't worry, it's easier than assembling IKEA furniture*

### Prerequisites
- Python 3.7+ (because we're not savages)
- A computer (preferably one that works)
- Basic understanding of databases (or at least the willingness to Google things)

### Quick Start
```bash
# Clone this masterpiece
git clone <your-repo-url>
cd business-data-system

# Install dependencies (prepare for magic)
pip install fastapi uvicorn sqlite3 faker pydantic

# Create and populate the database
python database.py

# Start the FastAPI server
uvicorn main:app --reload

# Navigate to http://localhost:8000 and witness greatness
```

## 📚 API Endpoints
*Your gateway to data nirvana*

- `GET /` - Says hello to Leslie (because everyone needs a friend)
- `GET /customers` - Retrieves all customers (prepare for information overload)
- `GET /items/{item_id}` - Gets specific items (with optional query parameters for the adventurous)

## 🗃️ Database Schema
*More organized than your sock drawer*

### Customers Table
Stores all the important people who give you money:
- Customer ID (auto-incrementing, because we're fancy)
- Personal info (name, email, phone - the usual suspects)
- Address details (where to send the thank you cards)
- Registration date (when they joined our cult... I mean customer base)
- Customer type (Individual or Business - we don't discriminate)

### Products Table
Your inventory, digitized:
- Product details, pricing, and stock levels
- Categories (because organization is key)
- Supplier information (for when things go wrong)

### Employees Table
The heroes behind the scenes:
- Employee information and roles
- Department assignments
- Salary details (shh, it's confidential)

## 📊 Example Usage

### Adding a Customer
```python
# Check out queries.py for a masterclass in customer creation
# Features the legendary "Hallo Voids" from wonderland
# Email: seeyousoon@zoom.de (we don't judge email choices)
```

### Analyzing Customer Data
```python
# Run groupby.py to see customer type distribution
# It's like a census, but more fun
```

## 🧪 Testing
We've included a Jupyter notebook (`test.ipynb`) because sometimes you need to see the data dance before your eyes.

## 🐛 Known Issues
- The system works too well (not really an issue, but we're humble)
- May cause excessive productivity
- Side effects include: improved data management and slight addiction to well-structured APIs

## 🤝 Contributing
Found a bug? Want to add a feature? Think our jokes are terrible? 

1. Fork the repo (it's not as violent as it sounds)
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request (and prepare for glory)

## 📝 License
This project is licensed under the "Do Whatever You Want But Don't Blame Us" License. 

## 🙏 Acknowledgments
- Coffee ☕ (the real MVP)
- Stack Overflow (for when we pretended to know what we were doing)
- The rubber duck on my desk (best debugging partner ever)
- Everyone who believed this README was a good idea

## 🆘 Support
If you're having trouble:
1. Try turning it off and on again
2. Check if you're using the right Python version
3. Make sure your database file exists
4. Sacrifice a rubber duck to the coding gods
5. Open an issue (we promise to respond faster than customer support)

---

*Made with ❤️, Python, and an unhealthy amount of caffeine*

**P.S.:** If this README made you smile, our work here is done. If it didn't, well... we'll work on our comedy skills. 😅