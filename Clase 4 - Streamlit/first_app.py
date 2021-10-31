
import streamlit as st
import numpy as np
import pandas as pd

st.title('This is mu first app from Galileo Master!')

x = 4
st.write(x, ' square is ', x*x)

st.write('this is a data frame example')

st.write(pd.DataFrame({
    'Column A': ['A', 'B', 'C', 'D', 'E'],
    'Column B': [1, 2, 3, 4, 5]
}))

df = pd.DataFrame({
    'Column A': ['A', 'B', 'C', 'D', 'E'],
    'Column B': [1, 2, 3, 4, 5]
})


"""
## Show me some graphs
"""
df_to_plot = pd.DataFrame(
    np.random.rand(20, 3), columns=['Column A', 'Column B', 'Column C']
)

st.line_chart(df_to_plot)

"""
## Let's plot a map!
"""

df_lan_lon = pd.DataFrame(
    np.random.rand(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(df_lan_lon)

if st.checkbox('show data frame'):
    df_lan_lon

"""
## Let's try some widgets
### 1. Slider
"""

x = st.slider('Select a value for X', min_value=1, max_value=100, value=4)
y = st.slider('Select power for X', min_value=0, max_value=4, value=2)

st.write(x, ' ^ ',  y, x**y)

"""
### What about options
"""

def test():
    st.write('Function Executed: ')

option_list = range(1, 10)

option = st.selectbox('Which number do you like best?', option_list, on_change=test)



st.write('your favorite numver is: ', option)

"""
## How about a progress bar
"""

import time

label = st.empty()

progress_bar = st.progress(0)

for i in range(0, 101):
    label.text(f'The value is:  {i}%')
    progress_bar.progress(i)
    time.sleep(0.02)

'This wait is done'


st.sidebar.write('This is a sidebar')

option_side = st.sidebar.selectbox('Select a side number', option_list)
st.sidebar.write('The selection is: ', option_side)

st.sidebar.write('Another Slider')

another_slider = st.sidebar.slider('Select Range', 0.0, 100.0, (25.0, 75.0))

st.sidebar.write('the element selected is ', another_slider)
