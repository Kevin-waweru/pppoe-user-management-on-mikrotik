from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from librouteros import connect
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem,QSplashScreen,QLabel
from PyQt5.QtGui import QColor
from twilio.rest import Client
import mysql.connector
import sqlite3
import traceback  # Helps in debugging errors
import os
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

    

connection=connect(
    
            username='admin',
            password='1111',
            host='192.168.88.1')
   
        



def clear(self):
    self.name.clear()
    self.username.clear()
    self.lineEdit_2.clear()

    self.location.clear()
    self.packagename.clear()
    self.localaddress.clear()
    self.dns.clear
    
    self.txrx.clear()

def msg(title,text):
    mes=QMessageBox()
    mes.setWindowTitle(title)
    mes.setText(text)
    mes.setStandardButtons(QMessageBox.Ok)
    mes.exec_()

def connectrt(self):
    
     try:
        
    
        
     
        
        pppoe_secrets = list(
                connection.path('ppp', 'secret').select('name', 'password', 'profile', 'caller-id')
            )

            # Fetch active PPPoE connections
        pppoe_active = {
                entry['name']: entry for entry in connection.path('ppp', 'active').select('name', 'address', 'uptime')
            }

            # Set the row count for the table widget
        self.totaluserslbl.setText(str(len(pppoe_secrets)))
            # Populate the table
        
        print(pppoe_secrets)

     except Exception as e:
                print(f"Error fetching PPPoE data: {e}")


 
def combo(self):
        packages=connection.path('ppp','profile',).select('name')
        for package in packages:

            self.packagecombo.addItem(package['name'])
            self.removepackagecombo.addItem(package['name'])
def combonum(self):
        users=connection.path('ppp','secret',).select('caller-id')
        for user in users:

            self.numbercombo.addItem(str(user['caller-id']))
                                      
def ques(self):
        try:
            quees=connection.path('queue','simple').select('name')
            for quee in quees:
                self.parentqueuecombo.addItem(quee['name'])
        except Exception as e:
            print(e)
def pools(self):
        try:
            pools1=connection.path('ip','pool',).select('name')
            for pool in pools1:
                self.remoteaddresscombo.addItem(pool['name'])
                
        except Exception as e:
            print(e)
