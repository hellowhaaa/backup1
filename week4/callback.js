// function firstAction() {
//   console.log("I am first 1 ");
//   setTimeout(secondAction, 1500);
// }

// function secondAction() {
//   console.log("I am second 2");
// }

// setTimeout(() => firstAction(secondAction), 1500);

// 進階 第二種 要記得在argument 加 callback

function firstAction(callback, message) {
  console.log(message);
  setTimeout(callback, 1500);
}

function secondAction(message) {
  console.log(message);
}

setTimeout(
  () => firstAction(() => secondAction("I am second 222"), "I am first 111"),
  1500
);

// call back button
button = document.querySelector("button");
const alertMe = () => {
  console.log("You clicked me!");
};

function alertMe() {
  console.log("You clicked me!");
}

button.addEventListener("click", alertMe);
