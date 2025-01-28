import React from 'react';
import { Brain } from 'lucide-react';

export function Navbar() {
  return (
    <nav className="bg-gradient-to-r from-blue-600 to-blue-800 text-white shadow-lg">
      <div className="container mx-auto px-4 py-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <Brain className="w-8 h-8" />
            <span className="text-2xl font-bold">QuizMaster</span>
          </div>
          <div className="flex items-center space-x-4">
            <button className="px-4 py-2 rounded-lg bg-white/10 hover:bg-white/20 transition-colors">
              About
            </button>
            <button className="px-4 py-2 rounded-lg bg-white/10 hover:bg-white/20 transition-colors">
              Contact
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}