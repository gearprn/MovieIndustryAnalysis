""" 
    MOVIE ANALYSIS
    chart : country
"""
import pandas, pygal
def main():
    """ chart: country """
    data_frame = pandas.read_csv("movies.csv", encoding="utf-8")
    country_grouped = data_frame.groupby('country')

    country_dict = {}

    for country, country_data_frame in country_grouped:
        country_dict[country] = country_data_frame.count()[2]

    country_dict = dict(sorted(country_dict.items(), key=lambda x :x[1]))

    pie_chart = pygal.Pie()
    pie_chart.title = "Where most movies from?"

    for i in list(country_dict)[-1:-6:-1]:
        pie_chart.add(i, [{"value": country_dict[i], "label": "%.2f"%(country_dict[i]/6820*100) + "%"}])

    pie_chart.legend_at_bottom = True
    pie_chart.legend_box_size = 16
    pie_chart.render_to_file('country_chart.svg')

main()
