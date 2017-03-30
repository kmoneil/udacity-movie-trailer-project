## Udacity Fresh Tomaters Project

Python program to add movies and tv shows and diaplay a html page showing clickable poster art to show youtube trailer.

### Create a Movie:

```python
ant_man = Movie(
    "Ant-Man",
    "An ordinary Lego construction worker, thought to be the prophesied 'Special'.", 
    VideoRating.PG13, 
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2NTQ5Mzc2M15BMl5BanBnXkFtZTgwNTcxMDI2NTE@._V1_.jpg", 
    "https://www.youtube.com/embed/pWdKf3MneyI?autoplay=1&html5=1",
    117
)
```

### Create a TV Show:

```python
seinfeld = TvShow(
    "Seinfeld",
    "The continuing misadventures of neurotic New York stand-up comedian Jerry "
    "Seinfeld.", 
    VideoRating.PG13, 
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2MDYyNDYyNl5BMl5BanBnXkFtZTgwNDQ4OTkwMDE@._V1._CR11,1,316,470_.jpg", 
    "https://www.youtube.com/embed/vKWYg9qFOpA?autoplay=1&html5=1",
    9
)
```

### Once you've created all the Movies and TV Shows, you'll need to add them to a list with the video type.

```python
videos = [
    [ant_man, 'movie'],
    [seinfield, 'tvshow'],
    ...
]
```

### Finally, pass video list to function: open_page(your_list)

```python

open_page(your_list)

```

## Running program from the Terminal
- Open and Edit fresh_tomatoes.py
- Add your custom movies and tv shows to the bottom
- Add your list of videos organized by video type
- Add open_page(your_list)
- Save file

In a Terminal window type:
```bash
$ python fresh_tomatoes.py
```

Your default browser will open with the html page that was rendered by python.

---

## credits:
- imdb.com for poster art.
- youtube.com for video trailers.
