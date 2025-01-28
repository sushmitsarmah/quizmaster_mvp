import React from 'react';
import { Quiz } from '../types';

interface QuizCardProps {
  quiz: Quiz;
  onClick: () => void;
}

export function QuizCard({ quiz, onClick }: QuizCardProps) {
  return (
    <div 
      onClick={onClick}
      className="bg-white rounded-lg shadow-lg overflow-hidden cursor-pointer transform transition-transform hover:scale-105"
    >
      <img 
        src={quiz.image} 
        alt={quiz.title}
        className="w-full h-48 object-cover"
      />
      <div className="p-4">
        <h3 className="text-xl font-bold mb-2">{quiz.title}</h3>
        <p className="text-gray-600">{quiz.description}</p>
      </div>
    </div>
  );
}