"""
This file contains all the things needed to communicate with the database for the dating app project, "TINDER".
Date: 31/12/2020
Created by: INDRAJIT AKULI
"""


import mysql.connector


class DBHelper:
    def __init__(self):
        # Constructor of DBHelper class is used to connect with the tinder database
        try:
            self._connection = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="tinder")
            self._mycursor = self._connection.cursor()
        except:
            print("Could not Connect!")


    def search(self, key1, value1, key2, value2, table):
        # This method is use to search into the database with two keys and two values and returns a response which is a List of Tuples
        self._mycursor.execute("SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'".format(table, key1, value1, key2, value2))
        response = self._mycursor.fetchall()

        return response


    def searchOne(self, key, value, table,  type):
        # This method is use to search into the database with one key and one value and returns a response which is a List of Tuples
        self._mycursor.execute("SELECT * FROM `{}` WHERE `{}` {} '{}'".format(table, key, type, value))
        response = self._mycursor.fetchall()

        return response


    def insert(self, inputDict, table):
        # This method is used to insert datas into a table of the tinder database. The datas are contained into the dictionary "inputDict"
        cols = ""
        colValues = ""

        for i in inputDict:
            cols = cols+"`"+i+"`"+","
            colValues = colValues + "'" + str(inputDict[i]) + "'" + ","

        cols = cols[:-1]
        colValues = colValues[:-1]

        try:
            self._mycursor.execute("INSERT INTO `{}` ({}) VALUES ({})".format(table, cols, colValues))
            self._connection.commit()
            return 1
        except:
            return 0


    def update(self, name, email, password, age, gender, city, bio, user_id, table):
        # This method is used to update data(s) into a table of the tinder database
        try:
            self._mycursor.execute("UPDATE `{0}` SET `fname` = '{1}', `email` = '{2}', `password` = '{3}', "
                                   "`age` = '{4}', `gender` = '{5}', `city` = '{6}', `bio` = '{7}' WHERE"
                                   " `{8}`.`user_id` = {9}"
                                   .format(table, name, email, password, age, gender, city, bio, table, user_id))
            self._connection.commit()
            return 1
        except:
            return 0