"""Draw pandas/matplotlib plots and replicate them in: 
    - seaborn
    - bokeh
    - plot.ly - TODO: seems not installed with current conda
    - (ggplot)
    - (altair)
   
Data: OIL_AVG and USD_AVG time sereis in <rub_oil.txt>, 2007-2016    

Main reference:
    - <http://pbpython.com/visualization-tools-1.html>
See also:     
    - <https://dansaber.wordpress.com/2016/10/02/a-dramatic-tour-*through-pythons-data-visualization-landscape-including-ggplot-and-altair/>
"""

"""
TODO:    
    - front-end "dashboard"    
    - html wrapper for pandas png plots
    
NOT TODO:
    - standalone seaborn
    - seaborn formatting for plt/pd as in datachamp course
"""

import pandas as pd
import bokeh.charts as bc
import matplotlib as plt

# import data
FILE = dict(filepath_or_buffer = "rub_oil.txt", sep = "\t", 
            decimal = ",", index_col = 0)
df = pd.read_csv(**FILE)

#plot and axis names
plot_title = "Oil vs ruble, 2007-2016"
x_axis_name = "Oil price, USD/b"
y_axis_name = "Exchange rate, RUB/USD"

###############################################################################
#
#    Pandas/matplotlib with seaborn formatting
#
###############################################################################

plt.style.use('seaborn-darkgrid')

# draw time series
time1 = df.plot()
time1.set_xlabel("Year")
# Q4: how do I control labels order - which label is for which line
time1.legend([x_axis_name, y_axis_name], loc=2)


scatter1 = df.plot.scatter(x='OIL_AVG', y='USD_AVG')
# Q1: can I pass xlabel and ylabel as 
scatter1.set_xlabel(x_axis_name)
scatter1.set_ylabel(y_axis_name)
# --- end Q1

scatter1.set_title(plot_title)

fig = scatter1.get_figure()
fig.savefig("rub_oil_pandas.png")

###############################################################################
#
#    Bokeh
#
###############################################################################

p = bc.Scatter(df, x='OIL_AVG', y='USD_AVG', title="Oil vs ruble, 2007-2016",
               xlabel=x_axis_name , ylabel="Exchange rate, RUB/USD")
bc.output_file("scatter.html")
#bc.show(p)

#Q2: save bokeh chart as local file

#Q3: can I preview it inline in SPYDER console?

#Comment: in scatter.html same distance has different pixel length - 
#    x axis is condensed, y axis is enlarged. can a bokeh chart 
#    be similar to pandas, where length in pixels is same on x and y axis?
#    Answer: this is a long-standing and open issue for bokeh:
#            https://github.com/bokeh/bokeh/issues/474


   

