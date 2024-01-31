function showCountry() {
  let xhr = new XMLHttpRequest();
  xhr.open("GET", "https://restcountries.com/v3.1/all", true);
  // initialize the request TRUE/FALSE 問你 是否為 asynchronous

  xhr.onload = function () {
    if (xhr.status == 200) {
      console.log("success");
      let countries = JSON.parse(xhr.response);
      //  JSON. parse 將 JSON File(全string) 轉成 Array
      //   let country = this.response;
      console.log(countries);
      countries.forEach((country) => {
        const countryCard = document.createElement("div");
        countryCard.innerHTML = country.name.common;
        document.getElementById("feed").appendChild(countryCard);
      });
    }
  };
  // 使用 call back function 確認 status code

  xhr.send();
  // send the request
}
