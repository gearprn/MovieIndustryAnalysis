"""
    Movie Industry Analysis
    Chart: gross
"""

import pandas, pygal

def main():
    """ create chart for gross """
    data_frame = pandas.read_csv("movies.csv", encoding = "utf-8")
    grouped = data_frame.groupby("genre")

    gross_dict = {}
    for genre, gross_data_frame in grouped:
        gross_dict[genre] = str(gross_data_frame.sum()[5])

    chart = pygal.Bar()
    chart.title = "Total gross in each genre from 1986-2016 (in million)"
    chart.x_title = 'genre'
    chart.y_title = 'sales (in millions)'
    chart.y_labels = range(0, 75001)
    chart.y_labels_major_count = 6
    chart.show_minor_y_labels = False

    for i in gross_dict:
        chart.add(i, [{"value": int(gross_dict[i][:len(gross_dict[i])-6]), "label": "in million" }])

    chart.legend_at_bottom = True
    chart.legend_box_size = 20

    chart.render_to_file('gross_chart.svg')

main()
