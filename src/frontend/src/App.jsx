import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
const endpoint = 'http://localhost:8000/draw_box/'

function App() {
  const [bgImage, setBgImage] = useState(null);
  const [init, setInit] = useState(false) ;

    const handle_file_submission = (e) => {
      const file = e.target.files[0];
      fetch(endpoint, {
        method:'POST',
        body:file,
      }).then(
        response => response.json()
      ).then(
        data => `url("data:image/jpeg;base64,${data.image}")`

      ).then(
        im => setBgImage(im)
      ).then(
        () => setInit(true)
      )
      
    } 
    const labelStyle = {
      top: '90%',
      left:'80%',
      width: '10%',
      height: '5%',
      backgroundColor: 'rgba(200,200,200,200)',
      fontSize:'8px',
      borderColor: 'rgba(0, 0, 0, 0)',
      
    }
    // const containter = 
  return (
    <>
      {init ? <div id="image-container" style={{backgroundImage:bgImage}}>
        {/* # remove default content */}

        <label id="upload-label" style={labelStyle}>
        upload another
        <input type="file" accept="image/*" id="file-input" onChange={handle_file_submission} />

        </label>
      </div> : <div id="image-container" >
        {/* # remove default content */}

        <label id="upload-label" >
          UPLOAD IMAGE HERE
        <input type="file" accept="image/*" id="file-input" onChange={handle_file_submission} />

        </label>
      </div>}
    </>
  )
}

export default App
