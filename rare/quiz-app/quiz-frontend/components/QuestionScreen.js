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
          <ul className="list-group">
            {questionData.choices.map((choice, index) => (
              <li
                key={index}
                className={`list-group-item ${
                  selectedChoice === choice.value? "active" : ""
                }`}
                onClick={() => handleSelectCHoice(choice)}
              >
                {choice.text}
              </li>
            )) }
          </ul>
          <div className="text-center">
            <button
              type="button"
              className="btn btn-primary"
              onClick={handleSubmit}
              disabled={!selectedChoice}
            >
              回答する
            </button>
          </div>
        </div>
      </div>
    </div>
  )
};
