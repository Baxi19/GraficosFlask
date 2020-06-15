
import pygal as pygal

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/grafico1/')
def grafico1():
    try:
        graph = pygal.Line()
        graph.title = '% Change Coolness of programming languages over time.'   #Titulo del grafico
        graph.x_labels = ['2011','2012','2013','2014','2015','2016']            #valores del eje X
        graph.add('Python',  [15, 31, 89, 200, 356, 900])                       #Valores que se evaluaran, seria hacer un SELECT a los datos de la BD
        graph.add('Java',    [15, 45, 76, 80,  91,  95])
        graph.add('C++',     [5,  51, 54, 102, 150, 201])
        graph.add('All others combined!',  [5, 15, 21, 55, 92, 105])
        graph_data = graph.render_data_uri()
        return render_template("graphing.html", graph_data = graph_data)
    except Exception as e:
        return(str(e))


@app.route('/grafico2/')
def grafico2():
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Browser usage in February 2012 (in %)'
    line_chart.add('IE', 19.5)
    line_chart.add('Firefox', 36.6)
    line_chart.add('Chrome', 36.3)
    line_chart.add('Safari', 4.5)
    line_chart.add('Opera', 2.3)
    return line_chart.render()



@app.route('/grafico3/')
def grafico3():
    radar_chart = pygal.Radar()
    radar_chart.title = 'V8 benchmark results'
    radar_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    radar_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
    radar_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
    radar_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
    radar_chart.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
    radar_chart.add('Item', [10])
    return radar_chart.render()


@app.route('/grafico4/')
def grafico4():
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    pie_chart.add('IE', 19.5)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)
    return pie_chart.render()



@app.route('/')
def hello_world():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
    return 'Hello, World!'


