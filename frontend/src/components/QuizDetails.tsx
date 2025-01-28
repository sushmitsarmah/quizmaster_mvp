import React, { useState } from 'react';
import { Quiz, Question } from '../types';
import { ArrowLeft, CheckCircle } from 'lucide-react';

interface QuizDetailsProps {
  quiz: Quiz;
  onBack: () => void;
}

interface SingleAnswerProps {
  question: Question;
  value: string;
  onChange: (value: string) => void;
}

interface MultiAnswerProps {
  question: Question;
  selectedAnswers: number[];
  onSelect: (index: number) => void;
}

interface SelectWordProps {
  question: Question;
  selectedWords: string[];
  onSelect: (word: string) => void;
}

function SingleAnswerQuestion({ question, value, onChange }: SingleAnswerProps) {
  return (
    <div className="space-y-3">
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Type your answer here..."
        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
      />
    </div>
  );
}

function MultiAnswerQuestion({ question, selectedAnswers, onSelect }: MultiAnswerProps) {
  return (
    <div className="space-y-3">
      {question.options?.map((option, optionIndex) => (
        <div
          key={optionIndex}
          onClick={() => onSelect(optionIndex)}
          className={`p-3 rounded-lg cursor-pointer transition-colors ${
            selectedAnswers.includes(optionIndex)
              ? 'bg-blue-100 border-2 border-blue-500'
              : 'bg-gray-50 hover:bg-gray-100'
          }`}
        >
          {option}
        </div>
      ))}
    </div>
  );
}

function SelectWordQuestion({ question, selectedWords, onSelect }: SelectWordProps) {
  if (question.answer.type !== 'select-word') return null;

  return (
    <div className="space-y-4">
      <p className="text-gray-600 mb-2">Fill in the blanks by selecting the correct words:</p>
      <p className="text-lg mb-4">{question.answer.sentence}</p>
      <div className="flex flex-wrap gap-2">
        {question.answer.options.map((word, index) => (
          <span
            key={index}
            onClick={() => onSelect(word)}
            className={`px-3 py-2 rounded-full cursor-pointer transition-colors ${
              selectedWords.includes(word)
                ? 'bg-blue-100 border-2 border-blue-500'
                : 'bg-gray-100 hover:bg-gray-200'
            }`}
          >
            {word}
          </span>
        ))}
      </div>
    </div>
  );
}

export function QuizDetails({ quiz, onBack }: QuizDetailsProps) {
  const [selectedAnswers, setSelectedAnswers] = useState<(string | number[] | string[])[]>(
    quiz.questions.map(q => {
      switch (q.type) {
        case 'single':
          return '';
        case 'multi':
          return [];
        case 'select-word':
          return [];
      }
    })
  );

  const handleSingleInput = (questionIndex: number, value: string) => {
    const newAnswers = [...selectedAnswers];
    newAnswers[questionIndex] = value;
    setSelectedAnswers(newAnswers);
  };

  const handleMultiSelect = (questionIndex: number, optionIndex: number) => {
    const newAnswers = [...selectedAnswers];
    const currentAnswers = newAnswers[questionIndex] as number[];
    
    if (currentAnswers.includes(optionIndex)) {
      newAnswers[questionIndex] = currentAnswers.filter(i => i !== optionIndex);
    } else {
      newAnswers[questionIndex] = [...currentAnswers, optionIndex];
    }
    
    setSelectedAnswers(newAnswers);
  };

  const handleWordSelect = (questionIndex: number, word: string) => {
    const newAnswers = [...selectedAnswers];
    const currentWords = newAnswers[questionIndex] as string[];
    
    if (currentWords.includes(word)) {
      newAnswers[questionIndex] = currentWords.filter(w => w !== word);
    } else {
      newAnswers[questionIndex] = [...currentWords, word];
    }
    
    setSelectedAnswers(newAnswers);
  };

  const handleSubmit = () => {
    // Here you would implement the logic to check answers
    console.log('Submitted answers:', selectedAnswers);
  };

  return (
    <div className="max-w-3xl mx-auto p-6">
      <button
        onClick={onBack}
        className="flex items-center text-blue-600 mb-6 hover:text-blue-800"
      >
        <ArrowLeft className="w-5 h-5 mr-2" />
        Back to Quizzes
      </button>

      <h2 className="text-3xl font-bold mb-6">{quiz.title}</h2>

      <div className="space-y-8">
        {quiz.questions.map((question, questionIndex) => (
          <div key={question.id} className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-xl font-semibold mb-4">
              {questionIndex + 1}. {question.text}
            </h3>
            
            {question.type === 'single' && (
              <SingleAnswerQuestion
                question={question}
                value={selectedAnswers[questionIndex] as string}
                onChange={(value) => handleSingleInput(questionIndex, value)}
              />
            )}
            
            {question.type === 'multi' && (
              <MultiAnswerQuestion
                question={question}
                selectedAnswers={selectedAnswers[questionIndex] as number[]}
                onSelect={(index) => handleMultiSelect(questionIndex, index)}
              />
            )}
            
            {question.type === 'select-word' && (
              <SelectWordQuestion
                question={question}
                selectedWords={selectedAnswers[questionIndex] as string[]}
                onSelect={(word) => handleWordSelect(questionIndex, word)}
              />
            )}
          </div>
        ))}
      </div>

      <button
        onClick={handleSubmit}
        className="mt-8 w-full bg-blue-600 text-white py-3 px-6 rounded-lg hover:bg-blue-700 flex items-center justify-center gap-2"
      >
        <CheckCircle className="w-5 h-5" />
        Submit Answers
      </button>
    </div>
  );
}