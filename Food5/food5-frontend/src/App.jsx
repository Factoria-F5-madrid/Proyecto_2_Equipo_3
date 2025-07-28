import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Navbar from './components/Navbar';
import Login from './pages/Login';
import Register from './pages/Register';
import Bread from './pages/Bread';

function App() {
  return (
    <BrowserRouter> {/*enables single-page application (SPA) behavior, allowing users to navigate between different views without triggering full page reloads. it maintains application state and provides a seamless user experience while your frontend makes API calls to your Python backend.*/}
      <Navbar /> {/*component positioned outside the <Routes> container will remain persistent across all navigation*/}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/bread" element={<Bread />} />
        <Route path="*" element={<NotFound />} /> {/* Adds a catch-all route for unmatched URLs. handles cases where users might bookmark URLs or share links that don't exist. Instead of getting a server error from your Python backend, users get a friendly 404 page that keeps them within your application ecosystem. */}
      </Routes>
    </BrowserRouter>
  );
}

// Simple 404 component
function NotFound() {
  return (
    <div className="container mt-4">
      <div className="text-center">
        <h1>404 - Page Not Found</h1>
        <p>The page you're looking for doesn't exist.</p>
        <a href="/" className="btn btn-primary">Go Home</a>
      </div>
    </div>
  );
}

export default App;
