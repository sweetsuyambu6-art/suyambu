import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt




filter_package = st.set_page_config(page_title="stock value", page_icon="📈",layout="wide")
df= pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\_csv\unique_tickers.csv")
df1 = pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\_csv\Sector_data - Sheet1.csv")
df2 = pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\_csv\combined2_data.csv")

#green stock*red stock
st.subheader("Top & Downfalling Stocks ")    
col1,col2=st.columns(2)
with col1:
  st.title('Top gaining')
  top= df2.groupby(['Ticker',"month"])[["open","high","volume","close"]].max().sort_values(by="close", ascending=False)
  close_price=df2['close'].sum()
  price_return=df2['close']-df2['close']/df2['close']
  st.dataframe(top)
with col2:
  st.title('Downfall Lossing')
  close_price=df2['close'].sum()
  price_return=df2['close']-df2['close']/df2['close']
  downfall = df2.groupby(['Ticker',"month"])[["open","high","volume","close"]].min().sort_values(by="close", ascending=True)
  st.dataframe(downfall)

#sector select
st.header("Sector Wise Company")
selected_sector = st.selectbox("Select Sector", ["ALUMINIUM", "AUTOMOBILES", "BANKING", 
                                                 'CEMENT', 'DEFENCE', 'ENERGY',
                                                 'ENGINEERING', 'FINANCE', 'FMCG', 'FOOD & TOBACCO',
                                                 'INSURANCE', 'MINING', 'MISCELLANEOUS',
                                                 'PAINTS', 'PHARMACEUTICALS', 'POWER', 'RETAILING',
                                                  'SOFTWARE', 'STEEL', 'TELECOM','TEXTILES'])
if selected_sector:
  filtered_df = df1[df1['sector'].isin([selected_sector])]
  st.subheader(f"Data for {selected_sector} Sector")
  st.dataframe(filtered_df) 
  st.subheader(f"Stock Price Trends for {selected_sector} Sector")
 
#name replace it of ticker for mapping 
col1, col2 = st.columns(2)
with col1:
  return_price = (df2['close'].max() - df2['close'].min())
  selected = df[df['Ticker'].isin(filtered_df['COMPANY'])]
  fig = px.bar(selected, x='date', y='close', color='Ticker', title=f'{selected_sector} Sector Stock Price Trends')
  st.plotly_chart(fig)

with col2:
  return_price = (df['close'].max() - df['close'].min())
  selected = df[df['Ticker'].isin(filtered_df['COMPANY'])]
  fig = px.scatter(selected, y='close', x='date',color="close",color_continuous_scale="reds",title=f'{selected_sector} Sector Stock Price Trends')
  st.plotly_chart(fig)


#dataframe table
st.columns(2)
column1, column2 = st.columns(2)
#corr
with column1:
    st.title('Define a custom')
    df2=pd.DataFrame.corr(df2,numeric_only=True)
    plt=sns.heatmap(df2,cmap="coolwarm",annot=True,fmt=".2f",linewidths=.5)
    st.pyplot()
#return_price   
with column2:
  filtered_df2 = df[df['Ticker'].isin(filtered_df['COMPANY'])]
  filtered_df2['return_price'] = (filtered_df2['close'] - filtered_df2['close'].shift(1)) / filtered_df2['close'].shift(1)
  st.dataframe(filtered_df2[['Ticker','close','date', 'return_price']])

