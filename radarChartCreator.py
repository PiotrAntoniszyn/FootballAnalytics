import streamlit as st
import time 
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from mplsoccer.pitch import Pitch
import seaborn as sns
from soccerplots.radar_chart import Radar
from soccerplots.utils import add_image
import ipywidgets as widgets
import sys
from bs4 import BeautifulSoup, Comment
import lxml.html as lh


url = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

table = BeautifulSoup(soup.select_one('#all_stats_standard').find_next(text=lambda x: isinstance(x, Comment)), 'html.parser')

tds=[]
for tr in table.select('tr:has(td)'):
    tdx = [td.get_text(strip=True) for td in tr.select('td')]
    tds.append(tdx)
df = pd.DataFrame(tds)
df[df.columns[10:31]]=df[df.columns[10:31]].apply(pd.to_numeric, axis=1)
legend = {0:'Player',1:'Nation',2:'Pos',3:'Squad',4:'Age',5:'Born',6:'MP',7:'Starts',8:'Min',9:'90s',10:'Goals',11:'Assists',12:'Non-penalty goals',13:'Penalty goals',14:'Penalty attempts',15:'Yellow cards',16:'Red cards',17:'Gls/90',18:'Ast/90',19:'G+A/90',20:'Non-penalty goals/90',21:'G+A-PK/90',22:'xG',23:'npxG',24:'xA',25:'npxG+xA',26:'xG/90',27:'xA/90',28:'xG+xA/90',29:'npxG/90',30:'npxG+xA/90',31:'Matches'}

df = df.rename(columns=dict(legend))
df['Min'] = df['Min'].str.replace(',', '').astype(float)
st.title('Premier League 20/21 Radar Chart Creator by P.A.')


col1, col2, col3 = st.beta_columns(3)

with col1:
	st.header("Database")
	st.dataframe(df)
	categories = st.multiselect('Choose categories',list(df.columns[10:31]),list(df.columns[10:13]))

	player1 = st.selectbox("Player 1:",options=list(df['Player'].sort_values(ascending=True)) )
	player2 = st.selectbox("Player 2:",options=list(df['Player'].sort_values(ascending=True)) )

	







#categories = st.multiselect('Choose categories',list(df.columns[10:31]),list(df.columns[10:13]))

#player1 = st.selectbox("Player 1:",options=list(df['Player'].sort_values(ascending=True)) )
#player2 = st.selectbox("Player 2:",options=list(df['Player'].sort_values(ascending=True)) )




valuerange=[]

for x in categories:
    #df[x] = df[x].astype('float64',errors='ignore')
    valuerange.append((min(df[df['Min']>300][x]),max(df[df['Min']>300][x])*1.1))


radar = Radar(background_color="#0E1117", patch_color="#535353", label_color="#FFFFFF",
              range_color="#FFFFFF")


title = dict(
    title_name=str(df.iloc[df[df['Player'].str.contains(player1)==True].index[0]]['Player']).split('\\')[0],
    title_color='#B6282F',
    subtitle_name=str(df.iloc[df[df['Player'].str.contains(player1)==True].index[0]]['Min']) + ' minutes',
    subtitle_color='#B6282F',
    title_name_2=str(df.iloc[df[df['Player'].str.contains(player2)==True].index[0]]['Player']).split('\\')[0],
    title_color_2='#344D94',
    subtitle_name_2=str(df.iloc[df[df['Player'].str.contains(player2)==True].index[0]]['Min']) + ' minutes',
    subtitle_color_2='#344D94',
    title_fontsize=18,                ## fontsize for left-title
    subtitle_fontsize=15,             ## fontsize for left-subtitle
    title_fontsize_2=18,              ## fontsize for right-title
    subtitle_fontsize_2=15            ## fontsize for right-subtitle
)


## endnote 
endnote = "Visualization made by:@PiotrAntoniszyn\nData from fbref.com"
end_color = 'blue'
## plot radar
fig, ax = radar.plot_radar(ranges=valuerange, params=categories, values=[df.iloc[df[df['Player'].str.contains(player1)==True].index[0]][categories],df.iloc[df[df['Player'].str.contains(player2)==True].index[0]][categories]], 
                                 radar_color=['#B6282F', '#313C96'],title=title,compare=True,endnote=endnote,end_color='#313C96',end_size=12)
#st.write(fig)

with col2:
	st.header("Chart")
	st.write(fig)
