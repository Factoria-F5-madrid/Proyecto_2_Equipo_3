// src/pages/DashboardPage.jsx
import Cards from "../components/Cards";
import WelcomeCard from "../components/WelcomeCard";
import DashboardLayout from "../components/DashboardLayout";
import { useState, useEffect } from 'react';
import axios from 'axios';

function OrderList() {
  const [orders, setOrders] = useState([]);

  const fetchOrders = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/order/');
      setOrders(response.data);
    } catch (error) {
      console.error('Error al obtener órdenes:', error);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  return (
    <div className="card">
      <div className="card-header">
        <h6 className="mb-0">Pedidos</h6>
      </div>
      <div className="card-body">
        {orders.map((order) => (
          <div key={order.id} className="d-flex justify-content-between align-items-center mb-3">
            <div className="d-flex align-items-center">
              <span className="badge bg-success rounded-pill me-2"></span>
              <div>
                <div className="fw-semibold">{order.customer?.name || 'Cliente'}</div>
                <small className="text-muted">Pedido #{order.id}</small>
              </div>
            </div>
            <div>
              <small className="text-muted">{order.gotten_date}</small>
            </div>
            <span className="text-success fw-bold">€{order.retail_price}</span>
          </div>
         
        ))}
      </div>
    </div>
  );
}

const DashboardPage = () => {
  const [view, setView] = useState('dashboard');

  return (
    <DashboardLayout>
      <div className="container-fluid py-4">
        {view === 'dashboard' ? (
          <>
            {/* Welcome Card y botón */}
            <div className="row mb-4">
              <div className="col-md-8">
                <WelcomeCard 
                  title="Panel Administrativo" 
                  message="Maneja tu catering de manera eficiente y sencilla." 
                />
              </div>
              <div className="col-md-4 d-flex align-items-center justify-content-end">
                <button 
                  onClick={() => setView('orders')}
                  className="btn btn-primary"
                >
                  Ver todos los pedidos
                </button>
              </div>
            </div>

            {/* Cards de resumen */}
            <div className="row mb-4">
              <div className="col-12">
                <Cards />
              </div>
            </div>

          </>
        ) : (
          <div>
            <div className="row mb-3">
              <div className="col-12">
                <button 
                  onClick={() => setView('dashboard')}
                  className="btn btn-success"
                >
                  ← Volver al Panel Administrativo
                </button>
              </div>
            </div>

            <div className="row">
              <div className="col-12">
                <OrderList />
              </div>
            </div>
          </div>
        )}
      </div>

      <style jsx>{`
        .cards-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
          gap: 1rem;
          margin-top: 1rem;
        }

        .card {
          padding: 1rem;
          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
      `}</style>
    </DashboardLayout>
  );
};

export default DashboardPage;
