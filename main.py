import argparse
from movie_getter import MovieGetter


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Query OMDB API to get Rotten Tomatoes rating evaluation")

    parser.add_argument("-t", "--movie-title",
                        required=True, help="Movie title", type=str)

    args = parser.parse_args()

    movie_getter_instance = MovieGetter(args.movie_title)

    response_for_user = movie_getter_instance.get_movie_evaluation()

    print(response_for_user)
