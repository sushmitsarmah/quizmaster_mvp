import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Navbar } from './components/Navbar';

import routesObj from './Routes';
import Protected from './components/ProtectedRoute';

const App = () => {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-100">
        <Navbar />
        <Routes>
              {routesObj.map((route) => (
               <Route
                   key={route.name}
                   path={route.path}
                   element={
                    !route.protected ? route.element : Protected() ? route.element : <Navigate to="/login" />
                  }
               />
              ))}
          </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;