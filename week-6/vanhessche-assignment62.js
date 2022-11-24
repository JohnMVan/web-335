// Title:  vanhessche_assignment62.js
// Author:  John Vanhessche 
// Date: 22 November 2022 
// Description:  vanhessche_assignment62.js file for assignment 6.2 


//Show a list of houses
db.houses.find();

//Show a list of students
db.students.find();

//adding a document to the student collection
db.students.insertOne({
    "firstName": "Barney",
	"lastName": "Miller",
	"studentId": "s1050",
	"houseId": "h1007"
})

//verifying that the student added in previous insert was found.
db.students.find({"_id":ObjectId("637d317876abc3ddee18a725")})

//Delete user by _id
db.students.deleteOne({"_id":ObjectId("637d317876abc3ddee18a725")})

//using lookup operator to look up students by houseid.  
db.houses.aggregate([{$lookup:{from: "students", localField: "houseId", foreignField: "houseId", as: "students_in_house"}}])

//getting a list of students in the Gryffindor house
db.houses.aggregate([{$match:{houseId: "h1007"}},{$lookup:{from: "students", localField: "houseId", foreignField: "houseId", as: "students_in_house"}}])

//list of students with Eagle as mascot.
db.houses.aggregate([{$match:{mascot: "Eagle"}},{$lookup:{from: "students", localField: "houseId", foreignField: "houseId", as: "students_in_house"}}])













