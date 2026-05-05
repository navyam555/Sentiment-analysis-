async function analyze() {
    let review = document.getElementById("review").value;

    let res = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({review})
    });

    let data = await res.json();

    document.getElementById("result").innerText =
        "Sentiment: " + data.sentiment +
        " | Issue: " + data.issue +
        " | Intent: " + data.intent;
}