// function firstAction() {
//   console.log("I am first 1 ");
//   setTimeout(secondAction, 1500);
// }

// function secondAction() {
//   console.log("I am second 2");
// }

// setTimeout(() => firstAction(secondAction), 1500);

// 進階 第二種 要記得在argument 加 callback

// function firstAction(callback, message) {
//   console.log(message);
//   setTimeout(callback, 1500);
// }

// function secondAction(message) {
//   console.log(message);
// }

// setTimeout(
//   () => firstAction(() => secondAction("I am second 222"), "I am first 111"),
//   1500
// );

// ----------------------------------------------
// call back button
// 底下兩個function是一樣的
button = document.querySelector("button");
const alertMe = () => {
  console.log("You clicked me!");
};

// function alertMe() {
//   console.log("You clicked me!");
// }
// -------------------------------------------

button.addEventListener("click", function alertMe22() {
  console.log("you click!");
});

button.addEventListener("click", function () {
  console.log("you click2222!");
});

button.addEventListener("click", () => {
  console.log("clicked!");
}); //匿名function

button.addEventListener("click", alertMe);
