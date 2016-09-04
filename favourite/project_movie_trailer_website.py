import media
import fresh_tomatoes


# Set Movie class instances with my favourite movies.
# Arugments for class
# (movie title, movie storyline, poster image url, trailer youtube url)

hellboy2 = media.Movie("Hellboy II",
                       "A resuced baby demon is raise to save the world",
                       "http://ia.media-imdb.com/images/M/MV5BMjA5NzgyMjc2Nl5BMl5BanBnXkFtZTcwOTU3MDI3MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                       "https://www.youtube.com/watch?v=w4liPmQEPEU")

lord_of_the_rings = media.Movie("The Lord of the Rings",
                                "A meek Hobbit and eight companions set out on a journey to destroy the One Ring and the Dark Lord Sauron.",  # noqa
                                "http://ia.media-imdb.com/images/M/MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@._V1_.jpg",  # noqa
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",  # noqa
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",  # noqa
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

the_martian = media.Movie("The Martian",
                          "An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.",  # noqa
                          "http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club.",  # noqa
                         "http://ia.media-imdb.com/images/M/MV5BNGM2NjQxZTAtMmU5My00YTk5LWFmOWMtYjZlYzk4YzMwNjFlXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

burn_after_reading = media.Movie("Burn After Reading",
                                 "A disk containing the memoirs of a CIA agent ends up in the hands of two unscrupulous gym employees who attempt to sell it.",  # noqa
                                 "http://ia.media-imdb.com/images/M/MV5BMTczNjQxODE0N15BMl5BanBnXkFtZTcwMzIxMjc3MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=SVCHSiRWjJM")

# Create an array with my favourite movies
movies = [hellboy2,
          lord_of_the_rings,
          interstellar,
          the_martian,
          fight_club,
          burn_after_reading]

# Run website fresh tomatoes
fresh_tomatoes.open_movies_page(movies)
