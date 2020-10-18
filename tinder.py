"""
This file contains all the things needed to control the dating app project, "TINDER".
Date: 31/12/2020
Created by: INDRAJIT AKULI
"""


import guihelper
import dbhelper


class Tinder(guihelper.GUI):    #Tinder is the subclass of GUI class in guihelper.py
    def __init__(self):
        self._dbObject = dbhelper.DBHelper()    # Connect with the database by creating an instance of DBHelper class
        super().__init__(self.loginHandler, self.regHandler, self.updateHandler)    # Calling of the superclass constructor i.e. create the login window


    def loginHandler(self, email, password, lbl):
        # This method searches the email and password into the tinder database
        response = self._dbObject.search("email", email, "password", password, "users")

        if len(response) == 0:
            lbl.config(text="(!) Invalid Email-id or Password")
        else:
            print("Welcome User")
            self.user_id = response[0][0]
            self.doLogin(response)


    def doLogin(self, data):
        self.mainWindow(self, data, 1, self.regHandler, self.updateHandler)


    def viewUsers(self, num):
        # This method is used to show the users other than logged in user
        response = self._dbObject.searchOne('user_id', self.user_id, 'users', 'NOT LIKE')
        data = []

        if num<0:
            num = len(response)-1
        if num>=len(response):
            num = 0
        x = response[num]
        data.append(x)
        self.mainWindow(self, data, 2, self.regHandler, self.updateHandler, num=num)


    def regHandler(self, name, email, password, age, gender, city, bio):
        # This method inserts the datas received by the user into the "users" table
        mydict = {
            'user_id': "NULL",
            'fname': name,
            'email': email,
            'password': password,
            'age': age,
            'gender': gender,
            'bg': 'Avatar.jpg',
            'city': city,
            'bio': bio
        }

        data = self._dbObject.search('fname', name, 'email', email, 'users')

        self._root1.destroy()

        if len(data) == 0:
            flag = self._dbObject.insert(mydict, 'users')

            if flag == 0:
                self.printMessage("Error", "Registration Fail!", 0)
            else:
                self.printMessage("Sucess", "Registration Successful", 1)
        else:
            self.printMessage("Registration Error", "You have already registered with this username and email-id. Please Login.", 0)


    def propose(self, juliet_id):
        # This method inserts the romeo_id and juliet_id into the "proposals" table
        data = self._dbObject.search('romeo_id', self.user_id, 'juliet_id', juliet_id, 'proposals')

        if len(data)>0:
            self.printMessage("Error", "You have already sent proposal to this person.", 0)
        else:
            mydict = {
                'proposal_id': "NULL",
                'romeo_id': self.user_id,
                'juliet_id': juliet_id
            }

            response = self._dbObject.insert(mydict, 'proposals')
            if response==1:
                self.printMessage("Sucess", "Proposal sent sucessfully", 1)
            else:
                self.printMessage("Proposal Failed", "Proposal has not sent. Some error occurred.", 0)


    def logoutHandler(self):
        # This method is used to logout
        self.clearMenu()
        self.clearScreen()
        self.dataList = []
       # if self.regwindowOpen or self.updatewindowOpen:
        #    self._root1.destroy()
        self.loginWindow(self.loginHandler, self.regHandler, self.updateHandler)


    def updateHandler(self, name, email, password, age, gender, city, bio):
        # This method is used to update data(s) of a logged in user
        response = self._dbObject.update(name, email, password, age, gender, city, bio, self.user_id, "users")

        if response==1:
            self.printMessage("Success", "Your data has updated sucessfully!", 1)
        else:
            self.printMessage("Error", "Updation Failed!!!", 0)

        self._root1.destroy()


    def proposalHandler(self, romeo_id, mode):
        # This method helps to collect the response of my proposals
        self.clearScreen()

        response1 = self._dbObject.searchOne('romeo_id', romeo_id, 'proposals', 'LIKE')
        response2 = []

        for i in response1:
            response = self._dbObject.searchOne('user_id', i[2], 'users', 'LIKE')
            response2.append(response[0])

        self.myProposalRequsetWindow(self, response2, mode)


    def requestHandler(self, juliet_id, mode):
        # This method helps to collect the response of my requests
        self.clearScreen()

        response1 = self._dbObject.searchOne('juliet_id', juliet_id, 'proposals', 'LIKE')
        response2 = []

        for i in response1:
            response = self._dbObject.searchOne('user_id', i[1], 'users', 'LIKE')
            response2.append(response[0])

        self.myProposalRequsetWindow(self, response2, mode)


    def matchHandler(self, romeo_id, mode):
        # This method helps to collect the response of my matches
        self.clearScreen()

        response1 = self._dbObject.searchOne('romeo_id', romeo_id, 'proposals', 'LIKE')
        juliets = []
        matches_id = []

        for i in response1:
            juliets.append(i[2])

        response2 = []
        for i in juliets:
            y = self._dbObject.search('romeo_id', i, 'juliet_id', romeo_id, 'proposals')
            if len(y) != 0:
                matches_id.append(y[0][1])

        for i in matches_id:
            response = self._dbObject.searchOne('user_id', i, 'users', 'LIKE')
            response2.append(response[0])

        self.myProposalRequsetWindow(self, response2, mode)


    def viewProposalWindowHandler(self, response):
        # This method sends the individual datas to the viewProposalWindow in the GUI class
        name = response[1]
        gender = response[5]
        age = str(response[4])
        city = response[7]
        bio = response[8]

        self.viewProposalWindow(name, gender, age, city, bio)


obj1 = Tinder()
