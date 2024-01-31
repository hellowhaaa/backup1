function show() {
  // data 是 得到讀 json file (all string)
  // document.createElement() and appendChild() methods are preferred.

  let xhr = new XMLHttpRequest();
  xhr.open(
    "GET",
    "https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
    true
  );
  xhr.onload = function () {
    if (xhr.status == 200) {
      console.log("success");
      let products = JSON.parse(this.response);
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
    } else {
      alert("There was a problem with the request.");
    }
  };
  xhr.send();
}
