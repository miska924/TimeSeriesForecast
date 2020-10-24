#!/bin/python3
import pandas as pd
import numpy as np
import requests
import datetime
import pathlib
import apimoex
import sys

board = 'TQBR'

res = list()

with open("TICKs", "r") as TICKs:
    TICKs = [line.rstrip() for line in TICKs]
process = 0

result = dict()

CORRECT = list()
with requests.Session() as session:
    for TICK in TICKs:
         process = process + 1
         print(("%.1f") % ((process / len(TICKs)) * 100), ' %')
         data = apimoex.get_board_history(session, TICK)
         if data == [] or TICK == "":
             continue
         CORRECT.append(TICK)
         df = pd.DataFrame(data)
         df = df[['TRADEDATE','CLOSE']]
         df = df.to_numpy()
         tmp = df[:,0:2]
         for i in range(tmp.shape[0]):
            if tmp[i][0] not in result:
                result[tmp[i][0]] = dict()
            result[tmp[i][0]][TICK] = tmp[i][1]
         if len(res) == 0:
             df = df[:,0:2]
             df = np.swapaxes(df, 0, 1)
             res.append(df[0].tolist())
             res.append(df[1].tolist())
         else:
             df = df[:,1:2]
             df = np.swapaxes(df, 0, 1)
             res.append(df[0].tolist())

#orig_stdout = sys.stdout
f = open('TABLE', 'w')
sys.stdout = f
TICKs = CORRECT.copy()
print("%10s" % (''), end = ' ')
for i in range(1, len(res)):
    print("%10s" % (TICKs[i - 1]), end = ' ')
print()

for x in sorted(result.keys(), key=lambda x: x[1]):
    print("%10s" % (x), end=' ')
    for y in TICKs:
        if y in result[x]:
            print("%10s" % (result[x][y]), end=' ')
        else:
            print("%10s" % ("?"), end=' ')
    print()
