# -*- coding: utf-8 -*-
import numpy as np
import random
import copy
import sys

#movie_name = open('name_log','w')
#__con__ = sys.stderr
#sys.stderr = movie_name

class load_MovieName():

    def __init__(self):
        self.MovieName = []
        print ('initialization complete',file = sys.stderr)

    def load_file(self,nameset):
        f1 = open(nameset,'r')
        for i, dataline in enumerate(f1):
            index, name, classification = dataline.strip('\r\n').split('::')
            #self.MovieName.append([index,name,classification])
            self.MovieName.append(index)
            self.MovieName.append(name)
            self.MovieName.append(classification)

            if i% 1000 == 0:
                print(f'{i} movies has been loaded',file = sys.stderr)

        f1.close()
        print('loading complete',file = sys.stderr)
        #print(self.MovieName,file = sys.stderr)

if __name__ == '__main__':

    movie_data = 'ml-1m/movies.dat'
    l_MN = load_MovieName()
    l_MN.load_file(movie_data)
