import React from "react";
import { FaCheckCircle, FaTimeCircle } from "react-icon/fa";

const ResultScreen = ({ isCorrect, explanation, onRetry }) => {
  return (
    <div className="container">
      <div className="card">
        <div className="card-body text-center">
          {isCorrect ? (
            <div>
              <FaCheckCircle size="60" color="green" />
              <h4>正解です!</h4>
            </div>
          ) : (
              <div>
                <FaTimeCircle size="60" color="red" />
                <h4>不正解です...</h4>
              </div>
          )}
          <p>{ explanation }</p>
        </div>
      </div>
    </div>
  )
}
