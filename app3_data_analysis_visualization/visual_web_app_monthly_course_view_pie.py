import justpy as jp
import pandas as pd
from pytz import utc
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('reviews.csv', parse_dates=['Timestamp'])
df_by_course_overall_count = df.groupby(['Course Name']).Rating.count()

chart_def = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Review', classes = 'text-h1 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analysis')

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = 'share of course traffic'
    hc.options.xAxis.categories = list(df_by_course_overall_count.index)
    hc.options.series[0].data = [{'name': a, 'y': b} for a, b in zip(df_by_course_overall_count.index, df_by_course_overall_count)]

    return wp

jp.justpy(app)
