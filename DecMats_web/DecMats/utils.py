from .models import Decmats
from django.db import connection

class Queries():

    def __init__(self) -> None:
        pass

    def decmats_query(self, input_type = None, input_n =None, input_d=None):

        query_data = {}
        query_data['type'] = input_type
        query_data['n'] = input_n
        query_data['d'] = input_d

        query = "SELECT decmat FROM Decmats "
        query += "WHERE"
        first = True
        for k, v in query_data.items():
            if k == "type":
                data = v
                if data:
                    if not first:
                        query += " AND"
                    else:
                        first = False
                    if ',' not in data:
                        query += " type = " + "'" + str(data).capitalize() + "'"
                    else:
                        type_range = data.split(',')
                        # print(degree_range)
                        query += " type BETWEEN " + type_range[0] + ' AND ' + type_range[1] 
            elif k == "n":
                data = v
                if data:
                    if not first:
                        query += " AND"
                    else:
                        first = False
                    if ',' not in data:
                        query += " n =" + data
                    else:
                        n_range = data.split(',')
                        # print(disc_range)
                        query += " n BETWEEN " + n_range[0] + ' AND ' + n_range[1] 
            elif k == "d":
                data = v
                if  data:
                    if not first:
                        query += " AND"
                    else:
                        first = False
                    if ',' not in data:
                        query += " d =" + data
                    else:
                        n_range = data.split(',')
                        # print(disc_range)
                        query += " d BETWEEN " + n_range[0] + ' AND ' + n_range[1]
                    
                    
        query += " LIMIT 10"
        print(query)

        cursor = connection.cursor()
        cursor.execute(query)
        decmats = cursor.fetchall()

        return decmats