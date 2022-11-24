# // Title:  vanhessche_usersp1.py
# // Author:  John Vanhessche 
# // Date: 23 November 2022 
# // Description:  vanhessche_usersp1.py file for exercise 6.3 


#importing MongoClient
from pymongo import MongoClient;
import datetime;

#Connecting to MongoDB
url = "mongodb+srv://web335_user:s3cret@bellevueuniversity.ouotidt.mongodb.net/web335DBretryWrites=true&w=majority"
client = MongoClient(url);

#access variable for web335DB
db = client['web335DB'];

#Displaying all documents in collection
print("List of all people")
for user in db.users.find({}):
    print(user);

#Find user where employeeId = 1011
print()
print("Employee with ID of 1011")
print(db.users.find_one({"employeeId": "1011"}));

#find user matching last name: Mozart
print()
print("Person with last name of Mozart")
print(db.users.find_one({"lastName": "Mozart"}));
