// src/pages/Login.jsx
import { useForm } from 'react-hook-form';
import axios from 'axios';

export default function Login() {
  const { register, handleSubmit } = useForm();

  const onSubmit = async (data) => {
    try {
      const res = await axios.post('http://localhost:8000/api/token/', {
        email: data.email,
        password: data.password,
      });

      localStorage.setItem('access', res.data.access);
      localStorage.setItem('refresh', res.data.refresh);

      alert('Inicio de sesión exitoso');
      // Puedes redirigir al usuario, por ejemplo:
      // window.location.href = '/dashboard';
    } catch (err) {
      console.error(err);
      alert('Error en el login. Verifica correo y contraseña.');
    }
  };

  return (
    <div className="container mt-5" style={{ maxWidth: "400px" }}>
      <h2 className="mb-4 text-center">Iniciar sesión</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="mb-3">
          <label className="form-label">Correo electrónico</label>
          <input
            {...register('email')}
            type="email"
            className="form-control"
            placeholder="Correo electrónico"
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Contraseña</label>
          <input
            {...register('password')}
            type="password"
            className="form-control"
            placeholder="Contraseña"
            required
          />
        </div>
        <button type="submit" className="btn btn-primary w-100">
          Entrar
        </button>
      </form>
    </div>
  );
}