import justpy as jp
import pandas as pd
from pytz import utc
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('reviews.csv', parse_dates=['Timestamp'])
df['week'] = df.Timestamp.dt.strftime('%Y-%W')
df_week_average = df.groupby('week').mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Analysis by day'
    },
    subtitle: {
        text: 'Udemy course'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: 'Week of year'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: 0 - 5.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} week: {point.y} rating'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Review', classes = 'text-h1 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analysis')

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = 'Average Rating by Week'
    hc.options.xAxis.categories = list(df_week_average.index)
    hc.options.series[0].data = list(df_week_average.Rating)

    return wp

jp.justpy(app)
