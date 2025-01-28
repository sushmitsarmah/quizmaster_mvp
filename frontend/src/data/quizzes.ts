import { Quiz } from '../types';

export const quizzes: Quiz[] = [
  {
    id: 1,
    title: "World Geography",
    description: "Test your knowledge of world capitals and landmarks",
    image: "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?auto=format&fit=crop&q=80&w=1000",
    questions: [
      {
        id: 1,
        type: 'single',
        text: "What is the capital of France?",
        answer: {
          type: 'single',
          correctAnswer: "Paris"
        }
      },
      {
        id: 2,
        type: 'multi',
        text: "Which of these countries are in South America?",
        options: ["Brazil", "Spain", "Peru", "Colombia"],
        answer: {
          type: 'multi',
          correctAnswers: [0, 2, 3]
        }
      },
      {
        id: 3,
        type: 'select-word',
        text: "Fill in the missing words: The ___ River flows through ___ and ___, eventually emptying into the ___ Sea.",
        answer: {
          type: 'select-word',
          sentence: "The ___ River flows through ___ and ___, eventually emptying into the ___ Sea.",
          options: ["Nile", "Amazon", "Egypt", "Sudan", "Brazil", "Mediterranean", "Red", "Black"],
          correctWords: ["Nile", "Egypt", "Sudan", "Mediterranean"]
        }
      }
    ]
  },
  {
    id: 2,
    title: "Science Quiz",
    description: "Explore the wonders of science",
    image: "https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&q=80&w=1000",
    questions: [
      {
        id: 1,
        type: 'single',
        text: "What is the chemical symbol for Gold?",
        answer: {
          type: 'single',
          correctAnswer: "Au"
        }
      },
      {
        id: 2,
        type: 'multi',
        text: "Which of these are noble gases?",
        options: ["Helium", "Oxygen", "Neon", "Argon"],
        answer: {
          type: 'multi',
          correctAnswers: [0, 2, 3]
        }
      },
      {
        id: 3,
        type: 'select-word',
        text: "Fill in the missing words: ___ contains four ___ bases: ___, ___, ___, and ___.",
        answer: {
          type: 'select-word',
          sentence: "___ contains four ___ bases: ___, ___, ___, and ___.",
          options: ["DNA", "RNA", "nucleotide", "protein", "Adenine", "Thymine", "Cytosine", "Guanine", "Uracil"],
          correctWords: ["DNA", "nucleotide", "Adenine", "Thymine", "Cytosine", "Guanine"]
        }
      }
    ]
  }
];