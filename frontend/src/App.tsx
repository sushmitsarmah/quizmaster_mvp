import React, { useState } from 'react';
import { QuizCard } from './components/QuizCard';
import { QuizDetails } from './components/QuizDetails';
import { Navbar } from './components/Navbar';
import { quizzes } from './data/quizzes';
import { Quiz } from './types';

function App() {
  const [selectedQuiz, setSelectedQuiz] = useState<Quiz | null>(null);

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      {selectedQuiz ? (
        <QuizDetails 
          quiz={selectedQuiz} 
          onBack={() => setSelectedQuiz(null)} 
        />
      ) : (
        <div className="container mx-auto px-4 py-8">
          <div className="text-center mb-12">
            <h1 className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-blue-800">
              Welcome to QuizMaster
            </h1>
            <p className="mt-4 text-xl text-gray-600">
              Challenge yourself with our collection of interactive quizzes
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {quizzes.map((quiz) => (
              <QuizCard
                key={quiz.id}
                quiz={quiz}
                onClick={() => setSelectedQuiz(quiz)}
              />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;