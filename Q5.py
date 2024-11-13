import yfinance as yf
import plotly.graph_objs as go

# Download Tesla stock data
tesla_data = yf.download("TSLA", start="2020-01-01", end="2023-01-01")

# Sample revenue data (replace this with actual scraped data)
tesla_revenue = [31.53, 34.33, 37.24, 53.85]  # Example values in billions
revenue_dates = ["2020", "2021", "2022", "2023"]  # Example revenue years

# Create a Plotly figure for Tesla stock and revenue
fig = go.Figure()

# Tesla stock price chart
fig.add_trace(go.Scatter(x=tesla_data.index, y=tesla_data['Close'], name="Tesla Stock Price"))

# Tesla revenue bar chart (you could replace this with actual scraped revenue)
fig.add_trace(go.Bar(x=revenue_dates, y=tesla_revenue, name="Tesla Revenue"))

# Update layout
fig.update_layout(title="Tesla Stock Price and Revenue",
                  xaxis_title="Date/Year",
                  yaxis_title="Value in $B",
                  barmode='group')

fig.show()
