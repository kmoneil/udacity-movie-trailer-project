from video import Video


class TvShow(Video):
    """Basic class to define the basic properties of a TV Show and inherits
    a the properties of the Video Class.

    Attributes:
        title (str): title of video
        description (str): brief description of the video
        rating (str): rating of the video, values in VideoRating class
        poster_image_url (str): link to artwork
        trailer_youtube_url (str): link to video
        seasons (integer): how many season are available

    """
    def __init__(self, title, description, rating, poster_image_url,
                 trailer_youtube_url, seasons):

        Video.__init__(self, title, description, rating, poster_image_url,
                       trailer_youtube_url)

        self.seasons = seasons
