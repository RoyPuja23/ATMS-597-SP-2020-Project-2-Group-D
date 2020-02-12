# Object to use user-input "avg_period" and "lineplot" options to generate Climate Stripes
# Options of "avg_period" : Y for yearly, M for Monthly and W for Weekly
# Options of "lineplot" : Yes for Yes and No for No

def extract_data(avg_period,lineplot):

  h=download_data(station_id,"1930-01-01","1931-01-01", Token) # ** Need to generalize the begin and end date **
  h['Mean Temp'] = h.mean(axis=1) # Add an extra column for mean daily temperature
  
  # Following are the subset dataframes for the three different time average periods.
  Yearly_MeanT = [] 
  Monthly_MeanT = []
  Weekly_MeanT = []

  if avg_period==Y:
    # Display mean temperature of the year
    Yearly_MeanT = h.groupby(pd.Grouper(key='date', freq='Y')).mean()
    
    #Insert plotting code here for Climate Stripes with "Mean Temp" column vs time for this case.
    if lineplot == Yes:
      #Insert plotting code for a *line plot* here for the "Mean Temp" column vs time for this case.
    else:
       print('Please input Yes if you want to plot the line plot')
  elif avg_period==M:
    # Display mean temperature of every month of the year
    Monthly_MeanT = h.groupby(pd.Grouper(key='date', freq='M')).mean()
    #Insert plotting code here for Climate Stripes with "Mean Temp" column vs time for this case.
    if lineplot == Yes:
      #Insert plotting code here for the "Mean Temp" column vs time for each case.
  elif avg_period==W: 
    # Display mean temperature of every week of the year
    Weekly_MeanT = h.groupby(pd.Grouper(key='date', freq='W')).mean()
    #Insert plotting code here for Climate Stripes with "Mean Temp" column vs time for this case.
    if lineplot == Yes:
      #Insert plotting code here for the "Mean Temp" column vs time for each case.

  return none  

