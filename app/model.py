from app import db

class Car(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(60), nullable=False)
    model = db.Column(db.String(60), nullable=False)
    color = db.Column(db.String(25), nullable=False)
    price = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<{self.brand} {self.model}>"