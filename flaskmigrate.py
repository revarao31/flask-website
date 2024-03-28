from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)
app.app_context().push()

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    def __repr__(self):
        return f"<Product {self.name}>"

# Create the database tables
db.create_all()

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
