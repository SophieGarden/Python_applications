import justpy as jp
import pandas as pd
from pytz import utc
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('reviews.csv', parse_dates=['Timestamp'])
df['month'] = df.Timestamp.dt.strftime('%Y-%m')
df_by_course_month = df.groupby(['month', 'Course Name']).Rating.mean().unstack()

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average rating during one month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Review', classes = 'text-h1 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analysis')

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = 'Average Rating by Month'
    hc.options.xAxis.categories = list(df_by_course_month.index)
    hc.options.series = [ {'name': x, 'data': df_by_course_month[x].to_list()} for x in df_by_course_month.columns]

    return wp

jp.justpy(app)
