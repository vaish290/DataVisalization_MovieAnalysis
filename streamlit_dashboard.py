import streamlit as st
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import plotly.express as px

# Load the datasets
@st.cache_data
def load_data():
    frequent_collaborations = pd.read_csv("merged_actor_director_data.csv")
    bollywood_full_preprocessed_split = pd.read_csv("bollywood_full_preprocessed_split.csv")
    return frequent_collaborations, bollywood_full_preprocessed_split

frequent_collaborations, bollywood_full_preprocessed_split = load_data()

# Combine datasets
combined_data = pd.merge(frequent_collaborations, bollywood_full_preprocessed_split, on='imdb_id', how='inner')

st.title("Bollywood Actor-Director Collaborations Analysis")

# Sidebar for filters
st.sidebar.header("Filters")

# Year filter
if 'year_of_release' in combined_data.columns:
    min_year = int(combined_data['year_of_release'].min())
    max_year = int(combined_data['year_of_release'].max())
    year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
    filtered_data = combined_data[(combined_data['year_of_release'] >= year_range[0]) & (combined_data['year_of_release'] <= year_range[1])]
else:
    st.sidebar.write("Year filter not available")
    filtered_data = combined_data

# Genre filter
genre_columns = ['genre1', 'genre2', 'genre3']
if all(col in combined_data.columns for col in genre_columns):
    all_genres = combined_data[genre_columns].melt()['value'].dropna().unique()
    selected_genres = st.sidebar.multiselect("Select Genres", all_genres, default=all_genres[:5])
    genre_filter = filtered_data[genre_columns].isin(selected_genres).any(axis=1)
    filtered_data = filtered_data[genre_filter]
else:
    st.sidebar.write("Genre filter not available")

# Top N filter
top_n = st.sidebar.slider("Select Top N Pairs", 5, 20, 10)

# Visualization 1: Network Graph
st.header(f"Top {top_n} Frequent Actor-Director Collaborations")

collaboration_data = filtered_data.groupby(['actor', 'name']).size().reset_index(name='collaboration_count')
top_collaborations = collaboration_data.nlargest(top_n, 'collaboration_count')

G = nx.DiGraph()
for _, row in top_collaborations.iterrows():
    G.add_edge(row['actor'], row['name'], weight=row['collaboration_count'])

# Increase spacing and adjust layout parameters
pos = nx.spring_layout(G, k=3.5, iterations=50, seed=42)

edge_x, edge_y = [], []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1.5, color='#4169E1'),  # Royal Blue for better visibility
    hoverinfo='none',
    mode='lines'
)

node_x, node_y = [], []
node_text = []
node_colors = []

# Separate actors and directors for different styling
actors = set(G.nodes()) & set(filtered_data['actor'].unique())
directors = set(G.nodes()) & set(filtered_data['name'].unique())

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    connections = len(list(G.neighbors(node)))
    node_colors.append(connections)
    
    # Create role-specific labels
    role = "Actor" if node in actors else "Director"
    node_text.append(f"{role}: {node}<br>Connections: {connections}")

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    hoverinfo='text',
    text=[node.split()[0] for node in G.nodes()],  # Show first name only
    textposition="top center",
    textfont=dict(size=10, color='white'),
    marker=dict(
        showscale=True,
        colorscale='Viridis',
        size=25,
        color=node_colors,
        colorbar=dict(
            thickness=15,
            title='Number of Connections',
            xanchor='left',
            titleside='right',
            titlefont=dict(color='white')
        ),
        line=dict(width=2, color='white')
    )
)

node_trace.text = node_text

# Create figure with improved layout
fig = go.Figure(
    data=[edge_trace, node_trace],
    layout=go.Layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=5, r=5, t=40),
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=700,  # Increased height
        font=dict(color='white')
    )
)

# Update hover templates
fig.update_traces(
    hovertemplate="%{text}<extra></extra>",
    selector=dict(type='scatter', mode='markers+text')
)

st.plotly_chart(fig, use_container_width=True)

# Visualization 2: Top N Actor-Director Pairs with Most Wins
st.header(f"Top {top_n} Actor-Director Pairs with Most Wins")

