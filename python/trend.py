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

    line_chart = pygal.Line(interpolate='cubic', dots_size=1.75)
    line_chart.title = "Movie Trend from 1986 to 2016"
    line_chart.x_labels = range(1986, 2017)
    line_chart.x_labels_major_count = 5
    line_chart.show_minor_x_labels = False
    line_chart.y_labels = [i for i in range(0, 101, 20)]
    line_chart.y_labels_major_every = 5
    line_chart.truncate_label = 5
    line_chart.legend_at_bottom = True
    line_chart.legend_box_size = 16

    for genre in genres:
        count = []
        for year in range(1986, 2017):
            count_num = 0
            for i in range(6819):
               if int(data_frame["year"][i]) == year and data_frame["genre"][i] == genre:
                count_num += 1
            count.append(count_num)
        print(genre, count)
        line_chart.add(genre, count)

    line_chart.render_to_file("trend_genre_line.svg")

main()
