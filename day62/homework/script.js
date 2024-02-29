//Create an Object:
//Create an object named person with properties name, age, and city.

const person = {
    name: "barbare",
    age: 14,
    city: "Mtskheta",

    greet: function(name){
        console.log("your name is " + name)
    }
}

person.greet("barbare")

//Access Object Properties:
//Access the name property of the person object you created in the previous exercise.

console.log(person.age)

//Modify Object Properties:
//Change the age property of the person object to a new value.

person.age = 14

//Add Object Properties:
//Add a new property named country to the person object and set its value.

person.country = "Georgia"

//Object Methods:
//Add a method named greet to the person object that logs a greeting message including the person's name.


//Object Comparison:
//Create two objects with the same properties and values. Use the === operator to compare them. Log the result.

const car = {
    color: "red",
    
}

const carOne = {
    color: "red"
}


console.log(car === carOne)

//Nested Objects:
//Create an object named school with properties name and students, where students is an array of objects representing student names and ages. Access a student's name and age from the school object.

const school = {
   name: "Mtsketis N2",
   students: [
    {
        name: "nanuka",
        age: 12

    }
    ,
    {
        name: "nia",
        age: 14
    }
    ,
    {
        name: "jeko",
        age: 14
    }
   ]
}

console.log(school.students[2].name)
console.log(school.students[2].age)
