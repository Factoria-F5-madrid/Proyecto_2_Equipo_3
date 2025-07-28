// src/pages/Contact.jsx
import { useForm } from 'react-hook-form';
import axios from 'axios';

export default function Contact() {
    const { register, handleSubmit, reset } = useForm();

    const onSubmit = async (data) => {
        try {
            await axios.post('http://localhost:8000/contact/', {
                name: data.name,
                email: data.email,
                message: data.message,
            });

            alert('Mensaje enviado con éxito 🎉');
            reset(); // Limpia el formulario
        } catch (err) {
            console.error('Error al enviar el mensaje:', err);
            alert('Hubo un problema al enviar el mensaje.');
        }
    };

    return (
        <div className="container mt-5" style={{ maxWidth: '500px' }}>
            <h2 className="mb-4 text-center">Contacto</h2>
            <form onSubmit={handleSubmit(onSubmit)}>
                <div className="mb-3">
                    <label className="form-label">Nombre</label>
                    <input
                        {...register('name', { required: true })}
                        type="text"
                        className="form-control"
                        placeholder="Tu nombre"
                    />
                </div>
                <div className="mb-3">
                    <label className="form-label">Correo electrónico</label>
                    <input
                        {...register('email', { required: true })}
                        type="email"
                        className="form-control"
                        placeholder="Tu correo"
                    />
                </div>
                <div className="mb-3">
                    <label className="form-label">Mensaje</label>
                    <textarea
                        {...register('message', { required: true })}
                        className="form-control"
                        rows="4"
                        placeholder="Escribe tu mensaje..."
                    />
                </div>
                <button type="submit" className="btn btn-success w-100">
                    Enviar mensaje
                </button>
            </form>
        </div>
    );
}