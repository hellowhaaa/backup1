// function show() {
//   let xhr = new XMLHttpRequest();
//   xhr.open(
//     "GET",
//     "https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
//     true
//   );
//   xhr.onload = function () {
//     if (xhr.status == 200) {
//       console.log("success");
//       let products = JSON.parse(this.response);
//       products.forEach((product) => {
//         const productName = document.createElement("div");
//         const productPrice = document.createElement("div");
//         const productDescription = document.createElement("div");
//         productName.innerHTML = product.name;
//         productPrice.innerHTML = product.price;
//         productDescription.innerHTML = product.description;
//         document.getElementById("all-product").appendChild(productName);
//         document.getElementById("all-product").appendChild(productPrice);
//         document.getElementById("all-product").appendChild(productDescription);
//       });
//     } else {
//       alert("There was a problem with the request.");
//     }
//   };
//   xhr.send();
// }

// 第一版
function ajax(src, callback) {
  let xhr = new XMLHttpRequest();
  xhr.open("GET", src, true);

  // xhr.onload = callback();
  xhr.onload = function () {
    if (xhr.status == 200) {
      console.log("success");
      data = xhr.response;
      callback(data);
    } else {
      alert("There was a problem with the request.");
    }
  };
  xhr.send();
}
function render(data) {
  let products = JSON.parse(data);
  products.forEach((product) => {
    const productName = document.createElement("div");
    const productPrice = document.createElement("div");
    const productDescription = document.createElement("div");
    productName.innerHTML = product.name;
    productPrice.innerHTML = product.price;
    productDescription.innerHTML = product.description;
    document.getElementById("all-product").appendChild(productName);
    document.getElementById("all-product").appendChild(productPrice);
    document.getElementById("all-product").appendChild(productDescription);
  });
}

ajax(
  "https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
  function (response) {
    render(response);
  }
);

// 第二版
// function ajax(src, callback) {
//   console.log("success");
//   let products = JSON.parse(data.response);
//   products.forEach((product) => {
//     const productName = document.createElement("div");
//     const productPrice = document.createElement("div");
//     const productDescription = document.createElement("div");
//     productName.innerHTML = product.name;
//     productPrice.innerHTML = product.price;
//     productDescription.innerHTML = product.description;
//     document.getElementById("all-product").appendChild(productName);
//     document.getElementById("all-product").appendChild(productPrice);
//     document.getElementById("all-product").appendChild(productDescription);
//   });
// }

// function render(data) {
//   let xhr = new XMLHttpRequest();
//   xhr.open("GET", src, true);
//   if (xhr.status == 200) {
//     xhr.onload = callback();
//   } else {
//     alert("There was a problem with the request.");
//   }
//   xhr.send();
// }

// ajax(
//   "https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
//   function (response) {
//     render(response);
//   }
// );
