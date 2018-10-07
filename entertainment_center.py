#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Main Module.
This python module is the main module of the movie trailer website. It contains all the movies and their relevant information. A user can add more movies just by adding a new instance containing the movie name, storyline, poster, and youtube url to the array of (MOVIES).
"""
import media
import fresh_tomatoes

#create new instance for each movie.
SPIDER_MAN = media.Movie('Spider man',
                        'A poor sickly orphan, is bitten by a radioactive spider. As a result of the bite, he gains superhuman strength, speed, and agility along with the ability to cling to walls.'
                        ,
                        'https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Spider-Man2002Poster.jpg/220px-Spider-Man2002Poster.jpg'
                        , 'https://www.youtube.com/watch?v=TYMMOjBUPMM'
                       )

DOCTOR_STRANGE = media.Movie('Doctor Strange', "Dr. Stephen Strange's (Benedict Cumberbatch) life changes after a car accident robs him of the use of his hands. When traditional medicine fails him, he looks for healing, and hope, in a mysterious enclave. He quickly learns that the enclave is at the front line of a battle against unseen dark forces bent on destroying reality. Before long, Strange is forced to choose between his life of fortune and status or leave it all behind to defend the world as the most powerful sorcerer in existence.",
                     'https://i.redd.it/myvs6zoz1qrz.jpg'
                     , 'https://www.youtube.com/watch?v=HSzx-zryEgM'
                    )

THE_FAULT_IN_OUR_STARS = media.Movie('The fault in our stars', 'young teenage girl who has been diagnosed with lung cancer and attends a cancer support group. Hazel is 16 and is reluctant to go to the support group, where she met a young boy named Hazel.',
                             'http://www.gstatic.com/tv/thumb/v22vodart/10372532/p10372532_v_v8_ae.jpg'
                             ,
                             'https://www.youtube.com/watch?v=9ItBvH5J6ss'
                            )

READY_PLAYER_ONE = media.Movie('Ready player one', 'cool movie with long storyline... too lazy to copy.',
                               'http://www.gstatic.com/tv/thumb/v22vodart/12806300/p12806300_v_v8_ac.jpg'
                               ,
                               'https://www.youtube.com/watch?v=cSp1dM2Vj48'
                              )



#the movies array, containing all the movies to display.
MOVIES = [SPIDER_MAN, DOCTOR_STRANGE, THE_FAULT_IN_OUR_STARS, READY_PLAYER_ONE]
#run the website from here, By opening the browser page.
fresh_tomatoes.open_movies_page(MOVIES)
      