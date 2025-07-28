import React, { useEffect, useState } from 'react';

let panesCache = null;

const Bread = () => {
    const [panes, setPanes] = useState([]);
    const [loading, setLoading] = useState(true);
    const [form, setForm] = useState({
        name: '',
        calories: '',
        vegan: false,
        gluten_free: false,
        purchase_price: '',
        retail_price: '',
        picture: ''
    });

    //  Obtener panes al montar
    useEffect(() => {
        if (panesCache) {
            setPanes(panesCache);
            setLoading(false);
            return;
        }

        fetch('http://localhost:8000/bread/')
            .then((res) => res.json())
            .then((data) => {
                panesCache = data;
                setPanes(data);
                setLoading(false);
            })
            .catch((err) => {
                console.error('Error al obtener los panes:', err);
                setLoading(false);
            });
    }, []);

    //  Actualización del formulario
    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setForm({
            ...form,
            [name]: type === 'checkbox' ? checked : value
        });
    };

    //  Crear o editar pan
    const handleSubmit = (e) => {
        e.preventDefault();

        const method = form.id ? 'PUT' : 'POST';
        const url = form.id
            ? `http://127.0.0.1:8000/bread/${form.id}/`
            : 'http://127.0.0.1:8000/bread/crear/';

        const dataToSend = { ...form };
        if (!form.id) delete dataToSend.id;

        // 🚫 Evitar enviar picture si está vacío
        if (!dataToSend.picture || dataToSend.picture.trim() === '') {
            delete dataToSend.picture;
        }

        fetch(url, {
            method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dataToSend),
        })
            .then((res) => {
                if (!res.ok) {
                    return res.json().then((errorData) => {
                        console.error('Error del servidor:', errorData);
                        throw new Error(`Error en la respuesta del servidor: ${res.status}`);
                    });
                }
                return res.json();
            })
            .then((data) => {
                if (form.id) {
                    setPanes((prev) => prev.map((p) => (p.id === data.id ? data : p)));
                } else {
                    setPanes((prev) => [...prev, data]);
                }

                panesCache = null;
                setForm({
                    name: '',
                    calories: '',
                    vegan: false,
                    gluten_free: false,
                    purchase_price: '',
                    retail_price: '',
                    picture: '',
                });
            })
            .catch((err) => console.error('Error al guardar el pan:', err));
    };

    //  Cargar datos en el formulario para editar
    const handleEdit = (pan) => {
        setForm({ ...pan });
    };

    //  Eliminar pan
    const handleDelete = (id) => {
        fetch(`http://127.0.0.1:8000/bread/${id}/`, {
            method: 'DELETE',
        })
            .then((res) => {
                if (res.ok) {
                    panesCache = null;
                    setPanes((prev) => prev.filter((p) => p.id !== id));
                }
            })
            .catch((err) => console.error('Error al eliminar:', err));
    };

    return (
        <div className="container my-5 p-4 border rounded shadow-sm bg-light">
            <h2 className="text-center text-uppercase mb-4" style={{ color: '#a67c52' }}>
                Panes disponibles 🍞
            </h2>

            {/* 🧾 Formulario para crear o editar */}
            <form onSubmit={handleSubmit} className="mb-5 row g-3">
                <div className="col-md-4">
                    <input name="name" value={form.name} onChange={handleChange}
                        className="form-control" placeholder="Nombre" required />
                </div>
                <div className="col-md-2">
                    <input name="calories" value={form.calories} onChange={handleChange} type="number"
                        className="form-control" placeholder="Calorías" />
                </div>
                <div className="col-md-2">
                    <input name="purchase_price" value={form.purchase_price} onChange={handleChange} type="number"
                        className="form-control" placeholder="Compra (€)" />
                </div>
                <div className="col-md-2">
                    <input name="retail_price" value={form.retail_price} onChange={handleChange} type="number"
                        className="form-control" placeholder="Venta (€)" />
                </div>
                <div className="col-md-2">
                    <input name="picture" value={form.picture} onChange={handleChange}
                        className="form-control" placeholder="URL imagen" />
                </div>
                <div className="col-md-2 form-check">
                    <label className="form-check-label">Vegano</label>
                    <input name="vegan" type="checkbox" checked={form.vegan} onChange={handleChange}
                        className="form-check-input" />
                </div>
                <div className="col-md-2 form-check">
                    <label className="form-check-label">Sin gluten</label>
                    <input name="gluten_free" type="checkbox" checked={form.gluten_free} onChange={handleChange}
                        className="form-check-input" />
                </div>
                <div className="col-12">
                    <button type="submit" className="btn btn-success">
                        {form.id ? 'Actualizar' : 'Crear'} pan
                    </button>
                    {form.id && (
                        <button type="button" className="btn btn-secondary ms-2"
                            onClick={() => setForm({
                                id: null, name: '', calories: '', vegan: false,
                                gluten_free: false, purchase_price: '', retail_price: '', picture: ''
                            })}>
                            Cancelar
                        </button>
                    )}
                </div>
            </form>

            {/* 🧁 Tarjetas de panes */}
            {loading ? (
                <p>Cargando panes...</p>
            ) : panes.length > 0 ? (
                <div className="row">
                    {panes.map((pan) => (
                        <div className="col-md-4 mb-4" key={pan.id}>
                            <div className="p-3 bg-white border rounded shadow-sm text-center">
                                <img
                                    src={pan.picture || 'https://placehold.co/250x150?text=Sin+imagen'}
                                    alt={pan.name}
                                    className="img-fluid mb-2 rounded"
                                />
                                <h3>{pan.name}</h3>
                                <p><strong>Calorías:</strong> {pan.calories}</p>
                                <p><strong>Vegano:</strong> {pan.vegan ? '✅ Sí' : '❌ No'}</p>
                                <p><strong>Sin gluten:</strong> {pan.gluten_free ? '✅ Sí' : '❌ No'}</p>
                                <p><strong>Compra:</strong> {pan.purchase_price} €</p>
                                <p><strong>Venta:</strong> {pan.retail_price} €</p>
                                <button className="btn btn-sm btn-primary me-2" onClick={() => handleEdit(pan)}>Editar</button>
                                <button className="btn btn-sm btn-danger" onClick={() => handleDelete(pan.id)}>Eliminar</button>
                            </div>
                        </div>
                    ))}
                </div>
            ) : (
                <p>No hay panes disponibles.</p>
            )}
        </div>
    );
};

export default Bread;