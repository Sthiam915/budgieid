import { useState } from 'react'
import './App.css'

const endpoint = 'http://localhost:8000/draw_box/'

function App() {
  const [bgImage, setBgImage] = useState(null)
  const [init, setInit] = useState(false)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handle_file_submission = async (e) => {
    const file = e.target.files[0]
    if (!file) return

    setLoading(true)
    setError('')
    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        body: file,
      })

      if (!response.ok) {
        throw new Error('Server error: ' + response.status)
      }

      const data = await response.json()
      const im = `url("data:image/jpeg;base64,${data.image}")`
      setBgImage(im)
      setInit(true)
    } catch (err) {
      console.error(err)
      setError('Something went wrong talking to the server.')
    } finally {
      setLoading(false)
    }
  }

  const labelStyle = {
    top: '90%',
    left: '80%',
    width: '10%',
    height: '5%',
    backgroundColor: 'rgba(200,200,200,200)',
    fontSize: '8px',
    borderColor: 'rgba(0, 0, 0, 0)',
  }

  return (
    <div
      style={{
        minHeight: '100vh',
        backgroundColor: '#f0f0f0',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '20px',
        boxSizing: 'border-box',
      }}
    >
      <h1 style={{ marginBottom: '20px' }}>BudgieID</h1>

      {/* SECTION 1: existing draw_box feature */}
      <div style={{ width: '100%', maxWidth: '900px', marginBottom: '40px' }}>
        <h2>1. Detect budgie & draw bounding box</h2>

        {init ? (
          <div id="image-container" style={{ backgroundImage: bgImage }}>
            <label id="upload-label" style={labelStyle}>
              upload another
              <input
                type="file"
                accept="image/*"
                id="file-input"
                onChange={handle_file_submission}
              />
            </label>
          </div>
        ) : (
          <div id="image-container">
            <label id="upload-label">
              UPLOAD IMAGE HERE
              <input
                type="file"
                accept="image/*"
                id="file-input"
                onChange={handle_file_submission}
              />
            </label>
          </div>
        )}

        {loading && <p>Processing image…</p>}
        {error && <p style={{ color: 'red' }}>{error}</p>}
      </div>

      {/* SECTION 2: Breeding simulator UI */}
      <div style={{ width: '100%', maxWidth: '900px' }}>
        <h2>2. Breeding simulator (mock UI)</h2>
        <BreedingSimulator />
      </div>
    </div>
  )
}

/* --- NEW COMPONENT: two parents + offspring table --- */

const COLOR_OPTIONS = ['green', 'blue', 'yellow', 'white']
const SEX_OPTIONS = ['m', 'f']

function BreedingSimulator() {
  const [parent1, setParent1] = useState({ sex: 'm', color: 'green' })
  const [parent2, setParent2] = useState({ sex: 'f', color: 'blue' })
  const [prediction, setPrediction] = useState(null)

  const handleChangeParent1 = (field, value) => {
    setParent1((prev) => ({ ...prev, [field]: value }))
  }

  const handleChangeParent2 = (field, value) => {
    setParent2((prev) => ({ ...prev, [field]: value }))
  }

  const handlePredict = () => {
    // 🔹 MOCK LOGIC: just builds a fake offspring list based on the selections.
    // Later this will be replaced with a real fetch() to the backend.
    const results = [
      {
        description: `Mix of ${parent1.color} (P1) and ${parent2.color} (P2)`,
        probability: 0.5,
      },
      {
        description: `Reverse mix of ${parent2.color} (P2) and ${parent1.color} (P1)`,
        probability: 0.5,
      },
    ]
    setPrediction(results)
  }

  return (
    <div
      style={{
        backgroundColor: '#e4e4e4',
        borderRadius: '8px',
        padding: '20px',
      }}
    >
      <div
        style={{
          display: 'flex',
          gap: '20px',
          marginBottom: '20px',
          flexWrap: 'wrap',
        }}
      >
        {/* Parent 1 */}
        <div
          style={{
            flex: 1,
            minWidth: '220px',
            backgroundColor: '#ffffff',
            borderRadius: '8px',
            padding: '12px',
          }}
        >
          <h3>Parent 1</h3>
          <div style={{ marginBottom: '8px' }}>
            <label>
              Sex:&nbsp;
              <select
                value={parent1.sex}
                onChange={(e) => handleChangeParent1('sex', e.target.value)}
              >
                {SEX_OPTIONS.map((s) => (
                  <option key={s} value={s}>
                    {s}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <div>
            <label>
              Color:&nbsp;
              <select
                value={parent1.color}
                onChange={(e) => handleChangeParent1('color', e.target.value)}
              >
                {COLOR_OPTIONS.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </label>
          </div>
        </div>

        {/* Parent 2 */}
        <div
          style={{
            flex: 1,
            minWidth: '220px',
            backgroundColor: '#ffffff',
            borderRadius: '8px',
            padding: '12px',
          }}
        >
          <h3>Parent 2</h3>
          <div style={{ marginBottom: '8px' }}>
            <label>
              Sex:&nbsp;
              <select
                value={parent2.sex}
                onChange={(e) => handleChangeParent2('sex', e.target.value)}
              >
                {SEX_OPTIONS.map((s) => (
                  <option key={s} value={s}>
                    {s}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <div>
            <label>
              Color:&nbsp;
              <select
                value={parent2.color}
                onChange={(e) => handleChangeParent2('color', e.target.value)}
              >
                {COLOR_OPTIONS.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </label>
          </div>
        </div>
      </div>

      <button onClick={handlePredict}>Predict Offspring (mock)</button>

      {prediction && (
        <div style={{ marginTop: '20px' }}>
          <h3>Possible offspring (demo data)</h3>
          <table
            style={{
              width: '100%',
              borderCollapse: 'collapse',
              backgroundColor: '#fff',
            }}
          >
            <thead>
              <tr>
                <th
                  style={{
                    borderBottom: '1px solid #ccc',
                    textAlign: 'left',
                    padding: '8px',
                  }}
                >
                  Description
                </th>
                <th
                  style={{
                    borderBottom: '1px solid #ccc',
                    textAlign: 'right',
                    padding: '8px',
                  }}
                >
                  Probability
                </th>
              </tr>
            </thead>
            <tbody>
              {prediction.map((row, idx) => (
                <tr key={idx}>
                  <td style={{ padding: '8px', borderBottom: '1px solid #eee' }}>
                    {row.description}
                  </td>
                  <td
                    style={{
                      padding: '8px',
                      borderBottom: '1px solid #eee',
                      textAlign: 'right',
                    }}
                  >
                    {(row.probability * 100).toFixed(1)}%
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}

export default App
