import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const getQuiz = async (id: number) => {
  const response = await axios.get(`${API_URL}/quizzes/${id}`);
  return response.data;
};

export const login = async (username: string, password: string) => {
  const response = await axios.post(`${API_URL}/login/`, {
    username,
    password,
  });
  return response.data;
};

export const getQuizzes = async () => {
  const response = await axios.get(`${API_URL}/quizzes/`);
  return response.data;
};

export const submitAnswer = async (quizId: number, questionId: number, answer: string) => {
  const response = await axios.post(`${API_URL}/quizzes/${quizId}/submit_answer/`, {
    question_id: questionId,
    answer: answer,
  });
  return response.data;
};
