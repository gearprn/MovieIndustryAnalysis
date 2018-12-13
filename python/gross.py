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

    gross_dict = dict(sorted(gross_dict.items(), key=lambda x: int(x[1])))

    bar_chart = pygal.Bar()
    bar_chart.title = "Total gross in each gross from 1986-2016 (in million)"

    for i in gross_dict:
        bar_chart.add(i, [{"value": int(gross_dict[i][:len(gross_dict[i])-6]), "label": "in million" }])

    bar_chart.legend_at_bottom = True
    bar_chart.legend_box_size = 20

    bar_chart.render_to_file('gross_chart.svg')

main()
