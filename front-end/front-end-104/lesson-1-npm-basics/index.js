const _ = require('lodash');

const numbers = [1, 2, 3, 4, 5, 6];
const shuffled = _.shuffle(numbers);

console.log('Оригинальный массив:', numbers);
console.log('Перемешанный массив:', shuffled);