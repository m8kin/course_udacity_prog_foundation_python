# imports
import webbrowser

# define the class
class Movie():
    
    # initialse a Constructor (space in memory) for the class to be used and defines self
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        
        # set Instance Variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    # create an Instance Method (function inside a class) as load movie trailer
    def show_trailer(self):
        
        # use webbrowser.open to open a url link
        webbrowser.open(self.trailer_youtube_url)
        