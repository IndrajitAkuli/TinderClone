"""
This file contains all the things needed to create only the GUI of the dating app project, "TINDER".
Date: 31/12/2020
Created by: INDRAJIT AKULI
"""


from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
#from PIL import Image, ImageTk


class GUI:
    def __init__(self, loginHandler, regHandler, updateHandler):
        # Constructor of GUI class, creates a GUI window of size 400*600
        self._root = Tk()
        self._root.title("Tinder")
        self._root.minsize(400, 600)
        self._root.maxsize(400, 600)
        self._root.configure(background="#FF7272")
        self.loginWindow(loginHandler, regHandler, updateHandler)
        self.dataList = []
        self.regwindowOpen = False
        self.updatewindowOpen = False
        self._root.mainloop()


    def loginWindow(self, loginHandler, regHandler, updateHandler):
        # This window contains all the components needed for a login window
        self.tinderIco = PhotoImage(file="Image/tinderIcon2.png")
        self.tinderIco = self.tinderIco.zoom(10)
        self.tinderIco = self.tinderIco.subsample(130)
        self.lblico = Label(self._root, image=self.tinderIco, bg="#FF7272")
        self.lblico.place(x=120, y=30)
        self._label1 = Label(self._root, text="TINDER")
        self._label1.configure(font=("candara", 25, "bold", "italic"), bg="#FF7272", fg="white")
        self._label1.place(x=160, y=30)

        self.emailLogo = PhotoImage(file="Image/mail.png")
        self._lblico1 = Label(self._root, image=self.emailLogo, bg="#FF7272")
        self._lblico1.place(x=83, y=115)
        self._label2 = Label(self._root, text="Email ")
        self._label2.configure(font=("calibri", 14, "bold"), bg="#FF7272", fg="#FFF9A9")
        self._label2.place(x=109, y=115)

        self._emailInput = Entry(self._root, font=("times", 10), bd=2)                  # To take email-id from  user
        self._emailInput.grid(row=2, padx=(85, 0), pady=(150, 20), ipady=4, ipadx=50)

        self.passwordLogo = PhotoImage(file="Image/password.png")
        self._lblico2 = Label(self._root, image=self.passwordLogo, bg="#FF7272")
        self._lblico2.place(x=82, y=202)
        self._label3 = Label(self._root, text="Password ")
        self._label3.configure(font=("calibri", 14, "bold"), bg="#FF7272", fg="#FFF9A9")
        self._label3.place(x=109, y=202)

        self._passwordInput = Entry(self._root, font=("times", 10), show='*', bd=2)     # To take password from  user
        self._passwordInput.grid(row=4, padx=(61, 24), pady=(37, 0), ipady=4, ipadx=25)

        viewBtn = Button(self._root, font=("times",10), text="SHOW", height=1, width=5, bg="#02032E", fg="#fff",
                              command=lambda:self.viewHidePassword(self._passwordInput, viewBtn, mode="show"))
        viewBtn.place(x=266, y=237)                                 # This button is used to show or hide the password

        self._loginBtn = Button(self._root, text="Login", width=12, height=1, font=("times", 12, "bold"), bg="#02032E",
                                fg="#fff", command=lambda: loginHandler(self._emailInput.get(), self._passwordInput.get(),
                                                             self._labelWarning))
        self._loginBtn.place(x=137, y=330)      # After clicking the button the control goes to the loginHandler() method of tinder.py and open my profile window

        self._labelWarning = Label(self._root, text="")     # This label is to validate the email and password input field
        self._labelWarning.configure(font=("calibri", 11), bg="#FF7272", fg="yellow")
        self._labelWarning.place(x=100, y=365)

        self._label3 = Label(self._root, text="Not a Member?")
        self._label3.configure(font=("calibri", 12), bg="#FF7272", fg="#000")
        self._label3.place(x=142, y=440)

        self._regBtn = Button(self._root, text="Click here", width=10, font=("times", 10, "bold"),  bg="#02032E",
                              fg="#fff", command=lambda: self.regWindow(regHandler, updateHandler, 1))
        self._regBtn.place(x=156, y=465)        # After clicking the button the control goes to the regWindow() method and open registration window


    def regWindow(self, regHandler, updateHandler, mode):
        # If mode=1 then, this window is registration window; if mode=2 then, this window is update window
        self._root1 = Tk()
        self._root1.title("Tinder")

        self._root1.minsize(400, 700)
        self._root1.maxsize(400, 700)
        self._root1.configure(background="#FF7272")

        def clearPlaceholder(event):        # This method clear the placeholder on clicking it or focusing in it
            if event.widget.get() == "Age" or event.widget.get() == "Gender" or event.widget.get() == "City" or event.widget.get() == "About":
                event.widget.delete(0, END)

        def returnPlaceholderAge(event):    # This method returns the placeholder "Age" after focusing out it
            if event.widget.get() == "":
                event.widget.insert(0, "Age")
        def returnPlaceholderGender(event): # This method returns the placeholder "Gender" after focusing out it
            if event.widget.get() == "":
                event.widget.insert(0, "Gender")
        def returnPlaceholderCity(event):   # This method returns the placeholder "City" after focusing out it
            if event.widget.get() == "":
                event.widget.insert(0, "City")
        def returnPlaceholderAbout(event):  # This method returns the placeholder "About" after focusing out it
            if event.widget.get() == "":
                event.widget.insert(0, "About")

        if mode == 1:       # for Registration window
            self._label1 = Label(self._root1, text="REGISTRATION")
            self._label1.configure(font=("candara", 25, "bold italic"), bg="#FF7272", fg="#FFF")
            self._label1.pack(pady=(40, 33))
            self.regwindowOpen = True

        if mode == 2:       # For Updation window
            self._label1 = Label(self._root1, text="UPDATE YOUR DETAILS")
            self._label1.configure(font=("candara", 25, "bold italic"), bg="#FF7272", fg="#FFF")
            self._label1.pack(pady=(40, 33))
            self.updatewindowOpen = True

        self._label2 = Label(self._root1, text="Name ")
        self._label2.configure(font=("calibri", 14, "bold"), bg="#FF7272", fg="#FFF9A9")
        self._label2.pack(pady=(8, 2), padx=(0, 175))

        self._nameInput = Entry(self._root1, font=("times", 10))    # To take name from user while registration
        if mode == 2:
            self._nameInput.insert(0, self.dataList[0][0][1])   # For updation window, the name of the logged in user is already printed on the name input field
        self._nameInput.pack(pady=(5, 10), ipady=4, ipadx=50)

        self._label3 = Label(self._root1, text="Email-id ")
        self._label3.configure(font=("calibri", 14, "bold"), bg="#FF7272", fg="#FFF9A9")
        self._label3.pack(pady=(8, 2), padx=(0, 158))

        self.__emailInput = Entry(self._root1, font=("times", 10))  # To take email-id from user while registration
        if mode == 2:
            self.__emailInput.insert(0, self.dataList[0][0][2]) # For updation window, the email of the logged in user is already printed on the name input field
        self.__emailInput.pack(pady=(5, 10), ipady=4, ipadx=50)

        self._label4 = Label(self._root1, text="Password ")
        self._label4.configure(font=("calibri", 14, "bold"), bg="#FF7272", fg="#FFF9A9")
        self._label4.pack(pady=(8, 2), padx=(0, 145))

        self.__passwordInput = Entry(self._root1, font=("times", 10), show="*")
        if mode == 2:
            self.__passwordInput.insert(0, self.dataList[0][0][3])  # For updation window, the password of the logged in user is already printed on the name input field
        self.__passwordInput.pack(pady=(5, 20), padx=(9, 56), ipady=4, ipadx=26)

        viewBtn = Button(self._root1, font=("times", 10), text="SHOW", height=1, width=5, bg="#02032E", fg="#fff",
                              command=lambda:self.viewHidePassword(self.__passwordInput, viewBtn, mode="show"))
        viewBtn.place(x=268, y=326)     # This button is used to show or hide the password

        self._ageInput = Entry(self._root1, font=("times", 10), fg="#807FB4", justify="center")
        self._label5 = Label(self._root1, text="Age : ", font=("times", 10), fg="#807FB4", bg="#fff")
        if mode == 1:
            self._ageInput.insert(0, "Age")     # Placeholder of age
            self._ageInput.bind("<FocusIn>", clearPlaceholder)
            self._ageInput.bind("<FocusOut>", returnPlaceholderAge)
        if mode == 2:
            self._ageInput.insert(0, self.dataList[0][0][4])    # For updation window, the age of the logged in user is already printed on the name input field
            self._label5.place(x=90, y=375)
        self._ageInput.pack(pady=(0, 20), ipady=4, ipadx=50)

        self._genderInput = Entry(self._root1, font=("times", 10), fg="#807FB4", justify="center")
        self._label6 = Label(self._root1, text="Gender : ", font=("times", 10), fg="#807FB4", bg="#fff")
        if mode == 1:
            self._genderInput.insert(0, "Gender")   # Placeholder for gender
            self._genderInput.bind("<FocusIn>", clearPlaceholder)
            self._genderInput.bind("<FocusOut>", returnPlaceholderGender)
        if mode == 2:
            self._genderInput.insert(0, self.dataList[0][0][5]) # For updation window, the gender of the logged in user is already printed on the name input field
            self._label6.place(x=90, y=422)
        self._genderInput.pack(pady=(0, 20), ipady=4, ipadx=50)

        self._cityInput = Entry(self._root1, font=("times", 10), fg="#807FB4", justify="center")
        self._label7 = Label(self._root1, text="City : ", font=("times", 10), fg="#807FB4", bg="#fff")
        if mode == 1:
            self._cityInput.insert(0, "City")   # Placeholder for city
            self._cityInput.bind("<FocusIn>", clearPlaceholder)
            self._cityInput.bind("<FocusOut>", returnPlaceholderCity)
        if mode == 2:
            self._cityInput.insert(0, self.dataList[0][0][7])   # For updation window, the city of the logged in user is already printed on the name input field
            self._label7.place(x=90, y=469)
        self._cityInput.pack(pady=(0, 20), ipady=4, ipadx=50)

        self._bioInput = Entry(self._root1, font=("times", 10), fg="#807FB4", justify="center")
        self._label8 = Label(self._root1, text="About : ", font=("times", 10), fg="#807FB4", bg="#fff")
        if mode == 1:
            self._bioInput.insert(10, "About")  # Placeholder for bio
            self._bioInput.bind("<FocusIn>", clearPlaceholder)
            self._bioInput.bind("<FocusOut>", returnPlaceholderAbout)
        if mode == 2:
            self._bioInput.insert(0, self.dataList[0][0][8])    # For updation window, the bio of the logged in user is already printed on the name input field
            self._label8.place(x=90, y=516)
        self._bioInput.pack(pady=(0, 20), ipady=4, ipadx=50)

        if mode == 1:
            self._registerBtn = Button(self._root1, text="Register", width=12, height=1, font=("times", 12, "bold"), bg="#02032E", fg="#fff",
                                       command=lambda: regHandler(self._nameInput.get(), self.__emailInput.get(),
                                                                  self.__passwordInput.get(), self._ageInput.get(),
                                                                  self._genderInput.get(), self._cityInput.get(),
                                                                  self._bioInput.get()))   # After clicking the button the control goes to the regHandler() method of tinder.py and completes registration
            self._registerBtn.pack()

        if mode == 2:
            self._updateBtn = Button(self._root1, text="Update", width=12, height=1, font=("times", 12, "bold"), bg="#02032E", fg="#fff",
                                     command=lambda: updateHandler(self._nameInput.get(), self.__emailInput.get(),
                                                                  self.__passwordInput.get(), self._ageInput.get(),
                                                                  self._genderInput.get(), self._cityInput.get(),
                                                                  self._bioInput.get()))    # After clicking the button the control goes to the updateHandler() method of tinder.py and completes updation
            self._updateBtn.pack()

        self._root1.mainloop()


    def clearScreen(self):
        # This method is used to clear the GUI window i.e. to destroy all the components of the GUI window
        for i in self._root.pack_slaves():
            i.destroy()

        for i in self._root.grid_slaves():
            i.destroy()

        for i in self._root.place_slaves():
            i.destroy()


    def headerMenu(self, other, data, mode, regHandler, updateHandler, num):
        # This method creates the menubar contains "Home" and "Proposals"
        self._menu = Menu(self._root)
        self._root.config(menu=self._menu)
        filemenu = Menu(self._menu)
        self._menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda: self.mainWindow(other, data, 1, regHandler, updateHandler, 0))
        filemenu.add_command(label="Edit Profile", command=lambda: self.regWindow(regHandler, updateHandler, 2))
        filemenu.add_command(label="View Profile", command=lambda: other.viewUsers(0))
        filemenu.add_command(label="LogOut", command=lambda: other.logoutHandler())

        helpmenu = Menu(self._menu)
        self._menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals", command=lambda: other.proposalHandler(self.dataList[0][0][0], 1))
        helpmenu.add_command(label="My Requests", command=lambda: other.requestHandler(self.dataList[0][0][0], 2))
        helpmenu.add_command(label="My Matches", command=lambda: other.matchHandler(self.dataList[0][0][0], 3))


    def clearMenu(self):
        # This method delete the menubar
        self._menu.delete(0, END)


    def mainWindow(self, other, data, mode, regHandler, updateHandler, num=0):
        # This window is "My Profile" window when mode=1 and "View Profile" window when mode=2
        self.clearScreen()

        self.dataList.append(data)
        self.headerMenu(other, self.dataList[0], mode, regHandler, updateHandler, num)

        if data[0][5] == "Female":
            self.profilePic = PhotoImage(file="image/NobodyFemale.png")
            self.profilePic = self.profilePic.zoom(15)
            self.profilePic = self.profilePic.subsample(50)
        else:
            self.profilePic = PhotoImage(file="image/NobodyMale.png")
            self.profilePic = self.profilePic.zoom(15)
            self.profilePic = self.profilePic.subsample(80)
        self._labelProfilePic = Label(self._root, image=self.profilePic, bg="#FF7272", width=600, justify="center")
        self._labelProfilePic.pack(pady=(30, 0))

        name = data[0][1].upper()
        self._label2 = Label(self._root, text=name)
        self._label2.config(font=("candara", 14, "bold"), fg="white", bg="#FF7272", width=600, justify="center")
        self._label2.pack(pady=(10, 0))

        self._label3 = Label(self._root, text="Age: ")
        self._label3.config(font=("candara", 14, "bold"), fg="white", bg="#FF7272")
        self._label3.place(x=100, y=210)

        age = data[0][4]
        self._label4 = Label(self._root, text=str(age))
        self._label4.config(font=("calibri", 14, "bold"), fg="white", bg="#FF7272")
        self._label4.place(x=255, y=210)

        self._label5 = Label(self._root, text="Not interested in: ")
        self._label5.config(font=("candara", 14, "bold"), fg="white", bg="#FF7272")
        self._label5.place(x=100, y=250)

        gender = data[0][5]
        self._label6 = Label(self._root, text=gender)
        self._label6.config(font=("calibri", 14, "bold"), fg="white", bg="#FF7272")
        self._label6.place(x=255, y=250)

        if mode == 1:
            city = data[0][7]
            self._label7 = Label(self._root, text="From "+city)
            self._label7.config(font=("calibri", 14, "bold"), fg="white", bg="#FF7272")
            self._label7.place(x=100, y=290)

            bio = data[0][8]
            self._label8 = Label(self._root, text="***   "+bio+"   ***")
            self._label8.config(font=("calibri", 14, "bold"), fg="white", bg="#FF7272", width=600, justify="center")
            self._label8.pack(pady=(160, 0))
        elif mode == 2:
            btn1 = Button(self._root, text="Previous", font=("times", 12, "bold"), fg="#fff", bg="#02032E",
                          height=1, width=7, command=lambda: other.viewUsers(num-1))
            btn1.place(x=75, y=300)
            btn2 = Button(self._root, text="Propose", font=("times", 12, "bold"), fg="#fff", bg="#02032E",
                          height=1, width=7, command=lambda: other.propose(data[0][0]))
            btn2.place(x=160, y=300)
            btn3 = Button(self._root, text="Next", font=("times", 12, "bold"), fg="#fff", bg="#02032E",
                          height=1, width=7, command=lambda: other.viewUsers(num+1))
            btn3.place(x=244, y=300)


    def myProposalRequsetWindow(self, other, response, mode):
        # This window is "My Proposals" window when mode=1, "My Requests" window when mode=2 and "My Macthes" window when mode=3
        proposalCount = 0
        buttonView = []

        labelHead = Label(self._root, font=("candara", 25, "bold italic"), bg="#FF7272", fg="#FFF", width=600,
                          justify="center")
        if mode == 1:
            labelHead.configure(text="SENT PROPOSALS")
        elif mode == 2:
            labelHead.configure(text="RECEIVED REQUESTS")
        else:
            labelHead.configure(text="MY MATCHES")
        labelHead.pack(pady=(17, 0))

        if len(response) == 0:
            self.emptyImage = PhotoImage(file="image/empty.png")
            self.emptyImage = self.emptyImage.zoom(10).subsample(35)
            self.labelEmpty = Label(self._root, width=600, justify="center", image=self.emptyImage, bg="#FF7272")
            self.labelEmpty.pack(pady=(120, 0))

            labelWarning = Label(self._root, font=("Arial", 19, "bold"), width=600, justify="center", bg="#FF7272",
                                 fg="#02032E")
            if (mode == 1):
                labelWarning.config(text="No Proposal Sent!")
            elif (mode == 2):
                labelWarning.config(text="No Request Received!")
            else:
                labelWarning.config(text="Oops!\nNo Match Found...")
            labelWarning.pack(pady=(0, 0))

        else:
            for i in response:
                proposalCount += 1

                frame = Frame(self._root, height = 40, width=600, bg="#FFF9A9")
                frame.place(x=5, y=80+(proposalCount-1)*51)

                label1 = Label(frame, text=str(proposalCount)+".", font=("times", 15, "bold"), fg="black", bg="#FFF9A9")
                label1.place(x=15, y=3)

                label2 = Label(frame, text=i[1].upper(), font=("times", 15, "bold"), fg="black", bg="#FFF9A9")
                label2.place(x=35, y=3)

                buttonView.append(Button(frame, text="View", width=9, bg="#005163", fg="#FFF", font=("times", 11, "bold"),
                                        command=lambda j=i: other.viewProposalWindowHandler(j)))
                buttonView[proposalCount-1].place(x=300, y=6)

                frame2 = Frame(self._root, height=3, width=600, bg="#FFF9A9")
                frame2.place(x=0, y=72+proposalCount*51)


    def viewProposalWindow(self, name, gender, age, city, bio):
        # This window shows the details of the user of either my proposals or my requests or my matches
        self.clearScreen()

        if gender == "Female":
            self.profilePic = PhotoImage(file="image/NobodyFemale.png")
            self.profilePic = self.profilePic.zoom(15)
            self.profilePic = self.profilePic.subsample(50)
        else:
            self.profilePic = PhotoImage(file="image/NobodyMale.png")
            self.profilePic = self.profilePic.zoom(15)
            self.profilePic = self.profilePic.subsample(80)
        self._labelProfilePic = Label(self._root, image=self.profilePic, bg="#FF7272", width=600, justify="center")
        self._labelProfilePic.pack(pady=(40, 0))

        label3 = Label(self._root, text=name.upper(), font=("times", 16, "bold"), fg="white", bg="#FF7272", width=600,
                       justify="center")
        label3.pack(pady=(10, 0))

        label4 = Label(self._root, text="Gender:", font=("times", 16), fg="white", bg="#FF7272")
        label4.place(x=120, y=300)

        label5 = Label(self._root, text=gender, font=("times", 16, "bold"), fg="white", bg="#FF7272")
        label5.place(x=200, y=300)

        label6 = Label(self._root, text="Age:", font=("times", 16), fg="white", bg="#FF7272")
        label6.place(x=120, y=340)

        label7 = Label(self._root, text=age + " years", font=("times", 16, "bold"), fg="white", bg="#FF7272")
        label7.place(x=200, y=340)

        label8 = Label(self._root, text="Lives in " + city, font=("times", 16), fg="white", bg="#FF7272")
        label8.place(x=120, y=380)

        label9 = Label(self._root, text="***   "+bio+"   ***", font=("calibri", 16, "bold italic"), fg="white",
                       bg="#FF7272", width=600, justify="center")
        label9.pack(pady=(30, 0))


    def printMessage(self, title, msg, type):
        if type == 0:
            messagebox.showerror(title, msg)  # this message is an error message when type=0
        elif type == 1:
            messagebox.showinfo(title, msg)  # this message is a info when type=1


    def viewHidePassword(self, password, viewBtn, mode):
        # This method is used to give a functionality to a button to hide or show password
        __password = password.get()
        passwordInput= password

        if mode=="show":
            viewBtn.configure(text="HIDE", command=lambda: self.viewHidePassword(passwordInput, viewBtn, mode="hide"))
            passwordInput.delete(0, END)
            passwordInput.insert(0, __password)
            passwordInput.configure(show="")
        elif mode=="hide":
            viewBtn.configure(text="SHOW", command=lambda: self.viewHidePassword(passwordInput, viewBtn, mode="show"))
            passwordInput.configure(show="*")
