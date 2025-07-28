import WelcomeCard from "../components/WelcomeCard";

export default function Home() {
  return (
    <div className="container mt-5 text-center">



      <div className="container mt-5 text-center">
        {/* Imagen superior */}
        <div className="mb-5">
          <img
            src="/assets/food5.png"
            alt="Food5 App Hero"
            className="img-fluid rounded shadow"
            style={{ maxHeight: '350px' }}
          />
        </div>
      </div>

      {/* Hero Section */}
      <div
        className="p-5 rounded shadow"
        style={{
          background: 'linear-gradient(to right, #f0f8ff, #e0f7fa)',
          border: '1px solid #ccc',
        }}
      >
        <h1 className="display-4 text-primary">Bienvenido a Food5 🍽️</h1>
        <p className="lead text-dark">
          Gestiona tus pedidos, menús y más desde un solo lugar.
        </p>
        <WelcomeCard
          title="¿Nuevo aquí?"
          message="Regístrate para empezar a gestionar tu restaurante con estilo."
        />
      </div>

      {/* Beneficios */}
      <div className="mt-5 row">
        <h2 className="mb-4 text-secondary">🥗 ¿Por qué elegir Food5?</h2>
        <div className="col-md-4 mb-4">
          <div className="border rounded p-3 shadow-sm bg-white">
            <h5 className="text-success">Gestión eficiente</h5>
            <p>Controla cada pedido, menú y cliente desde una sola plataforma.</p>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="border rounded p-3 shadow-sm bg-white">
            <h5 className="text-danger">Interfaz intuitiva</h5>
            <p>Diseñada para que cualquier persona pueda usarla sin complicaciones.</p>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="border rounded p-3 shadow-sm bg-white">
            <h5 className="text-info">Soporte dedicado</h5>
            <p>Estamos aquí para ayudarte en cada paso. ¡Nunca estarás solo!</p>
          </div>
        </div>
      </div>


      {/* Testimonios */}
      <div className="mt-5">
        <h2 className="text-secondary mb-4">💬 Lo que dicen nuestros clientes</h2>
        <div className="row">
          <div className="col-md-4 mb-4">
            <div className="border rounded p-4 shadow-sm bg-white">
              <p className="fst-italic">“Food5 ha simplificado toda la gestión de mi restaurante. ¡Ahora tengo más tiempo para mis clientes!”</p>
              <p className="fw-bold mb-0">— Laura G., Madrid</p>
            </div>
          </div>
          <div className="col-md-4 mb-4">
            <div className="border rounded p-4 shadow-sm bg-white">
              <p className="fst-italic">“La interfaz es intuitiva, el soporte es excelente y los resultados se ven desde el día uno.”</p>
              <p className="fw-bold mb-0">— Sergio M., Valencia</p>
            </div>
          </div>
          <div className="col-md-4 mb-4">
            <div className="border rounded p-4 shadow-sm bg-white">
              <p className="fst-italic">“¡Súper recomendado! Food5 nos ha ayudado a crecer y organizar nuestros menús con estilo.”</p>
              <p className="fw-bold mb-0">— Marta F., Sevilla</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  );
}