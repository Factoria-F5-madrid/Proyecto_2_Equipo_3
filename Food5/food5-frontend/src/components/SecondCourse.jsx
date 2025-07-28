import React, { useEffect, useState } from 'react';

let secondCourseCache = null;

const SecondCourse = () => {
    const [dishes, setDishes] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (secondCourseCache) {
            setDishes(secondCourseCache);
            setLoading(false);
            return;
        }

        fetch('http://localhost:8000/second_course/')
            .then((res) => res.json())
            .then((data) => {
                secondCourseCache = data;
                setDishes(data);
                setLoading(false);
            })
            .catch((err) => {
                console.error('Error al obtener los segundos platos:', err);
                setLoading(false);
            });
    }, []);

    return (
        <div className="container my-5 p-4 border rounded shadow-sm bg-light">
            <h2 className="text-center text-uppercase mb-4 text-warning">Platos principales 🍲</h2>
            <div className="row">
                {dishes.map((dish) => (
                    <div className="col-md-4 mb-4" key={dish.id || dish.name}>
                        <div className="p-3 bg-white border rounded shadow-sm text-center">
                            <img
                                src={dish.picture || 'https://placehold.co/250x150?text=Sin+imagen'}
                                alt={dish.name}
                                className="img-fluid mb-2 rounded"
                            />
                            <h3>{dish.name}</h3>
                            <p><strong>Calorías:</strong> {dish.calories}</p>
                            <p><strong>Vegano:</strong> {dish.vegan ? '✅ Sí' : '❌ No'}</p>
                            <p><strong>Sin gluten:</strong> {dish.gluten_free ? '✅ Sí' : '❌ No'}</p>
                            <p><strong>Compra:</strong> {dish.purchase_price} €</p>
                            <p><strong>Venta:</strong> {dish.retail_price} €</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default SecondCourse;