import numpy as np
import numpy
import pandas as pd
import math as mt
from matplotlib import pyplot as plt
from scipy.stats import norm
from numpy import random
from sklearn.model_selection import train_test_split
import seaborn as sns


class naive_training():    
    
    def naive_entrenamiento(data_w,Y):

        #data_w = data_cleaning(data_w)
        samples, features = data_w.shape
        y_class = np.unique(Y)
        n_class = len(y_class)

        mean = np.array(data_w.groupby(by=Y).mean())
        var = np.array(data_w.groupby(by=Y).var())
        priors = np.array(data_w.groupby(by=Y).count()/samples)

        pred = naive_training.Naive_Predict(data_w, mean,var,priors,y_class)

        accuracy = "{:0.2f}".format(metrics.accuracy_score(Y, pred))
        precision = "{:0.2f}".format(metrics.precision_score(Y, pred,pos_label='Y'))
        recall = "{:0.2f}".format(metrics.recall_score(Y, pred,pos_label='Y'))
        f1 = "{:0.2f}".format(metrics.f1_score(Y, pred,pos_label='Y'))

        writer = "Naive_"+"Vars="+ str(data_w.columns.values).replace('\n', '').replace('\r', '')+"_A="+accuracy+"_R="+recall+"_F1="+f1+"_P="+precision
        Write_Log("CadenaConfiguracion.csv",[writer])

        print("Navie_Accuracy:",accuracy)
        print("Navie_Recall:",recall)
        print("Navie_F1:",f1)
        print("Navie_Precision:",precision)
        print("")
        #str(data_w.columns.values) 
        writer_pkl = "Naive3=" + "ACC=" + accuracy + "PRE=" + precision +".pkl"
   
        jl.dump(pred, writer_pkl,compress=0, protocol=None)
    
        return (pred)
    
    
    def Naive_Predict(X, m,v,p,y_class):
        #X = data_cleaning(data_w)
        Y_Pred = []
        for x in np.array(X):
            posteriors = []
            for idx, c in enumerate(y_class):
                prior = np.log(p[idx][0])

                numer = np.exp(-((x - m[idx])**2)/(2 * v[idx]) )
                denomi = np.sqrt(2 * np.pi * v[idx])
                numl =np.log(numer/denomi)

                post = np.sum(numl)
                post = prior + post

                posteriors.append(post)

            Y_Pred.append(y_class[np.argmax(posteriors)])
        return np.array(Y_Pred)