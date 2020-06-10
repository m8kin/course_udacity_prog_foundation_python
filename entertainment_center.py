'''
this is to be used in conjunction with the media.py class file
'''

# imports (from local folder)
import media
import movie_website

# Instances
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio"
                        )
#example usage
    #print(toy_story.storyline)
    #toy_story.show_trailer()

    
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                     )

district_9 = media.Movie("District 9",
                     "Alien refugee's get stranded on earth",
                     "https://upload.wikimedia.org/wikipedia/en/d/d7/District_nine_ver2.jpg",
                     "https://www.youtube.com/watch?v=82s9atP0teY"
                     )

predator = media.Movie("Predator",
                        "A soldier is hired resuce some politicians from a jungle where a badass alien resides",
                        "http://www.gstatic.com/tv/thumb/movieposters/10094/p10094_p_v8_ap.jpg",
                        "https://www.youtube.com/watch?v=Y1txEAywdiw"
                        )

the_incredibles = media.Movie("The Incredibles",
                     "A family of super heros live ordinary lives",
                     "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
                     "https://www.youtube.com/watch?v=eZbzbC9285I"
                     )

mad_max_fury_road = media.Movie("Mad Max: Fury road",
                     "Max takes on some nasty dudes in the desert",
                     "http://cdn2-www.comingsoon.net/assets/uploads/gallery/mad-max-fury-road-1406144100/10636937_661847177254140_3001186770164503894_o.jpg",
                     "https://www.youtube.com/watch?v=hEJnMQG9ev8"
                     )


# create an array named movies with all the Instances in it
movies = [toy_story, avatar, district_9, predator, the_incredibles, mad_max_fury_road]


movie_website.open_movies_page(movies)


