#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Normal.py

Assesses normalcy of data

__author__ = Anita Cheung
__copyright__ = Copyright 2021
__version__ = 1.0
__maintainer__ = Anita Cheung
__status__ = Dev
"""

import pandas as pd
import numpy as np
import datetime as date
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns
import dash
import plotly.express as px

class Normal:

    def __init__(self, pathname):
        """Constructor"""
        self.pathname = pathname
        self.df = pd.read_csv(pathname)

    def visual(self, x, title=None, show=True):
        app = dash.Dash(__name__)
        app.layout = html.Div([
            dcc.Graph(id="graph"),
            tml.P("Mean:"),
            dcc.Slider(id="mean")
        fig = px.histogram(self.df, x=x)
        fig.update_layout(bargap=0.2)
        if show:
            fig.show()
        else:
            self.output(fig, title)       

    def output(self, fig, title):
        directory = os.path.dirname(self.pathname)
        fig.savefig(directory + '/' + title + '.png')
        plt.clf()
    
    def information(self):
        """Get information"""
        description = "Symmetric curve that adheres to the central limit effect"
        print(description)

def main():
   pass

if __name__ == '__main__':
    main()