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

    chart = pygal.Bar()
    chart.title = "Average budget for each genre"
    chart.x_title = 'amount (in millions)'
    chart.y_title = 'genre'
    chart.y_labels = range(0, 71)
    chart.y_labels_major_count = 8
    chart.show_minor_y_labels = False

    for i in range(17):
        if int(genre_grouped["budget"][i]) != 0:
            value = str(int(genre_grouped["budget"][i]))
            value = value[:len(value)-6]
        else:
            value = 0
        chart.add(typ[i], [{"value": int(value), "label": "In million"}] )
    
    chart.legend_at_bottom = True
    chart.legend_box_size = 16
    chart.render_to_file('avr_budget_chart.svg')

main()
