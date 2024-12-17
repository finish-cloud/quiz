import React, { useState } from "react";

const QuestionScreen = ({ questionDate, onAnswerSubmit }) => {
  const [selectedChoice, setSelectedChoice] = useState(null);

  const handleChoiceSelect = (choice) => {
    setSelectedChoice(choice);
  };

  const handleSubmit = () => {
    onAnswerSubmit(selectedChoice);
  };
