// src/pages/Home.jsx
import WelcomeCard from "../components/WelcomeCard";


export default function Home() {
  return (
    <div className="container mt-5 text-center">
      <h1 className="display-4">Bienvenido a Food5 🍽️</h1>
      <p className="lead">Gestiona tus pedidos, menús y más desde un solo lugar.</p>
      <WelcomeCard 
        title="¿Nuevo aquí?" 
        message="Regístrate para empezar a gestionar tu restaurante con estilo." 
      />
      <a href="/login" className="btn btn-primary">Iniciar sesión</a>
    </div>
  );
}