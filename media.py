import webbrowser

""" This class provides a way to store information used by class Movie and class Tv_show that will be inherited """
class Video():
    def __init__(self, title, synopsis, duration, poster_image, trailer_youtube):
        self.title = title
        self.synopsis = synopsis
        self.duration = duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

""" This clss provided a way to store information associated with the Movie class only. """
class Movie(Video):
    def __init__(self, title, synopsis, rating, duration, poster_image, trailer_youtube):
        Video.__init__(self, title, synopsis, duration, poster_image, trailer_youtube)
        self.rating = rating

    #Function that opens the browser to play trailers on youtube.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

""" This clss provided a way to store information associated with the Tv_show class only. """
class Tv_show(Video):
    def __init__(self, title, synopsis, rating, duration, seasons, episodes, poster_image, trailer_youtube):
        Video.__init__(self, title, synopsis, duration, poster_image, trailer_youtube)
        self.rating = rating
        self.seasons = seasons
        self.episodes = episodes

    # Function that opens the browser to play trailers on youtube.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)