import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Navbar from './components/Navbar';
import Login from './pages/Login';
import DashboardPage from "./pages/DashboardPage";
import Register from './pages/Register';
import Orders from './pages/Orders';
import Productos from './pages/Productos';
import Contact from './pages/Contact';


function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/orders" element={<Orders />} />
        <Route path="/productos" element={<Productos />} />
        <Route path="/contacto" element={<Contact />} />


      </Routes>
    </BrowserRouter>
  );
}

export default App;
