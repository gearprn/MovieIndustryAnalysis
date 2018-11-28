"""
    Movie Industry Analysis
    Chart: gross
"""

import pandas, pygal

def main():
    """ create chart for gross """
    data_frame = pandas.read_csv("movies.csv", encoding = "utf-8")

    gross_dict = {}

    for i in range(6819):
        if data_frame["genre"][i] not in gross_dict:
            gross_dict["%s"%(data_frame["genre"][i])] = int(data_frame["gross"][i])
        else:
            gross_dict["%s"%(data_frame["genre"][i])] += int(data_frame["gross"][i])

    gross_dict = dict(sorted(gross_dict.items(), key=lambda x: x[1]))

    for i in gross_dict:
        gross_dict[i] = str(gross_dict[i])
        gross_dict[i] = gross_dict[i][:len(gross_dict[i])-6]
        gross_dict[i] = int(gross_dict[i])

    bar_chart = pygal.Bar()
    bar_chart.title = "Total gross in each gross from 1986-2016 (in million)"
    for i in gross_dict:
        bar_chart.add(i, [{"value":gross_dict[i], "lable":"in million" }])
    bar_chart.legend_at_bottom = True
    bar_chart.legend_box_size = 16

    bar_chart.render_to_file('gross_chart.svg')

main()
