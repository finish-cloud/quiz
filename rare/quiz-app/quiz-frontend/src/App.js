import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function QuizApp() {
  const [questions, setQuestions] = useState([])
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/questions/")
      .then(response => setQuestions(response.data))
      .catch(error => console.error('Error:', error))
  }, [])
    return (
        <div className="App">
            <h1>Quiz App</h1>
            {questions.map(question => (
                <div key={question.id}>
                    <h2>{question.text}</h2>
                    <ul>
                        {question.choices.map(choice => (
                            <li key={choice.id}>{choice.text}</li>
                        ))}
                    </ul>
                    {question.explanation && <p>{question.explanation.text}</p>}
                </div>
            ))}
        </div>
    );
}
export default QuizApp;
