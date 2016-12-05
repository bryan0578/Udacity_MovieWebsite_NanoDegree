# Class for universal video information shared between movies and tv shows.
class Video():
    def __init__(self):
        # title
        # synopsis
        # duration
        # poster_image_url
        # trailer_youtube_url

# Class for information used only for movies.
class Movie(Video):
    def __init__(self):
        Video.__init__(self)
        #rating

    #Function that opens the browser to play trailers on youtube.
    def show_trailer(self):

# Class for information used only for tv shows.
class Tv_show(Video):
    def __init__(self):
        Video.__init__(self)
        # rating
        # seasons
        # episodes

    # Function that opens the browser to play trailers on youtube.
    def show_trailer(self):