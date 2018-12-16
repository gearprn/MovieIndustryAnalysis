"""
    Movie Industry Analysis
    Chart: Mean Budget Type
"""
import pygal, numpy, pandas
def main():
    """ creat chart """
    data_frame = pandas.read_csv("movies.csv", encoding = "utf-8")
    genre_grouped = data_frame.groupby('genre').mean()
    
    typ = []
    for i in range(6819):
        if data_frame["genre"][i] not in typ:
            typ.append(data_frame["genre"][i])
    typ = sorted(typ)

    chart = pygal.HorizontalBar()
    chart.title = "Average Budget"

    for i in range(17):
        chart.add(typ[i], genre_grouped["budget"][i])
    
    chart.legend_at_bottom = True
    chart.legend_box_size = 16
    chart.render_to_file('avr_budget.svg')

main()
