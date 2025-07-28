export default function Menu() {
  return (
    <div className="container mt-5">
      <h1 className="display-4 text-center">Menú</h1>
      <p className="lead text-center">
        Explora los platos y bebidas disponibles en Food5.
      </p>
      {/* Aquí puedes agregar la lógica para mostrar los platos y bebidas */}
      <div className="row">
        <div className="col-md-6">
          <h2>Platos</h2>
          {/* Lista de platos */}
        </div>
        <div className="col-md-6">
          <h2>Bebidas</h2>
          {/* Lista de bebidas */}
        </div>
      </div>
    </div>
  );
}