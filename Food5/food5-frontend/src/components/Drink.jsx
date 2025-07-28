import React, { useEffect, useState } from 'react';

let drinkCache = null;

const Drink = () => {
    const [drinks, setDrinks] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (drinkCache) {
            setDrinks(drinkCache);
            setLoading(false);
            return;
        }

        fetch('http://localhost:8000/drinks/')
            .then((res) => res.json())
            .then((data) => {
                drinkCache = data;
                setDrinks(data);
                setLoading(false);
            })
            .catch((err) => {
                console.error('Error al obtener las bebidas:', err);
                setLoading(false);
            });
    }, []);

    return (
        <div className="container my-5 p-4 border rounded shadow-sm bg-light">
            <h2 className="text-center text-uppercase mb-4 text-primary">Bebidas refrescantes 🍹</h2>
            <div className="row">
                {drinks.map((drink) => (
                    <div className="col-md-4 mb-4" key={drink.id || drink.name}>
                        <div className="p-3 bg-white border rounded shadow-sm text-center">
                            <img
                                src={drink.picture || 'https://placehold.co/250x150?text=Sin+imagen'}
                                alt={drink.name}
                                className="img-fluid mb-2 rounded"
                            />
                            <h3>{drink.name}</h3>
                            <p><strong>Calorías:</strong> {drink.calories}</p>
                            <p><strong>Vegano:</strong> {drink.vegan ? '✅ Sí' : '❌ No'}</p>
                            <p><strong>Sin gluten:</strong> {drink.gluten_free ? '✅ Sí' : '❌ No'}</p>
                            <p><strong>Compra:</strong> {drink.purchase_price} €</p>
                            <p><strong>Venta:</strong> {drink.retail_price} €</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Drink;