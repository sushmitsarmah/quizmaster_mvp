/* eslint-disable @typescript-eslint/no-explicit-any */
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL;

const fetchApi = async (url: string, method: string, data: any) => {
  const token = localStorage.getItem('token');
  const response = await axios({
    method,
    url: `${API_URL}${url}`,
    data,
    headers: {
      Authorization: `Token ${token}`,
    },
  });
  return response.data;
};

export const getQuiz = async (id: number) => {
  return fetchApi(`/quizzes/${id}/`, 'GET', null);
};

export const login = async (username: string, password: string) => {
  return fetchApi('/login/', 'POST', {
    username,
    password,
  });
};

export const getQuizzes = async () => {
  return fetchApi('/quizzes/', 'GET', null);
};

export const submitAnswer = async (quizId: number, questionId: number, answer: string) => {
  return fetchApi(`/quizzes/${quizId}/submit_answer/`, 'POST', {
    question_id: questionId,
    answer: answer,
  });
};
