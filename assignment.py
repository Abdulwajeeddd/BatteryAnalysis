#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


df=pd.read_csv('D:/Battery_Dataset/cleaned_dataset/metadata.csv')


# In[3]:


df.head()


# In[4]:


impedance_data = df[(df['type'] == 'impedance') & df[['Re', 'Rct']].notna().all(axis=1)]


# In[5]:


impedance_data = impedance_data.sort_values(by='start_time')


# In[19]:


import plotly.express as px  # Importing Plotly Express to help create interactive plots

# Now, we're going to create a line plot using the data from 'impedance_data'
fig1 = px.line(
    impedance_data,       # This is the DataFrame with our data (it should have columns 'start_time' and 'Re')
    x='start_time',       # The x-axis will represent the time, so we use the 'start_time' column from the DataFrame
    y='Re',               # The y-axis will show the electrolyte resistance, so we use the 'Re' column
    title='Electrolyte Resistance (Re) vs Time',  # Here we set the title of the plot to something descriptive
    labels={              # We want to make the axis labels a bit more readable
        'start_time': 'Time',  # Renaming the 'start_time' column to 'Time' for clarity on the x-axis
        'Re': 'Electrolyte Resistance (Ohms)'  # Giving the y-axis a more descriptive label
    }
)

# This command displays the plot in an interactive format so we can view it
fig1.show()


# In[7]:


# We’re going to create a line plot showing how the 'Charge Transfer Resistance (Rct)' changes over time
fig2 = px.line(
    impedance_data,       # Using the 'impedance_data' DataFrame, which contains the 'Rct' column
    x='start_time',       # The x-axis will represent time, coming from the 'start_time' column
    y='Rct',              # The y-axis will show the charge transfer resistance (Rct) over time
    title='Charge Transfer Resistance (Rct) vs Time',  # Giving the plot a clear title
    labels={              # Customizing the axis labels for better clarity
        'start_time': 'Time',  # Renaming the x-axis to 'Time' for easy understanding
        'Rct': 'Charge Transfer Resistance (Ohms)'  # Renaming the y-axis to specify tha


# In[8]:


# First, let's calculate the 'Battery_Impedance' by adding 'Re' (electrolyte resistance) and 'Rct' (charge transfer resistance)
impedance_data['Battery_Impedance'] = impedance_data['Re'] + impedance_data['Rct']

# Now, we’ll create a line plot to show how the 'Battery_Impedance' changes over time
fig3 = px.line(
    impedance_data,       # Using the 'impedance_data' DataFrame, which now has the 'Battery_Impedance' column
    x='start_time',       # The x-axis will represent time, which comes from the 'start_time' column
    y='Battery_Impedance',  # The y-axis will represent the battery impedance (the sum of 'Re' and 'Rct')
    title='Battery Impedance (Re + Rct) vs Time',  # Giving the plot a title that explains exactly what we're looking at
    labels={              # Customizing the axis labels for better clarity
        'start_time': 'Time',  # Renaming the x-axis label to 'Time' for simplicity
        'Battery_Impedance': 'Battery Impedance (Ohms)


# In[9]:


fig_combined = go.Figure()


# In[20]:


# We're adding traces (lines) to the combined figure, each representing different types of resistance

# Add a trace for Electrolyte Resistance (Re) over time
fig_combined.add_trace(go.Scatter(
    x=impedance_data['start_time'],  # The x-axis is 'start_time', which is the time data
    y=impedance_data['Re'],          # The y-axis is 'Re', which represents electrolyte resistance
    mode='lines',                    # We want to plot it as a line
    name='Electrolyte Resistance (Re)'  # Name the trace for the legend
))

# Add a trace for Charge Transfer Resistance (Rct) over time
fig_combined.add_trace(go.Scatter(
    x=impedance_data['start_time'],  # The x-axis is again 'start_time'
    y=impedance_data['Rct'],         # The y-axis is 'Rct', which represents charge transfer resistance
    mode='lines',                    # Plot this as a line too
    name='Charge Transfer Resistance (Rct)'  # Name it for the legend
))

# Add a trace for Battery Impedance (Re + Rct) over time
fig_combined.add_trace(go.Scatter(
    x=impedance_data['start_time'],  # The x-axis is still 'start_time'
    y=impedance_data['Battery_Impedance'],  # The y-axis is 'Battery_Impedance', the sum of 'Re' and 'Rct'
    mode='lines',                    # We plot it as a line as well
    name='Battery Impedance (Re + Rct)'  # Give this trace a name for the legend
))

# At this point, we have added three different lines (traces) for three different types of resistance to our figure.


# In[11]:


fig_combined.update_layout(
    title='Battery Parameters Over Time',
    xaxis_title='Time',
    yaxis_title='Values (Ohms)',
    legend=dict(x=0, y=1, traceorder='normal')
)
fig_combined.show()


# In[ ]:




