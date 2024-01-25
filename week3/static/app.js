
console.log('It\'s from JS!')
    // fetch("https://swapi.dev/api/people/1/")
    //     .then((res) => {
    //         console.log('Resolved', res);
    //         return res.json()
    //     })
    //     .then((data) => {
    //         console.log(data);
    //     })
    //     .cath((e) => {
    //         console.log('Error!', e)
    //     })

    // const req = new XMLHttpRequest();

    // req.onload = function() {
    //     console.log('It loaded');
    //     console.log(this);
    // };

    // req.onerror = function () {
    //     console.log("ERROR!!");
    //     console.log(this);
    // };

    // req.open("GET", "https://swapi.dev/api/people/1/");
    // req.send()

    (function () {
        var httpRequest;
        document
            .getElementById("btn")
            .addEventListener("click", makeRequest);

        function makeRequest() {
            httpRequest = new XMLHttpRequest();

            if (!httpRequest) {
                alert("Giving up :( Cannot create an XMLHTTP instance");
                return false;
            }
            httpRequest.onreadystatechange = alertContents;
            httpRequest.open("GET", "http://127.0.0.1:2000/");
            httpRequest.send();
        }

        function alertContents() {
            if (httpRequest.readyState === XMLHttpRequest.DONE) {
                if (httpRequest.status === 200) {
                    alert(httpRequest.responseText);
                } else {
                    alert("There was a problem with the request.");
                }
            }
        }
    })();


const httpRequest = new XMLHttpRequest();
function handler() {
    // Process the server response here.
}

httpRequest.onreadystatechange = handler;

httpRequest.open("GET", "http://www.example.org/some.file", true);
httpRequest.send();

httpRequest.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded",
);