if 'wins' in filtered_data.columns:
    filtered_data['wins'] = pd.to_numeric(filtered_data['wins'], errors='coerce').fillna(0)
    grouped_data = filtered_data.groupby(['actor', 'name'])['wins'].sum().reset_index()
    top_wins = grouped_data.nlargest(top_n, 'wins')
    
    # Calculate dynamic height based on number of pairs
    chart_height = max(600, top_n * 30)  # 30 pixels per pair
    
    fig = px.bar(top_wins, 
                 x='wins', 
                 y=[f"{row['actor']} - {row['name']}" for _, row in top_wins.iterrows()],
                 orientation='h',
                 labels={'wins': 'Number of Wins', 'y': 'Actor-Director Pair'},
                 #title=f'Top {top_n} Actor-Director Pairs with Most Wins',
                 height=chart_height)  # Dynamic height
    
    fig.update_layout(
        yaxis={
            'categoryorder': 'total ascending',
            'tickfont': {'size': 10 if top_n > 10 else 12}  # Reduce font size for more pairs
        },
        margin=dict(l=250, r=20, t=70, b=50),  # Increased left margin for labels
        #title_x=0.5,  # Center the title
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='white'),
        xaxis=dict(
            gridcolor='rgba(255, 255, 255, 0.1)',
            title_font={'size': 12}
        ),
        bargap=0.2  # Add space between bars
    )
    
    # Update bar colors and hover template
    fig.update_traces(
        marker_color='rgb(65, 105, 225)',
        hovertemplate="<b>%{y}</b><br>Wins: %{x}<extra></extra>"
    )
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("The 'wins' column is missing in the dataset.")

# Visualization 3: Genre Distribution for Selected Actor-Director Pair
st.header("Genre Distribution for Selected Actor-Director Pair")

actors = filtered_data['actor'].unique()
directors = filtered_data['name'].unique()

selected_actor = st.selectbox("Select Actor", actors)
selected_director = st.selectbox("Select Director", directors)

if 'wins' in filtered_data.columns and all(col in filtered_data.columns for col in genre_columns):
    pair_data = filtered_data[(filtered_data['actor'] == selected_actor) & (filtered_data['name'] == selected_director)]
    genre_data = pair_data[genre_columns].melt(value_name='genre')
    genre_counts = genre_data['genre'].value_counts()
    
    if not genre_counts.empty:
        fig = px.pie(values=genre_counts.values, names=genre_counts.index, 
                     title=f"Genre Distribution for {selected_actor} - {selected_director}")
        st.plotly_chart(fig)
    else:
        st.write(f"No genre data available for {selected_actor} - {selected_director} pair.")
else:
    st.write("The 'wins' column or genre columns are missing in the dataset.")

# Visualization 4: Average IMDb Rating for Top N Actor-Director Pairs
st.header(f"Average IMDb Rating for Top {top_n} Actor-Director Pairs")

if 'imdb_rating' in filtered_data.columns:
    filtered_data['imdb_rating'] = pd.to_numeric(filtered_data['imdb_rating'], errors='coerce')
    
    grouped_data = filtered_data.groupby(['actor', 'name']).agg(
        avg_imdb_rating=('imdb_rating', 'mean'),
        collaboration_count=('imdb_id', 'count')
    ).reset_index()
    
    top_pairs = grouped_data.nlargest(top_n, 'collaboration_count')
    
    fig = px.scatter(top_pairs, 
                     x=[f"{row['actor']} - {row['name']}" for _, row in top_pairs.iterrows()],
                     y='avg_imdb_rating',
                     size='collaboration_count',
                     hover_data=['collaboration_count'],
                     labels={'x': 'Actor-Director Pair', 'y': 'Average IMDb Rating', 'size': 'Collaboration Count'},
                     title=f'Average IMDb Rating for Top {top_n} Actor-Director Pairs')
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig)
    
    st.write(f"Top {top_n} Actor-Director Pairs with Average IMDb Ratings:")
    st.dataframe(top_pairs)
else:
    st.write("The 'imdb_rating' column is missing in the dataset.")