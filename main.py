import pandas as pd
import config
import ast
from plotly_settings import plotly_settings
import time

df = pd.read_csv('data_frames/games_march2025_cleaned.csv')
# df2 = pd.read_csv('data_frames/steam_games(price).csv')

# Получение множества уникальных жанров
def  getting_all_tags():
    
    # tags = df['tags'].str.split(',').explode('tags')
    # print(tags)
    print(df['tags'].str.split(',').explode())
    
    # for index, row in df1.iterrows():
    #     if isinstance(row['genres'], str):
    #         genres_set = set(genre.strip(" '\"") for genre in row['genres'].split(","))
    #         all_genres.update(genres_set)
    # print(all_genres)
            



if __name__ == "__main__":
    start_time = time.time()
    
    getting_all_tags()
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Код выполнялся {execution_time:.2f} секунд")
    
    
    
    
    
    
    
    
    
    
# Получение множества уникальных тэгов (жанров)
# def unique_tags():
#     tags_set = set()

#     for index, row in df.iterrows():
#         tags_list = ast.literal_eval(row['tags'])
#         for tags in tags_list:
#             tags_set.add(tags)

#     print(tags_set)
    
# # Запись количества игр в жанре и их цен в словарь tags_counts
# def main():
#     tags_set = config.ALL_TAGS
    
#     tags_counts = {tag : {'count': 0, 'price': 0} for tag in tags_set}
#     for index, row in df.iterrows():
#         for tag in tags_set:
#             if tag in ast.literal_eval(row['tags']):
#                 tags_counts[tag]['count'] += 1
#                 try:
#                     tags_counts[tag]['price'] += float(row['price(USD)'].replace("$", "").replace("Free", "0"))
#                 except:
#                     print(index, row['Title'], row['price(USD)'])
    
#     config.TAGS_DICT = tags_counts

# # Создание нового dataframe - my_tags_data.csv
# def my_tags_data():
#     new_data = []
#     for tag, data in config.TAGS_DICT.items():
#         tag_name = tag
#         sum_of_tags = data['count']
#         total_revenue = round(data['price'], 2)
#         average_revenue = round(total_revenue/sum_of_tags, 2)
        
#         new_data.append({
#         'name of tag': tag_name,
#         'sum of tags': sum_of_tags,
#         'total revenue' : total_revenue,
#         'average revenue' : average_revenue
#         })
    
#     tags_data = pd.DataFrame(new_data)
#     tags_data.to_csv('data_frames/my_tags_data.csv', index=False)
        