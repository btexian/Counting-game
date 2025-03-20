document.addEventListener("DOMContentLoaded", () => {
    function loadGame() {
        fetch("/get_game_data")
            .then(response => response.json())
            .then(data => {
                const gameContainer = document.getElementById("game-container");
                const optionsContainer = document.getElementById("options-container");
                const categoryHeader = document.getElementById("category");
                
                gameContainer.innerHTML = "";
                optionsContainer.innerHTML = "";
                categoryHeader.innerText = `Category: ${data.category}`;
                
                data.boxes.forEach((count, index) => {
                    const box = document.createElement("div");
                    box.classList.add("box");
                    if (index === data.red_index) {
                        box.classList.add("red-box");
                    }
                    box.innerText = data.object.repeat(count);
                    gameContainer.appendChild(box);
                });
                
                data.options.forEach(option => {
                    const button = document.createElement("button");
                    button.innerText = option;
                    button.onclick = () => {
                        if (option === data.boxes[data.red_index]) {
                            alert(`Correct! This is ${data.category}.`);
                        } else {
                            alert("Try Again!");
                        }
                        loadGame(); // Reload new game without refreshing the page
                    };
                    optionsContainer.appendChild(button);
                });
            });
    }
    
    loadGame(); // Initial game load
});