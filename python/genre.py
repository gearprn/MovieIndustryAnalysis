"""
    Movie Industry Analysis
    Chart: Genre
"""

import pandas, pygal

def main():
    """ create chart """
    data_frame = pandas.read_csv("movies.csv", encoding = "utf-8")

    genre_dict = {}
    for i in range(6819):
        if data_frame["genre"][i] not in genre_dict:
            genre_dict[data_frame["genre"][i]] = 1
        else:
            genre_dict[data_frame["genre"][i]] += 1

    genre_dict = dict(sorted(genre_dict.items(), key=lambda x: x[1]))

    bar_chart = pygal.Bar()
    bar_chart.title = "Total movies in each genre from 1986 to 2016"

    for i in genre_dict:
        bar_chart.add(i, genre_dict[i])

    bar_chart.legend_at_bottom = True
    bar_chart.legend_box_size = 16

    bar_chart.render_to_file('genre_chart.svg')

main()
