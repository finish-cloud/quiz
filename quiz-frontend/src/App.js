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
      setScore(score + 1);
    }

    const nextQuestionIndex = currentQuestion + 1;
    if (nextQuestionIndex < questions.length) {
      setCurrentQuestionIndex(nextQuestionIndex);
    } else {
      setShowScore(true);
    }
  };
  return (
    <div className="app">
      {showScore ? (
        <div className="score-section">
          You scored {score} out of {questions.length}
        </div>
      ) : (
        questions.length > 0 && (
          <div className="question-section">
            <div className="question-text">
              {questions[currentQuestionIndex].text}
            </div>
            <div className="answer-section">
              {questions[currentQuestionIndex].choices.map((choice) => (
                <button
                  key={choice.id}
                  onClick={() => handleAnswerClick(choice.is_correct)}
                >
                  {choice.text}
                </button>
              ))}
            </div>
          </div>
        )
      )}
    </div>
  );
}

export default App;
