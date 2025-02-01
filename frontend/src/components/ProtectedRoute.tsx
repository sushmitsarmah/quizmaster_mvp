const Protected = () => {
  const isAuthenticated = !!localStorage.getItem('token'); // Check if token exists

  return isAuthenticated;
};

export default Protected; 