"""
    Movie Industry Analysis
    Chart: Movie Trend
"""

import pandas, pygal

def main():
    """ create chart for movie trend """
    data_frame = pandas.read_csv("movies.csv", encoding = "utf-8")

    genres = ["Action", "Adventure", "Animation", "Biography", "Comedy",
                 "Crime", "Drama", "Family", "Fantasy", "Horror", "Musical",
                 "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]

    chart = pygal.Line(interpolate='cubic', dots_size=1.75)
    chart.title = "Movie trend from 1986 to 2016"
    chart.x_labels = range(1986, 2017)
    chart.x_title = 'years'
    chart.y_title = 'amount'
    chart.x_labels_major_count = 5
    chart.show_minor_x_labels = False
    chart.y_labels = [i for i in range(0, 101, 20)]
    chart.y_labels_major_every = 5
    chart.truncate_label = 5
    chart.legend_at_bottom = True
    chart.legend_box_size = 16

    for genre in genres:
        count = []
        for year in range(1986, 2017):
            count_num = 0
            for i in range(6819):
               if int(data_frame["year"][i]) == year and data_frame["genre"][i] == genre:
                count_num += 1
            count.append(count_num)
        chart.add(genre, count)

    chart.render_to_file("trend_genre_line.svg")

main()
