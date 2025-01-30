import React from 'react';
import { Route, redirect } from 'react-router-dom';

interface PrivateRouteProps {
  element: React.ReactElement;
  path: string;
}

const PrivateRoute = ({ element, path }: PrivateRouteProps) => {
  const isAuthenticated = !!localStorage.getItem('token'); // Check if token exists

  if (isAuthenticated) {
    return <Route path={path} element={element} />
  } else {
    redirect('/login');
    return null;
  }
};

export default PrivateRoute; 