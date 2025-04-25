import pandas as pd
import ast

# df = pd.read_csv("data_frames/games_march2025_cleaned.csv")

# def parse_list(s):
#     try:
#         return ast.literal_eval(s)
#     except (ValueError, SyntaxError):
#         return []
    
# df_genres = df.assign(new_genres=df['genres'])
# df_genres['new_genres'] = df_genres['new_genres'].apply(parse_list)
# df_exploded = df_genres.explode('new_genres')
# df_avg_price = df_exploded.groupby(['new_genres'])['price'].mean().sort_values(ascending=True).tail(15)

# print(df_avg_price)