def protocols(self):
         try:
                encryption_options = ["none", "required", "optional", "default"]

                self.protocolcombo.addItems(sorted(encryption_options))
         except Exception as e:
          print(f"Error fetching protocols: {e}")




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1233, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('background-color: rgb(142, 185, 255)')
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 20, 1250, 771))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet('border-color:rgb(142, 185, 255)')
        self.customermanagementtab = QtWidgets.QWidget()
        self.customermanagementtab.setObjectName("customermanagementtab")
        self.tableWidget = QtWidgets.QTableWidget(self.customermanagementtab)
        self.tableWidget.setGeometry(QtCore.QRect(200, 350, 800, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(4)
        self.tableWidget.itemSelectionChanged.connect(self.selec)
        self.tableWidget.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.bandwidthusagelbl = QtWidgets.QLabel(self.customermanagementtab)
        self.bandwidthusagelbl.setGeometry(QtCore.QRect(900, 40, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bandwidthusagelbl.setFont(font)
        self.bandwidthusagelbl.setObjectName("loadlbl")
        self.loadlbl = QtWidgets.QLabel(self.customermanagementtab)
        self.loadlbl.setGeometry(QtCore.QRect(550, 40, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.loadlbl.setFont(font)
        self.loadlbl.setObjectName("bandwidthusagelbl")
        #self.adduserbtn = QtWidgets.QPushButton(self.customermanagementtab)
        #self.adduserbtn.setGeometry(QtCore.QRect(130, 270, 75, 23))
        #self.adduserbtn.setObjectName("adduserbtn")
        #self.adduserbtn.clicked.connect(self.adduser)
        #self.adduserbtn.isEnabled
        self.disconnectuserbtn = QtWidgets.QPushButton(self.customermanagementtab)
        self.disconnectuserbtn.setGeometry(QtCore.QRect(240, 610, 91, 23))
        self.disconnectuserbtn.setObjectName("disconnectuserbtn")
        self.disconnectuserbtn.clicked.connect(self.disconnectuser)
        self.disconnectuserbtn.setStyleSheet('background-color: rgb(142, 221, 255)')
        self.removeuserbtn = QtWidgets.QPushButton(self.customermanagementtab)
        self.removeuserbtn.setGeometry(QtCore.QRect(470, 610, 75, 23))
        self.removeuserbtn.setObjectName("removeuserbtn")
        self.removeuserbtn.clicked.connect(self.removeuser)
        self.edituserbtn = QtWidgets.QPushButton(self.customermanagementtab)
        self.edituserbtn.setStyleSheet('background-color: rgb(142, 221, 255)')
        self.edituserbtn.setGeometry(QtCore.QRect(700, 610, 110, 23))
        self.edituserbtn.setObjectName("reconnectuser")
        self.edituserbtn.clicked.connect(self.reconnectuser)
        self.removeuserbtn.setStyleSheet('background-color: rgb(142, 221, 255)')
        self.refreshpagebtn = QtWidgets.QPushButton(self.customermanagementtab)
        self.refreshpagebtn.setGeometry(QtCore.QRect(630, 10, 75, 23))
        self.refreshpagebtn.setObjectName("refreshpagebtn")
        self.refreshpagebtn.clicked.connect(self.refresh)
        self.refreshpagebtn.setStyleSheet('background-color: rgb(142, 221, 255)')
        self.userinfobox = QtWidgets.QGroupBox(self.customermanagementtab)
        self.userinfobox.setGeometry(QtCore.QRect(80, 60, 391, 251))
        self.userinfobox.setObjectName("userinfobox")
        self.location = QtWidgets.QLineEdit(self.userinfobox)
        self.location.setGeometry(QtCore.QRect(100, 170, 113, 20))
        self.location.setObjectName("location")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.userinfobox)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.name = QtWidgets.QLineEdit(self.userinfobox)
        self.name.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.name.setObjectName("name")
        self.username = QtWidgets.QLineEdit(self.userinfobox)
        self.username.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.username.setObjectName("username")
        self.namelbl = QtWidgets.QLabel(self.userinfobox)
        self.namelbl.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.namelbl.setObjectName("namelbl")
        self.usernamelbl = QtWidgets.QLabel(self.userinfobox)
        self.usernamelbl.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.usernamelbl.setObjectName("usernamelbl")
        self.passwordlbl = QtWidgets.QLabel(self.userinfobox)
        self.passwordlbl.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.passwordlbl.setObjectName("passwordlbl")
        self.packagelbl = QtWidgets.QLabel(self.userinfobox)
        self.packagelbl.setGeometry(QtCore.QRect(20, 140, 47, 13))
        self.packagelbl.setObjectName("packagelbl")
        self.packagecombo = QtWidgets.QComboBox(self.userinfobox)
        self.packagecombo.setGeometry(QtCore.QRect(100, 140, 111, 22))
        self.packagecombo.setObjectName("packagecombo")
        self.locationlbl = QtWidgets.QLabel(self.userinfobox)
        self.locationlbl.setGeometry(QtCore.QRect(20, 170, 47, 13))
        self.locationlbl.setObjectName("locationlbl")
        self.servicelbl = QtWidgets.QLabel(self.userinfobox)
        self.servicelbl.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.servicelbl.setObjectName("servicelbl")
        self.servicecombo = QtWidgets.QComboBox(self.userinfobox)
        self.servicecombo.setGeometry(QtCore.QRect(100, 110, 111, 22))
        self.servicecombo.setObjectName("servicecombo")
        self.servicecombo.addItem('pppoe')
        self.totaluserslbl = QtWidgets.QLabel(self.customermanagementtab)
        self.totaluserslbl.setGeometry(QtCore.QRect(950, 110, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.totaluserslbl.setFont(font)
        self.totaluserslbl.setObjectName("totaluserslbl")
        self.finduserbtn = QtWidgets.QPushButton(self.customermanagementtab)
        self.finduserbtn.setGeometry(QtCore.QRect(340, 270, 75, 23))
        self.finduserbtn.setObjectName("finduserbtn")
        self.finduserbtn.clicked.connect(self.adduser)
        self.finduserbtn.setStyleSheet('background-color: rgb(142, 221, 255)')
        self.tabWidget.addTab(self.customermanagementtab, "")
        self.networmanagementtab = QtWidgets.QWidget()
        self.networmanagementtab.setObjectName("networmanagementtab")
        self.addpackanebox = QtWidgets.QGroupBox(self.networmanagementtab)
        self.addpackanebox.setGeometry(QtCore.QRect(20, 40, 271, 401))
        self.addpackanebox.setObjectName("addpackanebox")
        self.addpacknamelbl = QtWidgets.QLabel(self.addpackanebox)
        self.addpacknamelbl.setGeometry(QtCore.QRect(20, 20, 27, 13))
        self.addpacknamelbl.setObjectName("addpacknamelbl")
        self.addpacklocaladdresslbl = QtWidgets.QLabel(self.addpackanebox)
        self.addpacklocaladdresslbl.setGeometry(QtCore.QRect(20, 60, 65, 13))
        self.addpacklocaladdresslbl.setObjectName("addpacklocaladdresslbl")
        self.addpacktxrx = QtWidgets.QLabel(self.addpackanebox)
        self.addpacktxrx.setGeometry(QtCore.QRect(20, 210, 80, 13))
        self.addpacktxrx.setObjectName("addpacktxrx")
        self.addpackremoteaddresslbl_2 = QtWidgets.QLabel(self.addpackanebox)
        self.addpackremoteaddresslbl_2.setGeometry(QtCore.QRect(20, 90, 78, 13))
        self.addpackremoteaddresslbl_2.setObjectName("addpackremoteaddresslbl_2")
        self.addpackdns = QtWidgets.QLabel(self.addpackanebox)
        self.addpackdns.setGeometry(QtCore.QRect(20, 130, 54, 16))
        self.addpackdns.setObjectName("addpackdns")
        self.addpackprotocol = QtWidgets.QLabel(self.addpackanebox)
        self.addpackprotocol.setGeometry(QtCore.QRect(20, 170, 100, 13))
        self.addpackprotocol.setObjectName("addpackprotocol")
        self.addpackparentqueus = QtWidgets.QLabel(self.addpackanebox)
        self.addpackparentqueus.setGeometry(QtCore.QRect(20, 260, 67, 13))
        self.addpackparentqueus.setObjectName("addpackparentqueus")
        self.remoteaddresscombo = QtWidgets.QComboBox(self.addpackanebox)
        self.remoteaddresscombo.setGeometry(QtCore.QRect(120, 90, 111, 22))
        self.remoteaddresscombo.setObjectName("remoteaddresscombo")
        self.parentqueuecombo = QtWidgets.QComboBox(self.addpackanebox)
        self.parentqueuecombo.setGeometry(QtCore.QRect(120, 260, 111, 22))
        self.parentqueuecombo.setObjectName("parentqueuecombo")
        self.txrx = QtWidgets.QLineEdit(self.addpackanebox)
        self.txrx.setGeometry(QtCore.QRect(120, 210, 113, 20))
        self.txrx.setObjectName("txrx")
        self.packagename = QtWidgets.QLineEdit(self.addpackanebox)
        self.packagename.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.packagename.setObjectName("packagename")
        self.localaddress = QtWidgets.QLineEdit(self.addpackanebox)
        self.localaddress.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.localaddress.setObjectName("localaddress")
        self.dns = QtWidgets.QLineEdit(self.addpackanebox)
        self.dns.setGeometry(QtCore.QRect(120, 130, 113, 20))
        self.dns.setObjectName("dns")
        self.protocolcombo = QtWidgets.QComboBox(self.addpackanebox)
        self.protocolcombo.setGeometry(QtCore.QRect(120, 165, 111, 22))
        self.protocolcombo.setObjectName("protocolcombo")
        self.addpackagebtn = QtWidgets.QPushButton(self.addpackanebox)
        self.addpackagebtn.setGeometry(QtCore.QRect(110, 350, 75, 23))
        self.addpackagebtn.setObjectName("addpackagebtn")
        self.addpackagebtn.clicked.connect(self.addpack)
        self.addpackagebtn.setStyleSheet('background-color: rgb(142, 221, 255)')
        self.removepackagebox = QtWidgets.QGroupBox(self.networmanagementtab)
        self.removepackagebox.setGeometry(QtCore.QRect(460, 40, 220, 170))
        self.removepackagebox.setObjectName("removepackagebox")
        self.removepacknamelbl = QtWidgets.QLabel(self.removepackagebox)
        self.removepacknamelbl.setGeometry(QtCore.QRect(10, 40, 27, 13))
        self.removepacknamelbl.setObjectName("removepacknamelbl")
        self.removepackagecombo = QtWidgets.QComboBox(self.removepackagebox)
        self.removepackagecombo.setGeometry(QtCore.QRect(70, 40, 111, 22))
        self.removepackagecombo.setObjectName("removepackagecombo")
        self.removepackagecombo.addItem('None')
        self.removepackagebtn = QtWidgets.QPushButton(self.removepackagebox)
        self.removepackagebtn.setGeometry(QtCore.QRect(100, 110, 75, 23))
        self.removepackagebtn.setObjectName("removepackagebtn")
        self.removepackagebtn.clicked.connect(self.remove)
        self.removepackagebtn.setStyleSheet('background-color: rgb(142, 221, 255)')
        self.notificationbox = QtWidgets.QGroupBox(self.networmanagementtab)
        self.notificationbox.setGeometry(QtCore.QRect(820, 40, 260, 170))
        self.notificationbox.setObjectName("notificationbox")
        self.removepackagebtn_2 = QtWidgets.QPushButton(self.notificationbox)
        self.removepackagebtn_2.setGeometry(QtCore.QRect(100, 130, 75, 23))
        self.removepackagebtn_2.setObjectName("removepackagebtn_2")
        self.removepackagebtn_2.setStyleSheet('background-color: rgb(142, 221, 255)')
        self.removepackagebtn_2.clicked.connect(self.text)
        self.message = QtWidgets.QTextEdit(self.notificationbox)
        self.message.setGeometry(QtCore.QRect(23, 20, 215, 70))
        self.message.setObjectName("message")
        self.numbercombolbl = QtWidgets.QLabel(self.notificationbox)
        self.numbercombolbl.setGeometry(QtCore.QRect(20, 99, 80, 13))
        self.numbercombolbl.setObjectName("addpacknamelbl")
        self.numbercombo = QtWidgets.QComboBox(self.notificationbox)
        self.numbercombo.setGeometry(QtCore.QRect(100, 95, 138, 20))
        self.numbercombo.setObjectName("removepackagecombo")
        self.numbercombo.addItem('None')
        self.tabWidget.addTab(self.networmanagementtab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.name.hide()
        self.namelbl.hide()
        self.name.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.username.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.localaddress.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.location.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.servicecombo.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.packagecombo.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.lineEdit_2.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.packagename.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.remoteaddresscombo.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.dns.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.protocolcombo.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.removepackagecombo.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.message.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.numbercombo.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.parentqueuecombo.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.txrx.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_ether1_status)
        self.timer.start(10000)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.populate)
        self.timer1.start(5000)
        pools(self)
        ques(self)
        protocols(self)
        combo(self)
        self.populate()
        combonum(self)
        self.send()
        #self.throughput()
    
    def refresh(self):
        self.send()
        pools(self)
        ques(self)
        protocols(self)
        combo(self)
        connectrt(self)
        self.populate()
        clear(self)
        self.packagecombo.setCurrentIndex(0)
        self.dns.clear()
        self.removepackagecombo.setCurrentIndex(0)
        combo
        self.remoteaddresscombo.setCurrentIndex(0)
        self.protocolcombo.setCurrentIndex(0)
   
    
    def throughput(self):
     try:
      
        interfaces = connectrt.connection.path('interface' ).select('name', 'rx-byte-rate', 'tx-byte-rate')
        # Loop through the interfaces to find the specified one
        for interface in interfaces:
            if interface['name'] == 'bridge':
                # Extract received and transmitted bytes
                rx_bytes = int(interface.get('rx-byte', 0))  # Received bytes
                tx_bytes = int(interface.get('tx-byte', 0))  # Transmitted bytes
                
                # Print the throughput information
                print(f"Received bytes: {rx_bytes}")
                print(f"Transmitted bytes: {tx_bytes}")
                self.bandwidthusagelbl.setText(f"Rx = {rx_bytes} TX = {tx_bytes}")
                # Return the throughput values
                return rx_bytes, tx_bytes
                
        
        # If the specified interface is not found, print a message
    
     except Exception as e:
        print(f"Error fetching throughput: {e}")

    def selec(self):
     try:
      selectedrow=self.tableWidget.currentRow()
      if selectedrow!=-1:
        name=self.tableWidget.item(selectedrow,0).text()
        password=self.tableWidget.item(selectedrow,1).text()
        profile=self.tableWidget.item(selectedrow,2).text()


        self.username.setText(name)
        self.packagecombo.setCurrentText(profile)
        self.lineEdit_2.setText(password)
     except Exception as e:
        title='Unable to make selection'
        text=str(e)
        msg(title,text)
    
    def remove(self):
     try:
        profile=self.removepackagecombo.currentText()
        packages=connection.path('ppp','profile').select('name','.id')
        reply = QMessageBox.question(
            None, "Confirm Removal", 
            f"Are you sure you want to remove the profile '{profile}'?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            for package in packages:
                if package.get('name') == profile:
                    connection.path('ppp', 'profile').remove(package['.id'])
                    title = "Success"
                    text = f"{profile} successfully removed"
                    msg(title, text)
                     
                    self.removepackagecombo.setCurrentIndex(0)
                    return

                
            
            # If no matching profile is found
            msg("Error", f"Profile '{profile}' not found.")
     except Exception as e:
         title="Error cannot remove package"
         text=str(e)
         msg(title,text)
       
    def removeuser(self):

     try:
        use=self.username.text()
        users=connection.path('ppp','secret').select('name','.id')
        
        reply = QMessageBox.question(
            None, "Confirm Removal", 
            f"Are you sure you want to remove the user '{use}'?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            for user in users:
                if user.get('name') == use:
                    connection.path('ppp', 'secret').remove(user['.id'])
                    title = "Success"
                    text = f"User '{use}' successfully removed"
                    msg(title, text)
                    return  # Exit function after removing
                
            # If no matching user is found
            msg("Error", f"User '{use}' not found.")
     except Exception as e:
         title="Error cannot remove  user"
         text=str(e)
         msg(title,text)
    def reconnectuser(self):
       try:
        use = self.username.text()  # Get the username from the input field

        # Check if the user exists in the secret list
        users = connection.path('ppp', 'secret').select('name', '.id', 'disabled')
        user_found = False

        for user in users:
            if user.get('name') == use:
                user_found = True
                
                # Enable the user's secret if disabled
                if user.get('disabled') == 'true':
                    connection.path('ppp', 'secret').update(id=user['.id'], disabled='false')
                    print(f"User {use} has been re-enabled.")

                # Disconnect active session to force reconnection
                active_users = connection.path('ppp', 'active').select('name', '.id')
                for active_user in active_users:
                    if active_user.get('name') == use:
                        connection.path('ppp', 'active').remove(id=active_user['.id'])
                        print(f"User {use} disconnected to allow reconnection.")
                        break
                
                print(f"User {use} is ready to reconnect.")
                break

        if not user_found:
            print("User not found in PPP secret.")
       except Exception as e:
        print(f"Error reconnecting user: {e}")

    def disconnectuser(self):
     try:
        use = self.username.text()
        users = connection.path('ppp', 'secret').select('name', '.id', 'disabled')
        
        user_found = False
        for user in users:
            if user.get('name') == use:
                user_found = True
                
                # Check if the user is already disconnected
                if user.get('disabled') == 'true':
                    title = "User Already Disconnected"
                    text = f'{use} is already disconnected.'
                    msg(title, text)
                    return
                
                # Confirmation Message Box for disconnection
                reply = QMessageBox.question(
                    None, "Confirm Disconnection", 
                    f"Are you sure you want to disconnect the user '{use}'?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )
                
                if reply == QMessageBox.Yes:
                    # Disconnect user by setting disabled to 'yes'
                    connection.path('ppp', 'secret').update(
                        **{'.id': user['.id'], 'disabled': 'yes'}
                    )
                    active_sessions = connection.path('ppp', 'active').select('name', '.id')
                    for session in active_sessions:
                        if session.get('name') == use:
                            connection.path('ppp', 'active').remove( session['.id'])
                            break  # Stop after removing the session
                    title = "User Disconnected"
                    text = f"{use} successfully disconnected."
                    msg(title, text)
                else:
                    print("Action canceled by the user.")
                break

        if not user_found:
            # User not found in the list of PPP secrets
            title = "User Not Found"
            text = f"User {use} was not found."
            msg(title, text)
            print(f"User {use} not found in the PPP secret.")

     except Exception as e:
        # Handle any exceptions
        title = "Error Disconnecting User"
        text = str(e)
        msg(title, text)
        print(f"Error: {e}")
    def reconnectuser(self):
     try:
        use = self.username.text()
        users = connection.path('ppp', 'secret').select('name', '.id', 'disabled')
        
        # Check if the user exists and is disconnected
        user_found = False
        for user in users:
            if user.get('name') == use:
                user_found = True
                
                # Check if the user is disconnected (disabled == 'true')
                if user.get('disabled') == True:
                    # Confirmation Message Box for reconnecting
                    reply = QMessageBox.question(
                        None, "Confirm Reconnection", 
                        f"Are you sure you want to reconnect the user '{use}'?",
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                    )
                    
                    if reply == QMessageBox.Yes:
                        # Reconnect user by setting disabled to 'no'
                        connection.path('ppp', 'secret').update(
                            **{'.id': user['.id'], 'disabled': 'no'}
                        )
                        title = "User Reconnected"
                        text = f'{use} has been successfully reconnected.'
                        msg(title, text)
                    else:
                        print("Action canceled by the user.")
                else:
                    title = "User Already Connected"
                    text = f'{use} is already connected.'
                    msg(title, text)
                break
        
        if not user_found:
            # User not found in the list of PPP secrets
            title = "User Not Found"
            text = f"User {use} was not found."
            msg(title, text)
            print(f"User {use} not found in the PPP secret.")

     except Exception as e:
        # Handle any exceptions
        title = "Error Reconnecting User"
        text = str(e)
        msg(title, text)
        print(f"Error: {e}")
    
    




    def adduser(self):
        name = self.name.text().strip()
        username = self.username.text().strip()
        package = self.packagecombo.currentText().strip()
        phone = self.location.text().strip()  # Changed from 'location' for clarity
        password1 = self.lineEdit_2.text().strip()

        try:
            # Debugging: Check if required fields are empty
            

            # Connect to SQLite database
            db = sqlite3.connect("mikro.db")  # SQLite file database
            cur = db.cursor()

            # Ensure the users table exists
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL UNIQUE
                   
                )
            """)
            db.commit()

            # Debugging: Check if MikroTik connection exists
            if 'connection' not in globals():
                msg("Error", "MikroTik connection not initialized!")
                return

            # Add user to MikroTik
            connection.path('ppp', 'secret').add(
                name=username,
                service='pppoe',
                profile=package,
                password=password1
            )

            # Insert user into SQLite database
            cur.execute("INSERT INTO users (name, phone) VALUES (?, ?)", (username, phone))
            db.commit()

            # Success message
            msg("Success", f"{username} successfully added")
            clear(self) 

            cur.close()
            db.close()  # Ensure connection closes properly

        except sqlite3.IntegrityError:
            msg("Database Error", "A user with this phone number already exists.")

        except sqlite3.Error as e:
            msg("Database Error", f"SQLite Error: {str(e)}")
            print(traceback.format_exc())  # Logs error details
        except Exception as e:
            title = "Error adding User"
            text = str(e)
            msg(title, text)
            print(f"Error: {e}")
            clear(self)

    
    def send(self):
        db = sqlite3.connect("mikro.db")  
        cur = db.cursor()
        cur.execute("SELECT name, phone FROM users")
        user_data = cur.fetchall()

        cur.close()
        db.close()

        self.numbercombo.clear()

        if user_data:
            for row in user_data:
                name = row[0] if row[0] else "Unknown"  # Handle missing names
                phone = row[1] if row[1] else "No phone"
                self.numbercombo.addItem(f"{name} - {phone}")  
        else:
            self.numbercombo.addItem("No users found")



        
    def populate(self):
        try:
            
            secrets = list(connection.path('ppp', 'secret').select('name', 'password', 'profile', 'last-logged-out', 'disabled'))
            active_users = list(connection.path('ppp', 'active').select('name', 'uptime'))

            # Extract active usernames for comparison
            active_names = {user.get('name', ''): user.get('uptime', '') for user in active_users}

            self.tableWidget.setRowCount(len(secrets))
            self.tableWidget.setColumnCount(5)

            self.tableWidget.setHorizontalHeaderLabels(["Username", "Password", "Profile","Uptime","Disconnected"])
            for row, secret in enumerate(secrets):
                name = str(secret.get('name', ''))
                password = str(secret.get('password', ''))
                profile = str(secret.get('profile', ''))
                last_logout = str(secret.get('last-logged-out', ''))

                # Determine if user is online
                status = str(secret.get('disabled', ''))
                if name in active_names:
                    uptime = active_names[name]
                else:
                    uptime = "N/A"

                # Populate table
                self.tableWidget.setItem(row, 0, QTableWidgetItem(name))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(password))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(profile))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(uptime))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(status))  # Show offline status if not active



        except Exception as e:
            print(f"Error populating table: {e}")
    
    def addpack(self):
        name=self.packagename.text()
        localaddress=self.localaddress.text()
        remoteaddress=self.remoteaddresscombo.currentText()
        dns=self.dns.text()
        protocol=self.protocolcombo.currentText()
        txrx=self.txrx.text()
        parent=self.parentqueuecombo.currentText()

        
        try:
            connection.path('ppp','profile').add(
                name=name,
                **{'local-address':localaddress},
                **{'remote-address':remoteaddress},
                **{'dns-server':dns},
                **{'rate-limit':txrx},
                **{'use-encryption':protocol}
            )
        
            title="Package added"
            text=f'{name} package added successfully'
            msg(title,text)
            self.refresh()
        except Exception as e:
         title="Error cannot add package"
         text=str(e)
         msg(title,text)
    def text(self,body):
     try:
        number=str(self.numbercombo.currentText())
        num=f'+254{number[-9:]}'
        name=number[0:-9]
        
        
        body=self.message.toPlainText()
        
        print(num)
        self.message.clear()
        self.numbercombo.setCurrentIndex(0)
        client = Vonage(Auth(api_key="e0d9c1a2", api_secret="P3bTJtYkSUZHZoKC"))

        message = SmsMessage(
            to=str(num),
            from_="Vonage APIs",
            text=body
        )

        response: SmsResponse = client.sms.send(message)
        print(response)
        title='Notification Success'
        text=f'Notification sent to {name}'
        msg(title,text)
     except Exception as e:
      title='Notification failed'
      text=f'Notification failed {e}'
      msg(title,text)  
    def check_ether1_status(self):
        
      
        try:
            interfaces = connection.path('interface').select('name', 'running')
            for iface in interfaces:
                if iface.get('name') == 'ether1':
                    running = iface.get('running', 'True')
                    if running == True:
                        print(running)
                        
                    else:
                        self.ether1_disconnected()
                    break  
        except Exception as e:
            print("Error checking ether1 status:", e)
    
        except Exception as e:
            print("Error:", e)
    def ether1_disconnected(self):
       
        QMessageBox.warning(self.centralwidget, "Ether1 Disconnected", "Ether1 interface is disconnected!")
        client = Vonage(Auth(api_key="e0d9c1a2", api_secret="P3bTJtYkSUZHZoKC"))

        message = SmsMessage(
            to="254790535851",
            from_="Vonage APIs",
            text="Critical fault Ether 1 disconnected"
        )

        response: SmsResponse = client.sms.send(message)
        print(response)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Administration Application"))
        self.bandwidthusagelbl.setText(_translate("MainWindow", "Total b/w"))

        self.disconnectuserbtn.setText(_translate("MainWindow", "Disconnect User"))
        self.removeuserbtn.setText(_translate("MainWindow", "Remove User"))
        self.edituserbtn.setText(_translate("MainWindow", "Reconnect User"))
        self.refreshpagebtn.setText(_translate("MainWindow", "Refresh Page"))
        self.userinfobox.setTitle(_translate("MainWindow", "User Information"))
        self.namelbl.setText(_translate("MainWindow", "Name"))
        self.usernamelbl.setText(_translate("MainWindow", "Username"))
        self.passwordlbl.setText(_translate("MainWindow", "Password"))
        self.packagelbl.setText(_translate("MainWindow", "Package"))
        self.locationlbl.setText(_translate("MainWindow", "Contact"))
        self.servicelbl.setText(_translate("MainWindow", "Service"))
        self.totaluserslbl.setText(_translate("MainWindow", "Total users"))
        self.finduserbtn.setText(_translate("MainWindow", "Add User"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customermanagementtab), _translate("MainWindow", "Customer Management"))
        self.addpackanebox.setTitle(_translate("MainWindow", "Add Package"))
        self.addpacknamelbl.setText(_translate("MainWindow", "Name"))
        self.addpacklocaladdresslbl.setText(_translate("MainWindow", "Local address"))
        self.addpacktxrx.setText(_translate("MainWindow", "Bandwidth"))
        self.addpackremoteaddresslbl_2.setText(_translate("MainWindow", "Remote address"))
        self.addpackdns.setText(_translate("MainWindow", "DNS server"))
        self.addpackprotocol.setText(_translate("MainWindow", "Encryption"))
        self.addpackparentqueus.setText(_translate("MainWindow", "Parent Queue"))
        self.addpackagebtn.setText(_translate("MainWindow", "Add"))
        self.removepackagebox.setTitle(_translate("MainWindow", "Remove package"))
        self.removepacknamelbl.setText(_translate("MainWindow", "Name"))
        self.numbercombolbl.setText(_translate("MainWindow", "Phone Number"))

        self.removepackagebtn.setText(_translate("MainWindow", "Remove"))
        self.notificationbox.setTitle(_translate("MainWindow", "Send notification"))
        self.removepackagebtn_2.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.networmanagementtab), _translate("MainWindow", "Network Management"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
