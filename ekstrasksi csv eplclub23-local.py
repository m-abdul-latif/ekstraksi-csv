import csv
# download file: https://www.kaggle.com/datasets/ramjasmaurya/footballsoccer-clubs-ranking

with open('epl_clubs23.csv', 'r') as file:
    df_players = csv.reader(file)
    for row in df_players:
        print(row)
