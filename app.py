# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:36:00 2022

@author: DCHELD
"""

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

