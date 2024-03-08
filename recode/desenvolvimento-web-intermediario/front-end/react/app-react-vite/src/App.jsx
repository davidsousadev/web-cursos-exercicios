import React from 'react';
import './App.css'

function tick() {
return(
    <> 
        <div>
          <h1>{new Date().toLocaleTimeString()}</h1>
        </div>
      
    </>
  )
}

function App() {
    return tick()
  }

export default App
