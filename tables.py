from flask_table import Table, Col
 
class User_Table(Table):
    username = Col('username')
    password = Col('password')
    phone = Col('phone')