import justpy as jp

def app():
    # webpage
    wp = jp.QuasarPage()
    # heading
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    # paragraph
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis.")
    # highchart
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Rating by Day"

    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])

    return wp

jp.justpy(app)