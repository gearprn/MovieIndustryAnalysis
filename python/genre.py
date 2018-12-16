"""
    Movie Industry Analysis
    Chart: Genre
"""

import pandas, pygal

def main():
    """ create chart """
    data_frame = pandas.read_csv("movies.csv", encoding = "utf-8")
    genre_grouped = data_frame.groupby('genre')

    genre_amount = {}
    for genre, genre_data_frame in genre_grouped:
        genre_amount[genre] = genre_data_frame.count()[3]

    genre_amount = dict(sorted(genre_amount.items(), key=lambda x: x[1]))

    bar_chart = pygal.Bar()
    bar_chart.title = "Total movies in each genre from 1986 to 2016"

    for i in genre_amount:
        bar_chart.add(i, [{'value': genre_amount[i], 'label': "%.2f"%(genre_amount[i]/6820*100) + "%"}])

    bar_chart.legend_at_bottom = True
    bar_chart.legend_box_size = 16
    bar_chart.render_to_file('genre_chart.svg')

main()
