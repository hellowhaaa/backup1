delay(1000)
  .then(() => sayHello())
  .catch((err) => console.err(err));

// function delay(time) {
//     function dealWithPromise(resolve, reject){

//     }
//   return new Promise(dealWithPromise);
//   //   setTimeout(sayHello, time);
// }
// function sayHello() {
//   console.log("123");
// }

function delay(time) {
  return new Promise((resolve, reject) => {
    if (isNaN(time)) {
      reject(new Error("delay requires a valid number"));
    } else {
      setTimeout(resolve, time);
    }
  });
  //   setTimeout(sayHello, time);
}
function sayHello() {
  console.log("123");
}
