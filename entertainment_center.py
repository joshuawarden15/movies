#This is the file that contains the class that allows the creation of each movie link in the website
import media
#This is the file that runs the website using the entertainment_center file
import fresh_tomatoes


#These are the movie classes created using the media file
edge_of_tomorrow = media.Movie("Edge Of Tomorrow",
                               "Live. Die. Repeat.",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=yUmSVcttXnI")

serenity = media.Movie("Serenity",
                       "Cowboys in space with a psychic ninja warrior woman",
                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg",
                       "https://www.youtube.com/watch?v=w8JNjmK5lfk")

oblivion = media.Movie("Oblivion",
                       "Jack tries to save the world from itself",
                       "https://upload.wikimedia.org/wikipedia/en/2/2e/Oblivion2013Poster.jpg",
                       "https://www.youtube.com/watch?v=XmIIgE7eSak")

godzilla_2014 = media.Movie("Godzilla",
                            "Godzilla saves the world from malevolent monsters",
                            "https://upload.wikimedia.org/wikipedia/en/1/10/Godzilla_%282014%29_poster.jpg",
                            "https://www.youtube.com/watch?v=vIu85WQTPRc")

ten_items_or_less = media.Movie("10 Items Or Less",
                                "Movie star researches a movie roll and helps a woman down on her luck",
                                "https://upload.wikimedia.org/wikipedia/en/4/4d/Ten_items_or_less_poster.jpg",
                                "https://www.youtube.com/watch?v=alw0HHKn2Ig")

warcraft = media.Movie("Warcraft",
                       "Two worlds collide on the plains of Azeroth",
                       "https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg",
                       "https://www.youtube.com/watch?v=2Rxoz13Bthc")



#This is the list of the movies that is used in the fresh_tomatoes.py file to create the website
movies = [edge_of_tomorrow, serenity, oblivion, godzilla_2014, ten_items_or_less, warcraft]
#This method is called from the fresh_tomatoes file to use the list to create the website
fresh_tomatoes.open_movies_page(movies)

