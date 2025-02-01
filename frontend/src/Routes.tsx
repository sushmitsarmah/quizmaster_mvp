import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import QuizPage from './pages/QuizPage';
import NotFound from './pages/NotFound';

const routesObj = [
    {
        name: "login",
        path: "/login",
        element: <Login />,
        protected: false
    },
    {
        name: "dashboard",
        path: "/",
        element: <Dashboard />,
        protected: true
    },
    {
        name: "quiz",
        path: "/quiz/:id",
        element: <QuizPage />,
        protected: true
    },
    {
        name: "notFound",
        path: "*",
        element: <NotFound />,
        protected: true
    }
];

export default routesObj;