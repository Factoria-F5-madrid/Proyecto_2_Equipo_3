import { useForm } from 'react-hook-form';
import axios from 'axios';

export default function Register() {
  const { register, handleSubmit } = useForm();

  const onSubmit = async (data) => {
    try {
      await axios.post('http://localhost:8000/api/register/', data);
      alert('✅ Registro exitoso. Ahora puedes iniciar sesión.');
    } catch (err) {
      console.error(err);
      alert('❌ Hubo un error al registrarse. Revisa los datos e inténtalo de nuevo.');
    }
  };

  return (
    <div className="container mt-5" style={{ maxWidth: "400px" }}>
      <h2 className="mb-4 text-center">Registro</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="mb-3">
          <label className="form-label">Nombre</label>
          <input
            {...register('nombre')}
            className="form-control"
            placeholder="Tu nombre visible"
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Correo</label>
          <input
            {...register('email')}
            type="email"
            className="form-control"
            placeholder="ejemplo@email.com"
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Contraseña</label>
          <input
            {...register('password')}
            type="password"
            className="form-control"
            placeholder="••••••••"
          />
        </div>
        <button type="submit" className="btn btn-success w-100">
          Crear cuenta
        </button>
      </form>
    </div>
  );
}