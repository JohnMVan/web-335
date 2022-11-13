// Title:  vanhessche_assignment43.js
// Author:  John Vanhessche 
// Date:  13 November 2022
// Description:  js queries for Mongo


//load users.js script
load("users.js");

//To find all users in a collection
db.users.find();

//To find a user by their email address
db.users.find({ email: 'jbach@me.com'});

//to find user by lastName
db.users.find({ lastName: 'Mozart'});

//To find a user by first name
db.users.find({ firstName: 'Richard'});



