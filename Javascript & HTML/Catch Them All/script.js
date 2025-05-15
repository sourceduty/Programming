const screens = document.querySelectorAll('.screen');
const choose_pokemon_btns = document.querySelectorAll('.choose-pokemon-btn');
const start_btn = document.getElementById('start-btn');
const game_container = document.getElementById('game-container');
const timeEl = document.getElementById('time');
const scoreEl = document.getElementById('score');
const message = document.getElementById('message');
let seconds = 0;
let score = 0;
let selected_pokemon = {};

// Debugging
console.log("JavaScript file loaded correctly.");

start_btn.addEventListener('click', () => {
    console.log("Start button clicked.");
    screens[0].classList.add('up');
    console.log("First screen should now be visible.");
});

choose_pokemon_btns.forEach(btn => {
    btn.addEventListener('click', () => {
        const img = btn.querySelector('img');
        const src = img.getAttribute('src');
        const alt = img.getAttribute('alt');
        selected_pokemon = { src, alt };
        console.log("Selected Pokémon:", selected_pokemon);
        screens[1].classList.add('up');
        console.log("Second screen should now be visible.");
        setTimeout(createPokemon, 1000);
        startGame();
    });
});

function startGame() {
    console.log("Game started.");
    setInterval(increaseTime, 1000);
}

function increaseTime() {
    let m = Math.floor(seconds / 60);
    let s = seconds % 60;
    m = m < 10 ? `0${m}` : m;
    s = s < 10 ? `0${s}` : s;
    timeEl.innerHTML = `Time: ${m}:${s}`;
    seconds++;
    console.log("Time updated:", timeEl.innerHTML);
}

function createPokemon() {
    console.log("Creating Pokémon.");
    const pokemon = document.createElement('div');
    pokemon.classList.add('pokemon');
    const { x, y } = getRandomLocation();
    pokemon.style.top = `${y}px`;
    pokemon.style.left = `${x}px`;
    pokemon.innerHTML = `<img src="${selected_pokemon.src}" alt="${selected_pokemon.alt}" style="transform: rotate(${Math.random() * 360}deg)" />`;

    pokemon.addEventListener('click', catchPokemon);

    game_container.appendChild(pokemon);
    console.log("Pokémon added to the game container.");
}

function getRandomLocation() {
    const width = window.innerWidth;
    const height = window.innerHeight;
    const x = Math.random() * (width - 200) + 100;
    const y = Math.random() * (height - 200) + 100;
    return { x, y };
}

function catchPokemon() {
    console.log("Pokémon caught.");
    increaseScore();
    this.classList.add('caught');
    setTimeout(() => this.remove(), 2000);
    addPokemons();
}

function addPokemons() {
    setTimeout(createPokemon, 1000);
    setTimeout(createPokemon, 1500);
}

function increaseScore() {
    score++;
    if (score > 19) {
        message.classList.add('visible');
    }
    scoreEl.innerHTML = `Score: ${score}`;
    console.log("Score updated:", scoreEl.innerHTML);
}
