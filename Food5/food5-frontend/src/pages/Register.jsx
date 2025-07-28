import { useForm } from 'react-hook-form';
import axios from 'axios';

export default function Register() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    try {
      await axios.post('http://localhost:8000/user/register/', data);
      alert('✅ Registro exitoso. Ahora puedes iniciar sesión.');
      window.location.href = '/login';

    } catch (err) {
      console.error(err);
      alert('❌ Hubo un error al registrarse. Revisa los datos e inténtalo de nuevo.');
    }
  };

  return (
    <div className="container mt-5" style={{ maxWidth: '400px' }}>
      <h2 className="mb-4 text-center">Registro</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        {/* Nombre */}
        <div className="mb-3">
          <label className="form-label">Nombre</label>
          <input
            {...register('nombre', {
              required: 'Este campo es obligatorio',
              minLength: {
                value: 2,
                message: 'El nombre debe tener al menos 2 caracteres',
              },
            })}
            className="form-control"
            placeholder="Tu nombre visible"
          />
          {errors.nombre && <p className="text-danger">{errors.nombre.message}</p>}
        </div>

        {/* Correo */}
        <div className="mb-3">
          <label className="form-label">Correo</label>
          <input
            {...register('email', {
              required: 'Este campo es obligatorio',
              pattern: {
                value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                message: 'Introduce un correo válido',
              },
            })}
            type="email"
            className="form-control"
            placeholder="ejemplo@email.com"
          />
          {errors.email && <p className="text-danger">{errors.email.message}</p>}
        </div>

        {/* Contraseña */}
        <div className="mb-3">
          <label className="form-label">Contraseña</label>
          <input
            {...register('password', {
              required: 'Este campo es obligatorio',
              minLength: {
                value: 8,
                message: 'La contraseña debe tener al menos 8 caracteres',
              },
            })}
            type="password"
            className="form-control"
            placeholder="••••••••"
          />
          {errors.password && <p className="text-danger">{errors.password.message}</p>}
        </div>

        <button type="submit" className="btn btn-primary w-100">
          Crear cuenta
        </button>
      </form>
    </div>
  );
}