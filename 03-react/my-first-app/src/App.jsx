import { useState } from 'react'
import ProjectList from './ProjectList'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const projects = ["Calculator", "Budget Tracker", "AI Study Buddy", "Bio Page"]

  return (
    <div>
      <h1>My First React App</h1>
      <p>Count is {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>

      <h2>My Projects</h2>
      <ProjectList projects={projects} />
    </div>
  )
}

export default App