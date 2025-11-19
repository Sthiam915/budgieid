import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
const endpoint = 'http://localhost:8000/receive_image/'

function App() {
  
    const handle_file_submission = (e) => {
      const file = e.target.files[0];
      fetch(endpoint, {
        method:'POST',
        body:file,
      })
    } 
  return (
    <>
      <div id="image-container">
        {/* # remove default content */}

        <label id="upload-label">
        UPLOAD IMAGE HERE
        <input type="file" accept="image/*" id="file-input" onChange={handle_file_submission} />

        </label>
      </div>
    </>
  )
}

export default App
