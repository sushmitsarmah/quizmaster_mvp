export type SingleAnswer = {
  type: 'single';
  correctAnswer: string;
};

export type MultiAnswer = {
  type: 'multi';
  correctAnswers: number[];
};

export type SelectWordAnswer = {
  type: 'select-word';
  sentence: string;
  options: string[];
  correctWords: string[];
};

export type Answer = SingleAnswer | MultiAnswer | SelectWordAnswer;

export interface Question {
  id: number;
  type: 'single' | 'multi' | 'select-word';
  text: string;
  options?: string[];
  answer: Answer;
}