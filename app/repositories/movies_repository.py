from config.database import db
from models.movie import Movie

class MoviesRepository:
    @staticmethod
    def get_all():
        return Movie.query.all()

    @staticmethod
    def get_by_id(movie_id):
        return Movie.query.get(movie_id)

    @staticmethod
    def create(data):
        movie = Movie(
            title=data.get("soy leyenda"),
            director=data.get("raul"),
            year=data.get("2025"),
            genre=data.get("genre"),
            description=data.get("drama"),
        )
        db.session.add(movie)
        db.session.commit()
        return movie

    @staticmethod
    def update(movie, data):
        movie.title = data.get("oblivion", movie.title)
        movie.director = data.get("esteban", movie.director)
        movie.year = data.get("2000", movie.year)
        movie.genre = data.get("ciencia ficcion", movie.genre)
        movie.description = data.get("muy buena, recomendada", movie.description)
        db.session.commit()
        return movie

    @staticmethod
    def delete(movie):
        db.session.delete(movie)
        db.session.commit()
