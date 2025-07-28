# The ideia of this program is to try a little more of functions. Here, we'll emulate a library app.

import pandas as pd
import numpy as np


# Create dataframes to store data for a fictional library:

book_data = pd.DataFrame(columns=["id", "title", "author_id", "publication_date", "genre_id", "language"])
author_data = pd.DataFrame(columns=["id", "name", "dt_birth", "country", "main_genre", "main_language"])
genre_data = pd.DataFrame(columns=["id", "name"])

# Create functions to insert data into the dataframes.

def add_book(id, title, author_id, publication_date, genre_id, language):
    title = input("What's the title of the book?")
    author_id = input("What's the title of the book?")
    publication_date = input("What's the title of the book?")
    genre_id = input("What's the title of the book?")
    language = input("What's the title of the book?")
    return
