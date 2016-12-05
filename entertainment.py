import media

""" This is a list of movies and their information that will be filled in using the class Movie """
toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as"
                        " top toy in a boy's room.",
                        "G",
                        "1hr 21min",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4-8yIHdMcnI")
# print(toy_story.synopsis)

rogue_one = media.Movie("Rogue One",
                        "The Rebellion makes a risky move to steal the plans to the Death Star, setting up the epic "
                        "saga to follow.",
                        "PG-13",
                        "2hr 13min",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://www.youtube.com/watch?v=4fE_yHEerok&t=18s")
# print(rogue_one.synopsis)
# print(rogue_one.rating)

# rogue_one.show_trailer()
nightmare_on_elm_street = media.Movie("A Nightmare On Elm Street",
                                      "Several people are hunted by a cruel serial killer who kills his victims in"
                                      " their dreams. While the survivors are trying to find the reason for being "
                                      "chosen, the murderer won't lose any chance to kill them as soon as they fall "
                                      "asleep.",
                                      "R",
                                      "1hr 31min",
                                      "https://upload.wikimedia.org/wikipedia/en/f/fa/A_Nightmare_on_Elm_Street_"
                                      "%281984%29_theatrical_poster.jpg",
                                      "https://www.youtube.com/watch?v=dCVh4lBfW-c")

jungle_book = media.Movie("The Jungle Book",
                          "After a threat from the tiger Shere Khan forces him to flee the jungle, a man-cub named "
                          "Mowgli embarks on a journey of self discovery with the help of panther, Bagheera, and free "
                          "spirited bear, Baloo.",
                          "PG",
                          "1hr 46min",
                          "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",
                          "https://www.youtube.com/watch?v=WtR9tqPa48s")

amadeus = media.Movie("Amadeus",
                      "The incredible story of Wolfgang Amadeus Mozart, told by his peer and secret rival Antonio "
                      "Salieri - now confined to an insane asylum.",
                      "R",
                      "2hr 40min",
                      "https://upload.wikimedia.org/wikipedia/en/2/2f/Amadeusmov.jpg",
                      "https://www.youtube.com/watch?v=yIzhAKtEzY0")

return_of_the_jedi = media.Movie("Star War Episode VI Return of the Jedi",
                                 "After rescuing Han Solo from the palace of Jabba the Hutt, the rebels attempt to destroy the "
                                 "second Death Star, while Luke struggles to make Vader return from the dark side of the Force.",
                                 "PG",
                                 "2hr 11min",
                                 "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                                 "https://www.youtube.com/watch?v=5UfA_aKBGMc")

# List of movies to output in the HTML page
movies = [toy_story, rogue_one, nightmare_on_elm_street, jungle_book, amadeus, return_of_the_jedi]

""" This is a list of tv shows and their information that will be filled in using the class Tv_show """
breaking_bad = media.Tv_show("Breaking Bad",
                             "A high school chemistry teacher diagnosed with inoperable lung cancer turns to "
                             "manufacturing and selling methamphetamine in order to secure his family's future.",
                             "TV-14",
                             "49min",
                             "5 Seasons",
                             "62 Episodes",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3"
                             "OTcyMDE@._V1_SY1000_CR0,0,678,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=XZ8daibM3AE")
# print(breaking_bad.synopsis)
# print(breaking_bad.seasons)

# breaking_bad.show_trailer()

charmed = media.Tv_show("Charmed",
                        "Three sisters discover their destiny - to battle against the forces of evil, using their "
                        "witchcraft. They are the Charmed Ones.",
                        "TV-14",
                        "42min",
                        "8 Seasons",
                        "179 Episodes",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg0ODAyNjkzMF5BMl5BanBnXkFtZTYwMTExMDU3."
                        "_V1_.jpg",
                        "https://www.youtube.com/watch?v=A2wmzteG_t8")

supernatural = media.Tv_show("Supernatural",
                             "Two brothers follow their father's footsteps as hunters fighting evil supernatural beings "
                             "of many kinds including monsters, demons, and gods that roam the earth.",
                             "TV-14",
                             "44min",
                             "12 Seasons",
                             "265 Episodes",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA1OTY0NTk5MTJeQTJeQWpwZ15BbWU4MDY"
                             "wMjU4MjAy._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=ihh0xfsvyDg")

lucifer = media.Tv_show("Lucifer",
                        "Lucifer takes up residence in Los Angeles.",
                        "TV-14",
                        "42min",
                        "2 Seasons",
                        "35 Episodes",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4MTU0NzE1OF5BMl5BanBnXkFtZTgwODI3NDc0"
                        "OTE@._V1_SY1000_CR0,0,646,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=N7Y_JxjbRS4")

nurse_jackie = media.Tv_show("Nurse Jackie",
                             "A drug-addicted nurse struggles to find a balance between the demands of her frenetic job"
                             " at a New York City hospital and an array of personal dramas.",
                             "TV-MA",
                             "27min",
                             "7 Seasons",
                             "80 Episodes",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkwMjA4Mzc3M15BMl5BanBnXkFtZTgwNDk"
                             "1Njc2MTE@._V1_.jpg",
                             "https://www.youtube.com/watch?v=5dpjMmSLjvQ")

friends = media.Tv_show("Friends",
                        "Follows the personal and professional lives of six 20 to 30-something-year-old friends living "
                        "in Manhattan.",
                        "TV-14",
                        "22min",
                        "10 Seasons",
                        "236 Episodes",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4NzEyNzQ5OF5BMl5BanBnXkFtZTYwNTY3NDg"
                        "4._V1._CR24,0,293,443_.jpg",
                        "thttps://www.youtube.com/watch?v=hDNNmeeJs1Q")

# List of tv shows to output in the HTML page
tvShows = [breaking_bad, charmed, supernatural, lucifer, nurse_jackie, friends]

# print(movies)
# print(tvShows)
