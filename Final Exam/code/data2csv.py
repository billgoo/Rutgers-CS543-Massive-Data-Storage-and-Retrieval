# -*-coding:utf-8 -*-
import csv
import pandas as pd

line_list_ratings, line_list_users, line_list_movies = [], [], []
age_dict = {"1": "Under 18", "18": "18-24", "25": "25-34", "35": "35-44", "45": "45-49", "50": "50-55", "56": "56+"}
occupation_dict = {"0": "'other' or not specified", "1": "academic/educator", "2": "artist",\
                    "3": "clerical/admin", "4": "college/grad student", "5": "customer service",\
                    "6": "doctor/health care", "7": "executive/managerial", "8": "farmer", "9": "homemaker",\
                    "10": "K-12 student", "11": "lawyer", "12": "programmer", "13": "retired",\
                    "14": "sales/marketing", "15": "scientist", "16": "self-employed", "17": "technician/engineer",\
                    "18": "tradesman/craftsman", "19": "unemployed", "20": "writer"}

# transfer ratings
with open('ratings.dat', 'rb') as filein:
    for line in filein:
        l = line.decode('utf-8')
        line_list_ratings.append(l.strip('\n').split('::'))
# list to dataframe and write to csv
df_ratings = pd.DataFrame(line_list_ratings, columns=['UserID','MovieID','Rating','Timestamp'])
df_ratings.to_csv('ratings.csv', columns=['UserID','MovieID','Rating','Timestamp'], index=False, sep=',')

# transfer users
with open('users.dat', 'rb') as filein:
    for line in filein:
        l = line.decode('utf-8').strip('\n').split('::')
        # replace int tags with string
        l[2], l[3] = age_dict[l[2]], occupation_dict[l[3]]
        line_list_users.append(l)

df_users = pd.DataFrame(line_list_users, columns=['UserID','Gender','Age','Occupation','Zip-code'])
df_users.to_csv('users.csv', columns=['UserID','Gender','Age','Occupation','Zip-code'], index=False, sep=',')

# transfer movies
with open('movies.dat', 'rb') as filein:
    for line in filein:
        l = line.decode('utf-8')
        line_list_movies.append(l.strip('\n').split('::'))

df_movies = pd.DataFrame(line_list_movies, columns=['MovieID','Title','Genres'])
df_movies.to_csv('movies.csv', columns=['MovieID','Title','Genres'], index=False, sep=',')
