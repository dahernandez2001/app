from repositories.movies_repository import MoviesRepository

class MoviesService:
    @staticmethod
    def list_movies():
        movies = MoviesRepository.get_all()
        return [m.to_dict() for m in movies]

    @staticmethod
    def get_movie(movie_id):
        m = MoviesRepository.get_by_id(movie_id)
        return m.to_dict() if m else None

    @staticmethod
    def create_movie(data):
        movie = MoviesRepository.create(data)
        return movie.to_dict()

    @staticmethod
    def update_movie(movie_id, data):
        movie = MoviesRepository.get_by_id(movie_id)
        if not movie:
            return None
        updated = MoviesRepository.update(movie, data)
        return updated.to_dict()

    @staticmethod
    def delete_movie(movie_id):
        movie = MoviesRepository.get_by_id(movie_id)
        if not movie:
            return False
        MoviesRepository.delete(movie)
        return True
