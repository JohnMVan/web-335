# // Title:  vanhessche_usersp2.py
# // Author:  John Vanhessche 
# // Date: 30 November 2022 
# // Description:  vanhessche_usersp2.py file for exercise 7.3


#importing MongoClient
from pymongo import MongoClient;
import datetime;

#Connecting to MongoDB
url = "mongodb+srv://web335_user:s3cret@bellevueuniversity.ouotidt.mongodb.net/web335DBretryWrites=true&w=majority"
client = MongoClient(url);

#access variable for web335DB
db = client['web335DB'];

#creating a new person
klinger = {
    'firstName': 'Max',
    'lastName': 'Klinger',
    'employeeId': '2001',
    'email': 'mklinger@mash4077.com',
    'dateCreated': datetime.datetime.utcnow()
}

#create new person document
klinger_user_id = db.users.insert_one(klinger).inserted_id;
print(klinger_user_id);

#displaying newly crated document
print(db.users.find_one({'employeeId': '2001'}));

#update the users email address
db.users.update_one(
    {'employeeId': '2001'},
    {
        "$set": {'email': 'maxklinger@mash4077.com'}
    }
)

#displaying the updated document
print(db.users.find_one({'employeeId': '2001'}));

#deleting the document that was added
result = db.users.delete_one({'employeeId': '2001'})

#displaying results of delete query
print(result)
