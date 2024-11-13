import yfinance as yf
import plotly.graph_objs as go

# Download GameStop stock data
gamestop_data = yf.download("GME", start="2020-01-01", end="2023-01-01")

# Sample GameStop revenue data (replace this with actual scraped data)
gamestop_revenue = [6.45, 8.43, 10.35, 14.72]  # Example values in billions
revenue_dates = ["2020", "2021", "2022", "2023"]  # Example revenue years

# Create a Plotly figure for GameStop stock and revenue
fig = go.Figure()

# GameStop stock price chart
fig.add_trace(go.Scatter(x=gamestop_data.index, y=gamestop_data['Close'], name="GameStop Stock Price"))

# GameStop revenue bar chart (replace this with actual scraped revenue)
fig.add_trace(go.Bar(x=revenue_dates, y=gamestop_revenue, name="GameStop Revenue"))

# Update layout
fig.update_layout(title="GameStop Stock Price and Revenue",
                  xaxis_title="Date/Year",
                  yaxis_title="Value in $B",
                  barmode='group')

fig.show()
