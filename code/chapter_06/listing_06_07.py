# Listing 6.7: An interactive bar chart saved as HTML
import plotly.express as px

top = pd.DataFrame(freq.most_common(15), columns=["word", "count"])
fig = px.bar(top.sort_values("count"), x="count", y="word", orientation="h",
             title="Most frequent content words in Brown news texts",
             hover_data={"count": ":,"})
fig.update_layout(font=dict(size=14, color="black"), template="simple_white")
fig.write_html("top_words.html")      # open in any browser
