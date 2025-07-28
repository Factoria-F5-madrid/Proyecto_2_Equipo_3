// src/pages/DashboardPage.jsx

import WelcomeCard from "../components/WelcomeCard";
import DashboardLayout from "../components/DashboardLayout";
import { useState, useEffect } from 'react';
import axios from 'axios';

function QuickStats({ orders }) {
  const totalRevenue = orders.reduce((sum, order) => sum + parseFloat(order.retail_price || 0), 0);
  const todayOrders = orders.filter(order => {
    const orderDate = new Date(order.gotten_date).toDateString();
    const today = new Date().toDateString();
    return orderDate === today;
  }).length;

  return (
    <div className="row g-3 mb-4">
      <div className="col-md-3">
        <div className="card border-0 bg-primary text-white h-100">
          <div className="card-body d-flex align-items-center">
            <div className="flex-grow-1">
              <h6 className="card-title mb-0">Total Pedidos</h6>
              <h3 className="mb-0">{orders.length}</h3>
            </div>
            <div className="fs-1 opacity-50">📋</div>
          </div>
        </div>
      </div>
      <div className="col-md-3">
        <div className="card border-0 bg-success text-white h-100">
          <div className="card-body d-flex align-items-center">
            <div className="flex-grow-1">
              <h6 className="card-title mb-0">Ingresos Total</h6>
              <h3 className="mb-0">€{totalRevenue.toFixed(2)}</h3>
            </div>
            <div className="fs-1 opacity-50">💰</div>
          </div>
        </div>
      </div>
      <div className="col-md-3">
        <div className="card border-0 bg-warning text-white h-100">
          <div className="card-body d-flex align-items-center">
            <div className="flex-grow-1">
              <h6 className="card-title mb-0">Pedidos Hoy</h6>
              <h3 className="mb-0">{todayOrders}</h3>
            </div>
            <div className="fs-1 opacity-50">📅</div>
          </div>
        </div>
      </div>
      <div className="col-md-3">
        <div className="card border-0 bg-info text-white h-100">
          <div className="card-body d-flex align-items-center">
            <div className="flex-grow-1">
              <h6 className="card-title mb-0">Promedio/Pedido</h6>
              <h3 className="mb-0">€{orders.length ? (totalRevenue / orders.length).toFixed(2) : '0.00'}</h3>
            </div>
            <div className="fs-1 opacity-50">📊</div>
          </div>
        </div>
      </div>
    </div>
  );
}

