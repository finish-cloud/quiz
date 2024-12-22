import React, { useState } from "react";
import { container } from "webpack";

const QuestionScreen = ({ questionDate, onAnswerSubmit }) => {
  const [selectedChoice, setSelectedChoice] = useState(null);

  const handleChoiceSelect = (choice) => {
    setSelectedChoice(choice);
  };

  const handleSubmit = () => {
    onAnswerSubmit(selectedChoice);
  };
  return (
    <div className="container">
      <div className="card-shadow">
        <div className="card-body">
          <h4 className="card-title text-center">{questionData.text}</h4>
        </div>
      </div>
    </div>
  )
};
