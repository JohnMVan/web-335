// Title:  vanhessche_projections.js
// Author:  John Vanhessche 
// Date: 17 November 2022 
// Description:  vanhessche_projection.js file for assignment 5.2 


//inserting/adding a new user
db.users.insertOne({
    "firstName": "Angus", 
    "lastName": "Young", 
    "employeeId": "1013", 
    "email": "ayoung@acdc.com",
    "dateCreated": new Date()});

//updating email address for mozart user.
db.users.updateOne({"_id": ObjectId("6371034f4930172f82416117")}, {"$set": {"email": "mozart@me.com"}});

//viewing mozart user.
db.users.find({"_id": ObjectId("6371034f4930172f82416117")});

//listing all documents, showing only firstName, lastName, email, and sorting by lastName ascending.
db.users.aggregate([
            {
                $project: {
                    "_id": 0, 
                    "firstName": 1, 
                    "lastName": 1, 
                    "email": 1           
                }
            },
            {
                $sort: {
                    "lastName": 1
                }
            }             
        ]
    )