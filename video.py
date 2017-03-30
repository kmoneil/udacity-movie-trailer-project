class Video:
    """Basic class to define the basic properties of a video.

    Attributes:
        title (str): title of video
        description (str): brief description of the video
        rating (str): rating of the video, values in VideoRating class
        poster_image_url (str): link to artwork
        trailer_youtube_url (str): link to video

    """
    def __init__(self, title, description, rating, poster_image_url,
                 trailer_youtube_url):

        self.title = title
        self.description = description
        self.rating = rating
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
