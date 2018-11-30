"""
    Movie Industry Analysis
    Chart: Rating
"""

import pandas, pygal

def main():
    """ create chart for genre """
    data_frame = pandas.read_csv("movies.csv", encoding = "utf-8")

    rating_dict = {}
    for i in range(6819):
        if data_frame["rating"][i] not in rating_dict:
            rating_dict[data_frame["rating"][i]] = 1
        else:
            rating_dict[data_frame["rating"][i]] += 1

    rating_dict = dict(sorted(rating_dict.items(), key=lambda x: x[1]))

    bar_chart = pygal.Pie()
    bar_chart.title = "Total rating from 1986 to 2016"

    for i in rating_dict:
        bar_chart.add(i, int((int(rating_dict[i])/6820*100)*100)/100)

    bar_chart.legend_at_bottom = True
    bar_chart.legend_box_size = 16

    bar_chart.render_to_file('rating_chart.svg')

main()