// Componente de pedidos recientes mejorado
function RecentOrdersCard({ orders }) {
  const recentOrders = orders.slice(0, 5);

  const getStatusBadge = (order) => {
    // Simulamos diferentes estados basados en la fecha
    const orderDate = new Date(order.gotten_date);
    const now = new Date();
    const diffHours = (now - orderDate) / (1000 * 60 * 60);

    if (diffHours < 2) return { class: 'bg-success', text: 'Completado', icon: '✅' };
    if (diffHours < 24) return { class: 'bg-warning', text: 'En proceso', icon: '⏳' };
    return { class: 'bg-secondary', text: 'Entregado', icon: '📦' };
  };

  return (
    <div className="card border-0 shadow-sm h-100">
      <div className="card-header bg-white border-bottom-0 pb-0">
        <div className="d-flex justify-content-between align-items-center">
          <h5 className="card-title mb-0">
            <i className="bi bi-clock-history me-2"></i>
            Pedidos Recientes
          </h5>
          <span className="badge bg-primary rounded-pill">{recentOrders.length}</span>
        </div>
      </div>
      <div className="card-body pt-3">
        {recentOrders.length === 0 ? (
          <div className="text-center py-5 text-muted">
            <div className="fs-1 mb-3">📋</div>
            <p>No hay pedidos recientes</p>
          </div>
        ) : (
          <div className="list-group list-group-flush">
            {recentOrders.map((order, index) => {
              const status = getStatusBadge(order);
              return (
                <div key={order.id} className="list-group-item border-0 px-0 py-3">
                  <div className="d-flex justify-content-between align-items-start">
                    <div className="d-flex align-items-center flex-grow-1">
                      <div className="bg-light rounded-circle p-2 me-3">
                        <span className="fs-6">{status.icon}</span>
                      </div>
                      <div className="flex-grow-1">
                        <h6 className="mb-1 fw-semibold">
                          {order.customer?.name || `Cliente #${order.id}`}
                        </h6>
                        <p className="mb-1 text-muted small">
                          Pedido #{order.id} • {new Date(order.gotten_date).toLocaleDateString('es-ES')}
                        </p>
                        <span className={`badge ${status.class} badge-sm`}>
                          {status.text}
                        </span>
                      </div>
                    </div>
                    <div className="text-end">
                      <div className="fw-bold text-success fs-6">€{order.retail_price}</div>
                      <small className="text-muted">
                        {new Date(order.gotten_date).toLocaleTimeString('es-ES',
                          { hour: '2-digit', minute: '2-digit' })}
                      </small>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}

// Componente de gráfico de actividad simulado
function ActivityChart() {
  return (
    <div className="card border-0 shadow-sm h-100">
      <div className="card-header bg-white border-bottom-0">
        <h5 className="card-title mb-0">
          <i className="bi bi-graph-up me-2"></i>
          Actividad Semanal
        </h5>
      </div>
      <div className="card-body">
        <div className="d-flex justify-content-between align-items-end" style={{ height: '150px' }}>
          {['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'].map((day, index) => {
            const height = Math.random() * 80 + 20;
            return (
              <div key={day} className="text-center flex-fill">
                <div
                  className="bg-primary rounded-top mb-2 mx-1 position-relative"
                  style={{ height: `${height}px`, minWidth: '20px' }}
                  title={`${day}: ${Math.floor(height / 4)} pedidos`}
                >
                  <div className="position-absolute top-0 start-50 translate-middle-x text-white small"
                    style={{ marginTop: '-20px', fontSize: '10px' }}>
                    {Math.floor(height / 4)}
                  </div>
                </div>
                <small className="text-muted">{day}</small>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

// Componente principal de lista de pedidos mejorado
function OrderList() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  const fetchOrders = async () => {
    try {
      setLoading(true);
      const response = await axios.get('http://127.0.0.1:8000/api/order/');
      setOrders(response.data);
    } catch (error) {
      console.error('Error al obtener órdenes:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  const filteredOrders = orders.filter(order =>
    order.customer?.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    order.id.toString().includes(searchTerm)
  );

  if (loading) {
    return (
      <div className="card border-0 shadow-sm">
        <div className="card-body text-center py-5">
          <div className="spinner-border text-primary mb-3" role="status">
            <span className="visually-hidden">Cargando...</span>
          </div>
          <p className="text-muted">Cargando pedidos...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="card border-0 shadow-sm">
      <div className="card-header bg-white border-bottom">
        <div className="row align-items-center">
          <div className="col-md-6">
            <h5 className="card-title mb-0">
              <i className="bi bi-list-ul me-2"></i>
              Todos los Pedidos
            </h5>
          </div>
          <div className="col-md-6">
            <div className="input-group">
              <span className="input-group-text bg-light border-end-0">
                🔍
              </span>
              <input
                type="text"
                className="form-control border-start-0"
                placeholder="Buscar por cliente o ID..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
          </div>
        </div>
      </div>
      <div className="card-body p-0">
        {filteredOrders.length === 0 ? (
          <div className="text-center py-5 text-muted">
            <div className="fs-1 mb-3">🔍</div>
            <p>No se encontraron pedidos</p>
          </div>
        ) : (
          <div className="table-responsive">
            <table className="table table-hover mb-0">
              <thead className="table-light">
                <tr>
                  <th className="border-0 fw-semibold">#ID</th>
                  <th className="border-0 fw-semibold">Cliente</th>
                  <th className="border-0 fw-semibold">Fecha</th>
                  <th className="border-0 fw-semibold">Total</th>
                  <th className="border-0 fw-semibold">Estado</th>
                </tr>
              </thead>
              <tbody>
                {filteredOrders.map((order, index) => (
                  <tr key={order.id} className="animate-row" style={{ animationDelay: `${index * 0.1}s` }}>
                    <td className="align-middle">
                      <span className="badge bg-light text-dark">#{order.id}</span>
                    </td>
                    <td className="align-middle">
                      <div className="d-flex align-items-center">
                        <div className="bg-primary rounded-circle p-2 me-3 text-white" style={{ width: '35px', height: '35px', fontSize: '14px' }}>
                          {(order.customer?.name || 'C').charAt(0).toUpperCase()}
                        </div>
                        <div>
                          <div className="fw-semibold">{order.customer?.name || 'Cliente Anónimo'}</div>
                          <small className="text-muted">ID: {order.id}</small>
                        </div>
                      </div>
                    </td>
                    <td className="align-middle">
                      <div>
                        <div>{new Date(order.gotten_date).toLocaleDateString('es-ES')}</div>
                        <small className="text-muted">
                          {new Date(order.gotten_date).toLocaleTimeString('es-ES',
                            { hour: '2-digit', minute: '2-digit' })}
                        </small>
                      </div>
                    </td>
                    <td className="align-middle">
                      <span className="fs-6 fw-bold text-success">€{order.retail_price}</span>
                    </td>
                    <td className="align-middle">
                      <span className="badge bg-success">Completado</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

const DashboardPage = () => {
  const [view, setView] = useState('dashboard');
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
    <DashboardLayout>
      <div className="container-fluid py-4">
        {view === 'dashboard' ? (
          <>
            {/* Header mejorado */}
            <div className="row mb-4">
              <div className="col-md-8">
                <WelcomeCard
                  title="🍽️ Panel Administrativo Food5"
                  message="Maneja tu catering de manera eficiente y sencilla. Todo bajo control."
                />
              </div>
              <div className="col-md-4 d-flex align-items-center justify-content-end">
                <button
                  onClick={() => setView('orders')}
                  className="btn btn-primary btn-lg shadow-sm"
                >
                  <i className="bi bi-list-ul me-2"></i>
                  Ver todos los pedidos
                </button>
              </div>
            </div>

            {/* Estadísticas rápidas */}
            <QuickStats orders={orders} />


            {/* Dashboard principal */}
            <div className="row g-4">
              <div className="col-lg-8">
                <div className="row g-4">
                  <div className="col-12">
                    <RecentOrdersCard orders={orders} />
                  </div>
                </div>
              </div>
              <div className="col-lg-4">
                <ActivityChart />
              </div>
            </div>

          </>
        ) : (
          <div>
            <div className="row mb-4">
              <div className="col-12">
                <button
                  onClick={() => setView('dashboard')}
                  className="btn btn-success btn-lg shadow-sm"
                >
                  <i className="bi bi-arrow-left me-2"></i>
                  Volver al Panel Administrativo
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
          transition: all 0.3s ease;
          box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        }

        .card:hover {
          transform: translateY(-2px);
          box-shadow: 0 8px 15px rgba(0,0,0,0.12);
        }

        .animate-row {
          animation: slideInUp 0.6s ease-out forwards;
          opacity: 0;
        }

        @keyframes slideInUp {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        .list-group-item {
          transition: background-color 0.2s ease;
        }

        .list-group-item:hover {
          background-color: #f8f9fa;
        }

        .badge-sm {
          font-size: 0.7em;
        }

        .btn {
          transition: all 0.3s ease;
        }

        .btn:hover {
          transform: translateY(-1px);
        }

        .table-responsive {
          border-radius: 0.5rem;
        }

        .bg-primary {
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        }

        .bg-success {
          background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;
        }

        .bg-warning {
          background: linear-gradient(135deg, #fa709a 0%, #fee140 100%) !important;
        }

        .bg-info {
          background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%) !important;
        }

        .input-group-text {
          border: 1px solid #dee2e6;
        }

        .form-control:focus {
          border-color: #86b7fe;
          box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
        }
      `}</style>
    </DashboardLayout>
  );
};

export default DashboardPage;
