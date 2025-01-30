import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import QuizPage from './pages/QuizPage';
import PrivateRoute from './components/PrivateRoute';
import { Navbar } from './components/Navbar';

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-100">
        <Navbar />
        <Routes>
          <Route path="/login" element={<Login />} />

          {PrivateRoute({ element: <Dashboard />, path: '/' })}
          {PrivateRoute({ element: <QuizPage />, path: '/quiz/:id' })}
          {/* <PrivateRoute path="/" element={<Dashboard />} />
          <PrivateRoute path="/quiz/:id" element={<QuizPage />} /> */}
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;