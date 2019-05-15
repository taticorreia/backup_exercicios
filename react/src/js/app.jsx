
import ReactDom from 'react-dom';
import React from 'react';

let App = (
  <div>
    <h1>Olá Mundo!</h1>
  </div>
);

ReactDom.render(App, document.getById('app')); //essa informação trará a informação ola mundo para a pag html.
