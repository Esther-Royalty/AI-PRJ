<<<<<<< HEAD
import { Routes, Route } from 'react-router-dom'
import Welcome from './Welcome'
import Dashboard from './Dashboard'

function App() {
=======
import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [budget, setBudget] = useState(50000)
  const [expenses, setExpenses] = useState(() => {
    const saved = localStorage.getItem("expenses")
    return saved ? JSON.parse(saved) : [
    { amount: 5000, category: "Food", date: new Date().toISOString() },
    { amount: 2000, category: "Transport", date: new Date().toISOString() },
  ]
})
  useEffect(() => {
  localStorage.setItem("expenses", JSON.stringify(expenses))
}, [expenses])

  const [newAmount, setNewAmount] = useState("")
  const [newCategory, setNewCategory] = useState("")

  const total = expenses.reduce((sum, expense) => sum + expense.amount, 0)
  const remaining = budget - total

  const now = new Date()
  const currentMonth = now.getMonth()
  const currentYear = now.getFullYear()

  const thisMonthExpenses = expenses.filter((expense) => {
    const expenseDate = new Date(expense.date)
    return (
      expenseDate.getMonth() === currentMonth &&
      expenseDate.getFullYear() === currentYear
    )
   })

  const thisMonthTotal = thisMonthExpenses.reduce(
    (sum, expense) => sum + expense.amount,
    0
   )

  const recentExpenses = [...expenses]
   .sort((a, b) => new Date(b.date) - new Date(a.date))
   .slice(0, 5)

  function handleAddExpense() {
    if (newAmount === "" || newCategory === "") {
      alert("Please fill in both fields")
      return
    }

    const expense = {
      amount: parseFloat(newAmount),
      category: newCategory,
      date: new Date().toISOString(),
    }

    setExpenses([...expenses, expense])
    setNewAmount("")
    setNewCategory("")
  }

>>>>>>> b9fbc24975097e070708b428485e7431546ac45e
  return (
    <Routes>
      <Route path="/" element={<Welcome />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  )
}

export default App 