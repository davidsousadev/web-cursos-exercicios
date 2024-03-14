import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.jsx';
import './index.css';
import './Api.jsx';
import Api from './Api.jsx';

const nome = "David.";

  ReactDOM.render(
    <React.StrictMode>
       <App name={nome} />  {/*name is props */}
       <Api />
    </React.StrictMode>,
    document.getElementById('root')
  );

