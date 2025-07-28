import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Navbar from './components/Navbar';
import Login from './pages/Login';
import DashboardPage from "./pages/DashboardPage";


function App() {
  return (
    <BrowserRouter>
     <Navbar />

      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<DashboardPage />} />
    
      </Routes>
    </BrowserRouter>
  );
}

export default App;
