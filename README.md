# General

OMDB Api Tool is simple tool for getting Rotten Tomatoes rating evaluation based on provided movie title.

Movie title can be provided via `-t` or `--movie-title` command line arguments

# Installation & Setup:

Tool has been developed in Python 3.6

After cloning run `pip install -r requirements.txt`

And set `API_KEY` in environment

# Docker local setup & running

After cloning repo from git, navigate to main directory and build an image:

`docker build -t omdb-api-tool:latest .`

Then to get output in console, run:

`docker run --env API_KEY="Your_API_KEY" --rm omdb-api-tool:latest -t "Movie Title"`

# Examples

Example usage:

Standard response:

`python main.py -t "Shrek"`

`Shrek movie score on Rotten Tomatoes is 88%. This movie seems great!`

If Rotten Tomatoes rating is not present in response:

`python main.py -t "Godfather"`

`Rotten Tomatoes rating not found for Godfather movie!`

If movie title was not found:

`python main.py -t "Godfatherr"`

`It seems there was a problem with getting movie data. Error message: Movie not found!
`



