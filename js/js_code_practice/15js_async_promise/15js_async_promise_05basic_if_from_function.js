function checkAge(userAge) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (userAge > 17) {
        resolve({ id: 1, name: "Tom", age: userAge });
      } else {
        reject("Invalid age");
      }
    }, 3000);
  });
}

// It works outside and inside of function as well
checkAge(19)
  .then((user) => {console.log(user);})
  .catch((error) => {console.log("not valid age:" + error);});

checkAge(11)
  .then((user) => {console.log(user);})
  .catch((error) => {console.log("not valid age: " + error);});

// via function
// function checkingAge(age) {
//  return checkAge(age)
//    .then((user) => {
//      console.log("Checking of age is started");
//      console.log(user);
//    })
//    .catch((error) => {
//      console.log("not valid age: " + error);
//    })
//    .finally(() => {
//      console.log("Checking of age is completed");
//    });
//}
//// call function
//checkingAge(19);
//checkingAge(11);
