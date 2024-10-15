document.getElementById("makeMoveButton").addEventListener("click", () => {
    // For simplicity, a move could be simulated here
    fetch("/make_move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ move: "e2e4" }),  // Example move
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            alert("Move successful!");
        } else {
            alert("Error: " + data.message);
        }
    })
    .catch(error => console.error("Error:", error));
});
