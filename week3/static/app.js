document.getElementById("get-btn").addEventListener("click", makeRequest);
function makeRequest() {
  let number = document.getElementById("text").value;
  let xhr = new XMLHttpRequest();
  xhr.open("GET", "http://127.0.0.1:9000/data?number=" + number, true);
  // open method initialize the request
  // 1.what kind of the request
  // 2. path of the data
  // 3. if it's asynchronous

  // xhr.onload -> handle the response

  xhr.onload = function () {
    if (xhr.status == 200) {
      console.log("success");
    }
  };
  xhr.send();
}
