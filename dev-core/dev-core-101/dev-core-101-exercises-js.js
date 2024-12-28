//Из Цельсия в Фаренгейты
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

 rl.question('Введите температуру в Цельсиях: ', temp => { 
         temp2 = temp * 1.6 + 32
         console.log(`Температура из Цельсия в Фаренгейты будет равна ${temp2}`);
         rl.close();
     });

// Четное или нечетное число

 rl.question('Введите число для проверки: ', number => {
     if (number % 2 == 0)
         console.log('Число является четным');
     else
        console.log('Число нечетное');
     rl.close();
 });

//Игра "Угадай Число"

const randomNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

console.log("Welcome to 'Guess the Number'!");
console.log("I'm thinking of a number between 1 and 100. Keep guessing until you get it right!");

function askGuess() {
    rl.question("Enter your guess: ", (input) => {
        const userGuess = parseInt(input);
        attempts++;

        if (userGuess === randomNumber) {
            console.log(`Congratulations! You guessed the number ${randomNumber} correctly in ${attempts} attempts!`);
            rl.close(); 
        } else if (userGuess < randomNumber) {
            console.log("Too low! Try again.");
            askGuess();  
        } else if (userGuess > randomNumber) {
            console.log("Too high! Try again.");
            askGuess();
        } else {
            console.log("Please enter a valid number.");
            askGuess();  
        }
    });
}

askGuess();

rl.on('close', () => {
    console.log("Thanks for playing! Goodbye!");
});
