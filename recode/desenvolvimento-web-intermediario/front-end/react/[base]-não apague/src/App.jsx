import React from 'react';
import ReactDOM from 'react-dom';
import './App.css'

function tick() {
  
const content = (
    <> 
    <div>
      <h1>{new Date().toLocaleTimeString()}</h1>
    </div>     
    </>
  )
  ReactDOM.createRoot(document.getElementById('root')).render(content)
  return content
}

function App() {
    return tick()
  }
  setInterval (tick, 1000)
export default App
