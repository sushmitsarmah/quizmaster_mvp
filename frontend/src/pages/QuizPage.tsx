/* eslint-disable @typescript-eslint/no-explicit-any */
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getQuiz } from '../services/index';
import { Quiz } from '../types';
import { QuizDetails } from '../components/QuizDetails';

const QuizPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [quiz, setQuiz] = useState<Quiz | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    const fetchQuiz = async () => {
      if (!id) return;
      try {
        const response = await getQuiz(+id);
        setQuiz(response.data);
      } catch (err: any) {
        console.log(err);
        setError('Failed to load quiz');
      } finally {
        setLoading(false);
      }
    };

    fetchQuiz();
  }, [id]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div className="text-red-500">{error}</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      {quiz ? (
        <QuizDetails quiz={quiz} onBack={() => window.history.back()} />
      ) : (
        <div className="text-center text-xl text-gray-600">Quiz not found</div>
      )}
    </div>
  );
};

export default QuizPage;
