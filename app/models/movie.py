from config.database import db

class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    director = db.Column(db.String(120), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    genre = db.Column(db.String(80), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "director": self.director,
            "year": self.year,
            "genre": self.genre,
            "description": self.description,
        }

    def __repr__(self):
        return f"<Movie {self.title}>"
