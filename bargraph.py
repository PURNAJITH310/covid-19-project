import pandas as pd
import plotly.express as px


df=pd.read_csv('data.csv')
fig=px.bargraph(df,x="date",y="no of cases",color="Country",size="Percentage",size_max=60)
fig.show()
