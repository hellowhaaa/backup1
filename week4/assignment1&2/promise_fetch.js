let api = "https://restcountries.com/v3.1/all";
// let promise = fetch(api);
// console.log(promise); 得到的會是promise

// Version1  ------------------------------
// function setup() {
//   fetch(api).then(gotData).catch(gotErr);

//   function gotData(data) {
//     console.log(data);
//   }
//   function gotErr(err) {
//     console.log(err);
//   }
// }
// Version 2  --------------------------------
// function setup() {
//   fetch(api)
//     .then((data) => {
//       console.log(data);
//     })
//     .catch((err) => {
//       console.log(err);
//     });
// }

// Version 3  --------------------------------

fetch(api)
  .then((response) => {
    return response.json();
  })
  .then((json) => {
    console.log(json[0].name);
  })
  .catch((err) => {
    console.log(err);
  });

  