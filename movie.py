from video import Video


class Movie(Video):
    """Basic class to define the basic properties of a Movie.

    Movie inherits a Video class.

    Attributes:
        title (str): title of video
        description (str): brief description of the video
        rating (str): rating of the video, values in VideoRating class
        poster_image_url (str): link to artwork
        trailer_youtube_url (str): link to video
        duration (integer): length of movie

    """
    def __init__(self, title, description, rating, poster_image_url,
                 trailer_youtube_url, duration):

        Video.__init__(self, title, description, rating, poster_image_url,
                       trailer_youtube_url)

        self.duration = duration
