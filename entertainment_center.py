#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Main Module.
This python module is the main module of the movie trailer website. It contains all the movies and their relevant information. A user can add more movies just by adding a new instance containing the movie name, storyline, poster, and youtube url to the array of (MOVIES).
"""
import media
import fresh_tomatoes

#create new instance for each movie.
TOY_STORY = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life'
                        ,
                        'http://www.gstatic.com/tv/thumb/v22vodart/17420/p17420_v_v8_an.jpg'
                        , 'https://www.youtube.com/watch?v=KYz2wyBy3kc'
                       )

AVATAR = media.Movie('Avatar', 'A marine on an alien planet',
                     'http://www.gstatic.com/tv/thumb/v22vodart/3542039/p3542039_v_v8_ac.jpg'
                     , 'https://www.youtube.com/watch?v=5PSNL1qE6VY'
                    )

SCHOOL_OF_ROCK = media.Movie('school of rock', 'Story line',
                             'https://lh3.ggpht.com/w60u7fTrzb6Sgrf0Atg3UY1rOA0cK8VB-BE6ItGxov-ePzEGuwZbhjbTQ6G-ahzO8tUW=w200-h300'
                             ,
                             'https://www.youtube.com/watch?v=XCwy6lW5Ixc'
                            )

THE_HUNGER_GAMES = media.Movie('The Hunger games', 'Story line',
                               'https://upload.wikimedia.org/wikipedia/en/thumb/9/9d/Mockingjay_Part_2_Poster.jpg/220px-Mockingjay_Part_2_Poster.jpg'
                               ,
                               'https://www.youtube.com/watch?v=PbA63a7H0bo'
                              )


#the movies array, containing all the movies to display.
MOVIES = [TOY_STORY, AVATAR, SCHOOL_OF_ROCK, THE_HUNGER_GAMES]
#run the website from here, By opening the browser page.
fresh_tomatoes.open_movies_page(MOVIES)
      