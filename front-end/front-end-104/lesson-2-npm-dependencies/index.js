const axios = require('axios');

axios.get('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => {
    console.log('Задача:', response.data.title);
  })
  .catch(error => {
    console.log('Ошибка:', error.message);
  });