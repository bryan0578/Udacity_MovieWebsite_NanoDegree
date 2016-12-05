# Class for universal video information shared between movies and tv shows.
class Video():
    def __init__(self, title, synopsis, duration, poster_image, trailer_youtube):
        self.title = title
        self.synopsis = synopsis
        self.duration = duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Class for information used only for movies.
class Movie(Video):
    def __init__(self, title, synopsis, rating, duration, poster_image, trailer_youtube):
        Video.__init__(self, title, synopsis, duration, poster_image, trailer_youtube)
        self.rating = rating

    #Function that opens the browser to play trailers on youtube.
    def show_trailer(self):

# Class for information used only for tv shows.
class Tv_show(Video):
    def __init__(self, title, synopsis, rating, duration, seasons, episodes, poster_image, trailer_youtube):
        Video.__init__(self, title, synopsis, rating, duration, poster_image, trailer_youtube)
        self.rating = rating
        self.seasons = seasons
        self.episodes = episodes

    # Function that opens the browser to play trailers on youtube.
    def show_trailer(self):