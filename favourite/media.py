import webbrowser


class Movie():
    # triple quotes allows for setting class variable __doc__
    """ This class provides a way to store movie related information

        Attributes:
            movie title (str): Specify the title of the movie
            movie storyline (str): Movie description or plot
            poster image url (str): A URL of the movie poster
            trailer youtube url (str): A URL of the movie trailer

        Method:
            show_trailer(): opens a web broswer and loads instance's trailer

    """

    # Class Constructor Arugments for class
    # (movie title, movie storyline, poster image url, trailer youtube url)
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image, trailer_youtube):

        # Instance variables to be set via contructor
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Class method for showing trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
