import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Navbar from './components/Navbar';
import Login from './pages/Login';

function App() {
  return (
    <BrowserRouter>
     <Navbar />

      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Home />} />
    
      </Routes>
    </BrowserRouter>
  );
}

export default App;
