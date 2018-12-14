""" MOVIE ANALYSIS """
import pandas, pygal
def main():
    """ chart: country """
    data_frame = pandas.read_csv("movies.csv", encoding="utf-8")
    comp_dict = {}

    movie_chart = pygal.Treemap()
    movie_chart.title = "Where most movie from?"

    for i in range(6819):
        if data_frame["company"][i] not in comp_dict:
            comp_dict[data_frame["company"][i]] = 1
        else:
            comp_dict[data_frame["company"][i]] += 1

    for i in comp_dict:
        movie_chart.add(i, comp_dict[i])
    movie_chart.render_to_file("country_chart.svg")
main()
