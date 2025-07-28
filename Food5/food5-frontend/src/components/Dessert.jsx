import React, { useEffect, useState } from 'react';

let dessertCache = null;

const Dessert = () => {
    const [desserts, setDesserts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (dessertCache) {
            setDesserts(dessertCache);
            setLoading(false);
            return;
        }

        fetch('http://localhost:8000/dessert/')
            .then((res) => res.json())
            .then((data) => {
                dessertCache = data;
                setDesserts(data);
                setLoading(false);
            })
            .catch((err) => {
                console.error('Error al obtener los postres:', err);
                setLoading(false);
            });
    }, []);

    return (
        <div className="container my-5 p-4 border rounded shadow-sm bg-light">
            <h2 className="text-center text-uppercase mb-4 text-danger">Postres deliciosos 🍰</h2>
            <div className="row">
                {desserts.map((dessert) => (
                    <div className="col-md-4 mb-4" key={dessert.id || dessert.name}>
                        <div className="p-3 bg-white border rounded shadow-sm text-center">
                            <img
                                src={dessert.picture || 'https://placehold.co/250x150?text=Sin+imagen'}
                                alt={dessert.name}
                                className="img-fluid mb-2 rounded"
                            />
                            <h3>{dessert.name}</h3>
                            <p><strong>Calorías:</strong> {dessert.calories}</p>
                            <p><strong>Vegano:</strong> {dessert.vegan ? '✅ Sí' : '❌ No'}</p>
                            <p><strong>Sin gluten:</strong> {dessert.gluten_free ? '✅ Sí' : '❌ No'}</p>
                            <p><strong>Compra:</strong> {dessert.purchase_price} €</p>
                            <p><strong>Venta:</strong> {dessert.retail_price} €</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Dessert;