from numpy import prod
import pymongo
from pymongo import MongoClient
import pprint
import os
import random
from bson.objectid import ObjectId
import json


mongodb_host = os.environ.get('MONGO_HOST', 'localhost')
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))
client = MongoClient(mongodb_host, mongodb_port)
db = client.optimasi

result = list(db.temp.find())
my_list = []

for i in range(len(result)):
    dataTable = []

    a = result[i]
    dataTable.append(a.get('mhs'))
    dataTable.append(a.get('dosbing'))
    dataTable.append(a.get('p1'))
    dataTable.append(a.get('p2'))

    my_list.append(dataTable)

# my_list = [[[1.0, 5.0, 3.0], [0.0, 5.0, 3.0], [0.0, 2.0, 1.0], [0.0, 4.0, 1.0]],
#             [[0.0, 4.0, 4.0], [0.0, 4.0, 4.0], [1.0, 4.0, 1.0], [0.0, 1.0, 2.0]],
#             [[0.0, 2.0, 1.0], [1.0, 2.0, 3.0], [1.0, 1.0, 1.0], [1.0, 3.0, 4.0]],
#             [[1.0, 5.0, 4.0], [1.0, 1.0, 4.0], [1.0, 3.0, 4.0], [0.0, 5.0, 4.0]],
#             [[0.0, 1.0, 1.0], [1.0, 5.0, 4.0], [1.0, 2.0, 4.0], [0.0, 1.0, 4.0]],
#             [[0.0, 4.0, 1.0], [1.0, 3.0, 4.0], [1.0, 5.0, 4.0], [1.0, 2.0, 3.0]],
#             [[1.0, 1.0, 3.0], [0.0, 4.0, 1.0], [1.0, 4.0, 3.0], [0.0, 2.0, 1.0]],
#             [[0.0, 3.0, 3.0], [0.0, 3.0, 3.0], [0.0, 5.0, 1.0], [1.0, 4.0, 3.0]],
#             [[1.0, 2.0, 2.0], [0.0, 5.0, 1.0], [1.0, 3.0, 3.0], [1.0, 1.0, 3.0]],
#             [[1.0, 2.0, 4.0], [1.0, 2.0, 2.0], [0.0, 1.0, 3.0], [0.0, 5.0, 1.0]],
#             [[0.0, 2.0, 3.0], [1.0, 1.0, 1.0], [0.0, 5.0, 3.0], [0.0, 2.0, 4.0]],
#             [[1.0, 3.0, 4.0], [1.0, 4.0, 2.0], [1.0, 2.0, 2.0], [0.0, 5.0, 3.0]],
#             [[1.0, 3.0, 1.0], [0.0, 2.0, 1.0], [1.0, 5.0, 2.0], [1.0, 4.0, 4.0]],
#             [[0.0, 1.0, 2.0], [0.0, 1.0, 2.0], [1.0, 3.0, 2.0], [1.0, 3.0, 2.0]],
#             [[1.0, 4.0, 2.0], [0.0, 4.0, 3.0], [0.0, 2.0, 3.0], [1.0, 3.0, 3.0]],
#             [[1.0, 5.0, 1.0], [1.0, 3.0, 2.0], [1.0, 3.0, 1.0], [1.0, 1.0, 1.0]],
#             [[1.0, 3.0, 2.0], [1.0, 3.0, 1.0], [0.0, 4.0, 2.0], [0.0, 3.0, 1.0]],
#             [[1.0, 1.0, 4.0], [1.0, 5.0, 2.0], [1.0, 1.0, 4.0], [1.0, 4.0, 2.0]],
#             [[1.0, 5.0, 2.0], [0.0, 1.0, 3.0], [0.0, 1.0, 2.0], [1.0, 5.0, 2.0]],
#             [[0.0, 4.0, 3.0], [1.0, 2.0, 4.0], [0.0, 4.0, 4.0], [0.0, 2.0, 2.0]]]
#

num = 1
for j in range(20):
    for k in range(20):
        for l in range(20):
            # pprint.pprint(my_list)
            """LOGIC GOES HERE"""
            for j in range(len(my_list)):
                # menghitung data pertama pada my_list
                data = j

                """RUMUS"""
                # menghitung status
                hx = (my_list[data][0][0]+my_list[data][1][0]+my_list[data][2][0]+my_list[data][3][0])/4

                """RUMUS"""
                # menghitung jam dan hari
                YZ = []
                for i in range(4):
                    result = (3*my_list[data][i][1]+5*my_list[data][i][2])
                    YZ.append(result)
                YZprod = int(prod(YZ))

                """RUMUS"""
                # menghitung kasus akar
                akar = []
                for i in range(4):
                    if (YZprod**(1/4) == YZ[i]):
                        a.append(0)
                    else:
                        a.append(1)

                """RUMUS"""
                # fungsi fitness
                f = 1/(a + hx + 1)
                if f >= 0.8 :
                    # sama.append(my_list[data])
                    print(my_list[data])
                    # db.komputasi.insert({'mhs': my_list[data][0], 'dosbing' : my_list[data][1], 'p1' : my_list[data][2], 'p2' : my_list[data][3], 'fitnes' : f})

            temp = my_list[0][3]
            for i in range(19):
                my_list[i][3] = my_list[i+1][3]
            my_list[19][3] = temp
        temp = my_list[0][2]
        for i in range(19):
            my_list[i][2] = my_list[i+1][2]
        my_list[19][2] = temp
    temp = my_list[0][1]
    for i in range(19):
        my_list[i][1] = my_list[i+1][1]
    my_list[19][1] = temp
