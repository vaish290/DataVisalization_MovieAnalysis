# DataVisalization_MovieAnalysis
This is an interactive dashboard built with Python and Streamlit that explores Bollywood actor-director collaborations from 1951 to 2019. You can filter by genres, year, and more to discover fun and useful trends in Indian cinema.

📌 What This Project Does
This project helps you:

- See which actors and directors worked together most often

- Find out which pairs have the most award-winning films

- Explore average IMDb ratings for collaborations

- Understand what genres certain actor-director pairs prefer

- Use filters to narrow down the data by year or genre

🔍 Features

🔗 Frequent Collaborations – See the most common actor-director pairs in a graph

🏆 Most Awarded Pairs – View the top 5 actor-director pairs with the highest number of wins

🍿 Genre Distribution – Pick an actor-director pair and see the genres they worked on

⭐ IMDb Ratings – Check average IMDb ratings for the top 5 actor-director collaborations

🎛️ Filters – Easily change year range, genres, and number of top pairs displayed

🐍 Python Data Analysis (Jupyter Notebook)

This section includes data cleaning, merging, and exploratory visualizations built using pandas, matplotlib, seaborn, and plotly. It focuses on uncovering trends in genres, actor appearances, movie ratings, and award patterns.

🟢 Genre Popularity Over Time (Bubble Chart)
<img width="1392" height="790" alt="image" src="https://github.com/user-attachments/assets/2a1bb246-ebc6-452c-81ca-b048512a5bc4" />


Shows how different genres like Drama, Romance, and Action grew over the years.

Bigger bubbles mean more movies of that genre in that year.

🟦 Average IMDb Ratings by Decade

<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/95dca8dd-72ea-4bfb-ad1a-18d90e3179dc" />

A bar chart showing how the average IMDb ratings have changed from the 1950s to 2010s.

Earlier decades like the 1950s and 60s had higher ratings, which gradually declined.

💗 Top Genre Combinations (Bar Chart)

<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/5861d88b-5161-4e7d-8047-43d0a71fcb0e" />

Displays the most common multi-genre combinations like "Action-Crime-Drama" or "Drama-Romance".

Helps understand Bollywood’s trend of mixing genres.

👤 Top 10 Actors by Number of Movies

<img width="990" height="590" alt="image" src="https://github.com/user-attachments/assets/67b0635c-d664-468e-94db-73a51e2f6355" />

A bar chart showing which actors appeared in the most number of films.

Anupam Kher, Shakti Kapoor, and Amitabh Bachchan are at the top.

🎯 IMDb Ratings vs Wins (Scatter Plot)

<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/3184f847-2890-46cc-9e19-025dafd10895" />

Each dot is a movie. The chart compares IMDb rating (x-axis) with number of awards (y-axis).

Shows that higher-rated movies tend to win more awards.

🏆 Top 10 Genres by Total Wins

<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/daae770e-90cc-4913-8291-4d43a97818f5" />

A bar chart ranking genres based on how many total awards they’ve won.

Drama, Action, and Comedy lead the chart.

🔄 Genre Blending – Masala Films (Venn Diagram)

<img width="640" height="587" alt="image" src="https://github.com/user-attachments/assets/3c8ccd0c-ad02-49d3-8c1a-4e1190dcb62f" />

A Venn diagram showing how often Romance, Action, and Comedy are mixed in movies.

Shows Bollywood's love for multi-genre "masala" films.

👥 Top Actor-Director Collaborations (Network Graph)

<img width="1589" height="1190" alt="image" src="https://github.com/user-attachments/assets/48988911-0e45-49da-805b-eba323776833" />

A graph of actor-director pairs who have worked together most frequently.

Strong links (thicker lines) show high collaboration counts.

🏅 Top Actor-Director Pairs with Most Wins

<img width="1190" height="790" alt="image" src="https://github.com/user-attachments/assets/14b916f1-2102-45c6-8e70-db603c51a58b" />

A horizontal bar chart ranking actor-director pairs by number of movie awards.

Pairs like Boman Irani – Rajkumar Hirani are top performers.

🥧 Genre Distribution of a Pair (Pie Chart)

<img width="777" height="790" alt="image" src="https://github.com/user-attachments/assets/76d74905-b5e4-4474-bb66-d0868c95ca76" />

A pie chart showing the types of genres a selected actor-director pair usually works in.

For example, Boman Irani – Rajkumar Hirani mostly worked in Drama and Comedy.

🔵 Average IMDb Rating for Top 10 Actor-Director Pairs (Bubble Chart)

<img width="1184" height="790" alt="image" src="https://github.com/user-attachments/assets/2faa9dd6-52c1-4897-b764-0a75335abff0" />

Shows the top 10 actor-director pairs with the highest average IMDb ratings.

Each bubble represents a pair, and the rating is shown inside the bubble.

Larger bubbles = higher ratings or stronger collaboration visibility.

For example, Boman Irani – Rajkumar Hirani and Anurag Kashyap’s frequent collaborators appear consistently at the top.

🌐 Interactive Dashboard (Streamlit App)

This Streamlit-powered dashboard allows users to explore actor-director collaborations interactively. Features include filters by year, genre, and dynamic visualizations such as network graphs, bar charts, and pie charts to reveal deep insights into Bollywood cinema.

1️⃣ Top 5 Frequent Actor-Director Collaborations (Network Graph)

<img width="1897" height="1031" alt="dshb1" src="https://github.com/user-attachments/assets/93c48b05-cb10-4484-81ac-2fda2e31f160" />

Displays a network of the most frequently collaborating actor-director pairs.

Each node represents a person; lines show collaborations.

Color and size indicate the number of connections.

Why it matters: Helps identify the strongest working partnerships in Bollywood cinema.

2️⃣ Top 5 Actor-Director Pairs with Most Wins (Bar Chart)

<img width="1778" height="762" alt="dshb2" src="https://github.com/user-attachments/assets/d8c34d54-513d-4713-b961-ccbd523b87bf" />

A horizontal bar chart showing actor-director pairs whose movies have won the most awards.

Examples include Boman Irani – Rajkumar Hirani and Ranveer Singh – Sanjay Leela Bhansali.

Why it matters: Highlights critically successful partnerships.

3️⃣ Genre Distribution for Selected Actor-Director Pair (Pie Chart)

<img width="1780" height="762" alt="dshb3" src="https://github.com/user-attachments/assets/2ca4896d-be70-489c-8ae6-3efc33170b9b" />

Select an actor and a director to see what genres they mostly worked in.

The pie chart shows genre percentages such as Action, Drama, War, etc.

Why it matters: Reveals the genre preferences of specific actor-director duos.

4️⃣ Average IMDb Rating for Top 5 Actor-Director Pairs (Bubble Chart + Table)

<img width="1725" height="965" alt="dshb4" src="https://github.com/user-attachments/assets/4a2d29fc-3601-46b1-aaca-10636a7f29a8" />

A bubble chart showing average IMDb ratings for the most frequent actor-director pairs.

The table below lists actor names, director names, average ratings, and number of collaborations.

Why it matters: Lets users compare popularity vs productivity of different pairs.

