const analyzeButton = document.getElementById("analyzeBtn");

const text = document.getElementById("text");

const operation = document.getElementById("operation");

const result = document.getElementById("result");


analyzeButton.addEventListener("click", async function () {

    const response = await fetch("/analyze", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            text: text.value,
            operation: operation.value

        })

    });

    const data = await response.json();

    if (response.ok) {

        result.innerHTML = data.result;

    }

    else {

        result.innerHTML = data.error;

    }

});