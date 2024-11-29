import React, { useState, useEffect } from "react";
import './App.css';

function App() {
  const [questions, setQuestions] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [showScore, setShowScore] = useState(false);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/quiz").then((response) => {
      setQuestions(response.data);
    });
  }, []);
  const handleAnswer = (isCorrect) => {
    if (isCorrect) {
      setScore(scor