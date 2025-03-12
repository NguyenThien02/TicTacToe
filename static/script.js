document.addEventListener("DOMContentLoaded", function () {
    const cells = document.querySelectorAll(".cell");
    const message = document.getElementById("message");

    cells.forEach(cell => {
        cell.addEventListener("click", function () {
            const index = this.getAttribute("data-index");

            fetch("/play", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ position: parseInt(index) }),
            })
            .then(response => response.json())
            .then(data => {
                updateBoard(data.board);
                message.textContent = data.message;

                if (data.winner) {
                    setTimeout(() => {
                        alert(data.message);
                        resetGame();
                    }, 200);
                }
            })
            .catch(error => console.error("Error:", error));
        });
    });

    function updateBoard(board) {
        board.forEach((value, index) => {
            cells[index].textContent = value === "x" || value === "o" ? value : "";
        });
    }

    function resetGame() {
        fetch("/reset", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            updateBoard(data.board);
            message.textContent = "Bắt đầu ván mới!";
        })
        .catch(error => console.error("Error:", error));
    }
});
