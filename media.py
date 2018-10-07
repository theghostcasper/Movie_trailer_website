#!/usr/bin/python
# -*- coding: utf-8 -*-

"""media module, containing classes for media.
This module contains classes that holds different media information.

"""


class Video():
  """Blueprint that holds video information.

  This class holds video information, like video title.

  Attributes:
    video_title: string containing the title of the video.
  """

  def __init__(self, video_title):
    """Inits Video with given attributes."""
    self.title = video_title


class Movie(Video):
  """Blueprint that holds movies information.

    This class holds movie information, like movie title, storyline, poster url and trailer url

    Attributes:
        movie_title: string containing the title of the movie.
        movie_storyline: containing the storyline of the movie.
        poster_image: a poster image url for the movie.
        trailer_youtube: the youtube trailer to be showed.
    """
  def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    Video.__init__(self,movie_title)
    """Inits Movie with given Attributes."""
    self.movie_storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube
