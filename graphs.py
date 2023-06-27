import pandas as pd
import plotly.express as px
import numpy

url = 'https://raw.githubusercontent.com/ssuni2/nba_data_csv/main/nba_advanced.csv'
df = pd.read_csv(url)

# Total Wins Graph
ddf = df.drop_duplicates(subset=['Visitor'])

fig = px.bar(ddf, x = 'Visitor', y = 'Visitor_W', labels={'Visitor':'Team', 'Visitor_W':'Number of Wins in 2022-23 Season'}, title='Total Wins By Team (2022-23)')
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

fig.write_html('total_wins_graph.html')

