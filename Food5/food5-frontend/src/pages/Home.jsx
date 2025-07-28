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
      <a href="/signup" className="btn btn-success">Registrarse</a>    
    
    {/* Contact with Us Section */}
    <div className="mt-5 p-4 border rounded bg-light">
      <h2>Contacta con nosotros</h2>
      <p>¿Tienes alguna pregunta o necesitas ayuda? ¡Estamos aquí para ayudarte!</p>
      <a href="mailto:soporte@food5.com" className="btn btn-outline-secondary">
        Enviar correo a soporte
      </a>
    </div>
    {/* Close main container div */}
    </div>
  );
}