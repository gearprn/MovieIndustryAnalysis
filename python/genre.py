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

    chart = pygal.Bar()
    chart.title = "Total movies in each genre from 1986 to 2016"
    chart.x_title = 'genre'
    chart.y_title = 'amount'
    chart.y_labels = range(0, 2101)
    chart.y_labels_major_count = 8
    chart.show_minor_y_labels = False

    for i in genre_amount:
        chart.add(i, [{'value': genre_amount[i], 'label': "%.2f"%(genre_amount[i]/6820*100) + "%"}])

    chart.legend_at_bottom = True
    chart.legend_box_size = 16
    chart.render_to_file('genre_chart.svg')

main()
