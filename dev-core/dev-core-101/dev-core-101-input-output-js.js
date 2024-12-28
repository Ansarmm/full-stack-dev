const cy = 2024
const century = 100

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Введите ваше имя: ', name => {
    readline.question("Введите ваш возраст: ", age => {
        const hundred = 100 - {age} + 2024
        console.log(`Привет, ${name}. Тебе будет 100 лет в ${century - age + cy} году.`);
        readline.close();
    });
});