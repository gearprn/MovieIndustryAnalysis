"""
    Movie Industry Analysis
    Chart: Mean Budget Type
"""
import pygal, numpy, pandas
def main():
    """ creat chart """
    typ = []
    data_frame = pandas.read_csv("movies.csv", encoding = "utf-8")
    genre_grouped = data_frame.groupby('genre')
    budget_data = genre_grouped.mean()

    for i in range(6819):
        if data_frame["genre"][i] not in typ:
            typ.append(data_frame["genre"][i])
    typ = sorted(typ)
    print(typ)
    print(budget_data)
    chart = pygal.Bar()
    chart.title = "Average Budget"


    for i in range(17):
        chart.add(typ[i], budget_data["budget"][i])

    chart.render_to_file('avr_budget.svg')

main()
