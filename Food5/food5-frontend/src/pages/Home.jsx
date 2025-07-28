import { useState, useEffect } from 'react';
import { api } from '../services/api';
import WelcomeCard from "../components/WelcomeCard";


export default function Home() {
  const [menuItems, setMenuItems] = useState([]);
  const [drinks, setDrinks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [menuData, drinkData] = await Promise.all([
          api.getMenus(),
          api.getDrinks()
        ]);
        
        setMenuItems(menuData);
        setDrinks(drinkData);
      } catch (err) {
        setError('Failed to fetch data from server');
        console.error('Error fetching data:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div className="container mt-4">Loading...</div>;
  if (error) return <div className="container mt-4 alert alert-danger">{error}</div>;

  return (
    <div className="container mt-4">
      <h1>Welcome to Food5 Restaurant</h1>
      
      <div className="row">
        <div className="col-md-6">
          <h2>Menu Items</h2>
          {menuItems.length > 0 ? (
            <div className="list-group">
              {menuItems.map((item) => (
                <div key={item.id} className="list-group-item">
                  <h5>{item.name}</h5>
                  <p>Price: ${item.price}</p>
                </div>
              ))}
            </div>
          ) : (
            <p>No menu items available</p>
          )}
        </div>
        
        <div className="col-md-6">
          <h2>Drinks</h2>
          {drinks.length > 0 ? (
            <div className="list-group">
              {drinks.map((drink) => (
                <div key={drink.id} className="list-group-item">
                  <h5>{drink.name}</h5>
                  <p>Price: ${drink.retail_price}</p>
                  {drink.vegan && <span className="badge bg-success">Vegan</span>}
                </div>
              ))}
            </div>
          ) : (
            <p>No drinks available</p>
          )}
        </div>
      </div>
      <WelcomeCard 
        title="¿Nuevo aquí?" 
        message="Regístrate para empezar a gestionar tu restaurante con estilo." 
      />
      <a href="/login" className="btn btn-primary">Iniciar sesión</a>
    </div>
  );
}