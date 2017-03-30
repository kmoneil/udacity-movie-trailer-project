#!/usr/bin/env python

import webbrowser
import os
import re

from movie import Movie
from tvshow import TvShow
from videorating import VideoRating

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Udacity Movie Project</title>
    <link rel="stylesheet" 
        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css"
        integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" 
        crossorigin="anonymous">

    <style type="text/css">
        .movies, .tv {
            padding: 25px;
        }
        .card {
            border: 0;
            margin: 5px;
            position: relative;
            overflow: hidden;
            color: #ffffff;
            font-size: 12px;
            cursor: pointer;
        }
        .card-details {
            position: absolute;
            height: 150px;
            width: 220px;
            bottom: -150px;
            background-color: #000000;
            opacity: 1;
            -webkit-transition: all 300ms ease-out;
            -moz-transition: all 300ms ease-out;
            -ms-transition: all 300ms ease-out;
            -o-transition: all 300ms ease-out;
            transition: all 300ms ease-out;
        }
        .card-other {
            font-size: 13px;
        }
        .card:hover .card-details {
            transform: translateY(-150px);
            -webkit-transform:translateY(-150px);
            -moz-transform:translateY(-150px);
            -ms-transform:translateY(-150px);
            -o-transform:translateY(-150px);
        }
    </style>
  </head>
'''

main_page_content = '''
    <body>
        <div class="navbar navbar-inverse bg-inverse">
            <div class="container d-flex justify-content-between">
                <a href="#" class="navbar-brand">Movie/TV Project</a>
            </div>
        </div>
        <!-- Section for movies -->
        <section class="movies">
            <div class="container">
                <h3>Movies</h3>
                <div class="row">{movies}</div>
            </div>
        </section>

        <!-- Section for tv shows -->
        <section class="tv">
            <div class="container">
                <h3>TV Shows</h3>
                <div class="row">{tvshows}</div>
            </div>
        </section>

        <!-- Pop up modal to display trailer -->
        <div id="trailerModal" class="modal fade" tabindex="-1" role="dialog" 
            aria-hidden="true">

            <div class="modal-dialog modal-lg">
                <div class="modal-content text-center">
                    <iframe id="tubePlayer" type="text/html" width="100%" 
                        height="480" src="" frameborder="0"></iframe>
                </div>
            </div>
        </div>

        <script src="https://code.jquery.com/jquery-3.2.1.min.js"
            integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
            crossorigin="anonymous"></script>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" 
            integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" 
            crossorigin="anonymous"></script>
        
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" 
            integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn"
            crossorigin="anonymous"></script>

        <script type="text/javascript" charset="utf-8">
            $(document).ready(function () {{
                $(".card").on("click", function() {{
                    $("#tubePlayer").attr("src", $(this).data("trailer-youtube-id"));
                    $("#trailerModal").modal("show");
                }});
                $("#trailerModal").on("hidden.bs.modal", function () {{
                    $("#tubePlayer").attr("src", "");
                }});
            }});
        </script>
    </body>
</html>
'''

# A single video entry html template
video_tile_content = '''
<div class="card" data-trailer-youtube-id="{trailer_youtube_id}">
    <img class="card-img-top" src="{poster_image_url}" alt="" 
        width="220" height="342">

    <div class="card-details">
        <div class="card-block">
            <h6 class="card-title">{video_title}</h6>
            <p class="card-text">{video_description} ...</p>
            <div class="row card-other">
                <div class="col-3">
                    <p>
                        <span class="badge badge-primary">{video_rating}</span>
                    </p>
                </div>
                <div class="col-9 text-right">
                    <p>{duration_or_season}</p>
                </div>
            </div>
        </div>
    </div>
</div>
'''

def create_video_tiles_content(video, type):
    '''
    Returns a section of html for a video, built from a html template.

    video (obj): Either of Movie / TvShow obj
    type (str): type of video, 'movie', 'tvshow'
    '''
    content = ''

    # Extract the youtube ID from the url
    youtube_id_match = re.search(r'(?<=v=)[^&#]+', 
            video.trailer_youtube_url)

    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', video.trailer_youtube_url)

    trailer_youtube_id = (youtube_id_match.group(0) 
        if youtube_id_match else None)

    duration_or_season = get_duration_or_seasons(type, video.duration 
        if hasattr(video, 'duration') else video.seasons)

    # Append the tile for the video with its content filled in
    return video_tile_content.format(
        video_title=video.title,
        video_description=video.description,
        video_rating=video.rating,
        poster_image_url=video.poster_image_url,
        trailer_youtube_id=video.trailer_youtube_url,
        duration_or_season=duration_or_season
    )

def get_duration_or_seasons(type, value):
    '''
    Returns correct html for a giving video type.

    type (obj): Movie/TvShow class,
    value (integer): Movie duration or Number of seasons depending on obj.
    '''
    if type == 'movie':
        return '<strong>Duration:</strong> ' + str(value) + ' mins'
    elif type == 'tvshow':
        return '<strong>Seasons:</strong> ' + str(value)

    return ''


def open_page(videos):
    '''
    Receives movies and tv shows and write the html output to a file.
    '''

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    movies = '';
    tvshows = '';

    # Loop through videos passing it with the correct type.
    for video in videos:
        if video[1] == 'movie':
            movies += create_video_tiles_content(video[0], 'movie')
        elif video[1] == 'tvshow':
            tvshows += create_video_tiles_content(video[0], 'tvshow')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movies=movies,
        tvshows=tvshows,
    )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


office_space = Movie("Office Space",
    "Three company workers who hate their jobs decide to rebel against their "
    "greedy boss.", 
    VideoRating.R, 
    "http://www.gstatic.com/tv/thumb/movieposters/22554/p22554_p_v8_aa.jpg", 
    "https://www.youtube.com/embed/dMIrlP61Z9s?autoplay=1&html5=1",
    89
)

lego_movie = Movie(
    "The Lego Movie",
    "Armed with a super-suit with the astonishing ability to shrink in scale "
    "but increase in ...",
    VideoRating.PG, 
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4MDk1ODExN15BMl5Ban"
    "BnXkFtZTgwNzIyNjg3MDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg", 
    "https://www.youtube.com/embed/fZ_JOBCLF-I?autoplay=1&html5=1",
    100
)

ant_man = Movie(
    "Ant-Man",
    "An ordinary Lego construction worker, thought to be the prophesied 'Special'.", 
    VideoRating.PG13, 
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2NTQ5Mzc2M15BMl5Ban"
    "BnXkFtZTgwNTcxMDI2NTE@._V1_.jpg", 
    "https://www.youtube.com/embed/pWdKf3MneyI?autoplay=1&html5=1",
    117
)

seinfeld = TvShow(
    "Seinfeld",
    "The continuing misadventures of neurotic New York stand-up comedian Jerry "
    "Seinfeld.", 
    VideoRating.PG13, 
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2MDYyNDYyNl5BMl5Ban"
    "BnXkFtZTgwNDQ4OTkwMDE@._V1._CR11,1,316,470_.jpg", 
    "https://www.youtube.com/embed/vKWYg9qFOpA?autoplay=1&html5=1",
    9
)

video_list = [
    [office_space, 'movie'],
    [lego_movie, 'movie'],
    [ant_man, 'movie'],
    [seinfeld, 'tvshow']
]

open_page(video_list)
