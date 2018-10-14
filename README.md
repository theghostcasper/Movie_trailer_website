# Movie trailer website

### By Hazim Mohamed
This website is part of the [Full stack Developer nanodegree of udacity](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Project description

This project is a Movie trailer website. It allows users to see the movies i like and view its trailers too. 
The project consists of three main files:

1. `fresh_tomatoes.py`, It is the tool used to parse the html code and add the links, images and youtube trailers. Then generate an HTML file that the browser understands.

2. `entertainment_center.py`, This is the main program used to create an instance for each movie, those instances are later passed to the `fresh_tomatoes.py` file, which in turn generates the html code based on the movie instances created.

3. `media.py`. This python file contains the blueprints (classes) that is used to hold movie information. These classes are then used by the `entertainment_center.py` to create the movie instances.

## Project requirements

To be able to run this project you should have done the following.

1. Download any python 2 version. visit [this website to download python](https://www.python.org/)
2. Add python to path. [Here's how you can add python to path](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows).

## How to run the website

1. download the repository or clone it by typing: $ `git clone https://github.com/SteveWooding/movie-website` in the git bash
2. Then: $ `cd "movie-website"` 
3. execute the entertainment_center.py script by entering: $ `python entertainment_center.py`

The browser will then launch the movie trailer website.

## FAQ

### 1. how to view the story line ?
A. to view the storyline just put the cursur over the movie you like.

### 2. how to view the trailer ?
A. just click on the movie you like.