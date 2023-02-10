fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => document.getElementsByClassName('title')[0].textContent = json.title)