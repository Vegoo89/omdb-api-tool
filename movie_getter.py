import os
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MovieGetter:

    def __init__(self, movie_title):

        if 'API_KEY' not in os.environ:
            raise Exception("API_KEY not found in environ! Set it first!")

        self.api_key = os.environ['API_KEY']

        self.movie_title = movie_title

        self.request_url = "http://www.omdbapi.com/?t=%s&apikey=%s" \
                           % (movie_title, self.api_key)

    def create_rating_response(self, rotten_tomato_rating_string):

        rotten_tomato_rating_string = rotten_tomato_rating_string.replace(
            "%", "")

        try:
            rotten_tomato_rating = int(rotten_tomato_rating_string)
        except ValueError:
            return "Rotten Tomatoes OMDB API Rating for movie %s couldn't " \
                   "be converted to integer. Original value: %s" \
                   % (self.movie_title, rotten_tomato_rating_string)

        # Simple movie to score mapping response

        sentence_start = "%s movie score on Rotten Tomatoes is %i%%. " \
                         % (self.movie_title, rotten_tomato_rating)

        if rotten_tomato_rating >= 90:
            response = sentence_start + "This movie has to be almost perfect!"

        elif rotten_tomato_rating >= 60:
            response = sentence_start + "This movie seems great!"

        elif rotten_tomato_rating >= 40:
            response = sentence_start + \
                       "This doesn't seem like a great movie at all."

        else:
            response = sentence_start + \
                       "Watch it on your own risk - it's most likely terrible."

        return response

    def get_movie_evaluation(self):

        logger.info("Creating request for movie %s" % self.movie_title)

        try:

            response = requests.post(url=self.request_url)

        except Exception as broad_exception:

            return "Ups! Something went wrong while receiving OMDB API " \
                   "response. Error: %s" % broad_exception

        status_code = response.status_code

        if status_code == 200:

            response_json = response.json()
            response_param = response_json["Response"]

            if response_param == "True":

                all_ratings = response_json["Ratings"]

                for rating in all_ratings:

                    if rating["Source"] == "Rotten Tomatoes":
                        rotten_tomato_rating_string = rating["Value"]
                        return self.create_rating_response(
                            rotten_tomato_rating_string)

                return "Rotten Tomatoes rating not found for %s movie!" \
                       % self.movie_title

            elif response_param == "False":

                error_message = "Unknown"

                if "Error" in response_json:
                    error_message = response_json["Error"]

                return "It seems there was a problem with " \
                       "getting movie data. Error message: %s" \
                       % error_message

            else:
                return "Response parameter returned by OMDB API " \
                       "seems incorrect. Parameter value: %s" % response_param
        else:

            return "OMDB API returned non-200 status code: %i " \
                   "with content: %s" \
                   % (status_code, response.content.decode("utf-8"))
