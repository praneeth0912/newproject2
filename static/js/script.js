// =========================
// DOM Elements
// =========================
const display = document.getElementById("display");
const buttons = document.querySelectorAll(".buttons button");

// =========================
// Click Event Listeners
// =========================
buttons.forEach((button) => {
    button.addEventListener("click", () => {
        handleInput(button.value);
    });
});

// =========================
// Keyboard Event Listener
// =========================
document.addEventListener("keydown", (event) => {
    const key = event.key;

    // Numbers & Operators
    if ((key >= "0" && key <= "9") || ["+", "-", "*", "/", "."].includes(key)) {
        event.preventDefault();
        handleInput(key);
    }
    // Backspace
    else if (key === "Backspace") {
        event.preventDefault();
        display.value = display.value.slice(0, -1);
    }
    // Enter / Equals
    else if (key === "Enter" || key === "=") {
        event.preventDefault();
        handleInput("=");
    }
    // Escape / Clear
    else if (key === "Escape" || key === "c" || key === "C") {
        event.preventDefault();
        handleInput("C");
    }
});

// =========================
// Handle Input Logic
// =========================
function handleInput(value) {
    // Clear display
    if (value === "C") {
        display.value = "";
        return;
    }

    // Trigger Calculation
    if (["=", "√", "x²", "%"].includes(value)) {
        if (display.value.trim() !== "") {
            calculate(value);
        }
        return;
    }

    // Append value to display
    display.value += value;
}

// =========================
// Flask Request API
// =========================
async function calculate(operation) {
    try {
        const response = await fetch("/calculate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                expression: display.value,
                operation: operation
            })
        });

        const data = await response.json();

        if (response.ok) {
            display.value = data.result;
        } else {
            alert(data.error || "Error performing operation");
        }

    } catch (error) {
        alert("Unable to connect to Flask server.");
    }
}