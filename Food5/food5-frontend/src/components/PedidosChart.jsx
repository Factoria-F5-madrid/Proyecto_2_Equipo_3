// src/components/PedidosChart.jsx
import { useEffect, useState } from 'react';
import axios from 'axios';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from 'recharts';
import dayjs from 'dayjs';

const chartStyle = {
  width: "100%",
  height: "400px",
  background: "#111",
  borderRadius: "12px",
  padding: "1rem",
  color: "#fff",
};

export default function PedidosChart() {
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/order/');
        const orders = response.data;

        // Agrupar pedidos por fecha
        const grouped = {};

        orders.forEach(order => {
          const date = dayjs(order.gotten_date).format('YYYY-MM-DD');
          if (!grouped[date]) grouped[date] = 0;
          grouped[date]++;
        });

        const formattedData = Object.entries(grouped).map(([date, count]) => ({
          date,
          pedidos: count
        }));

        setChartData(formattedData);
      } catch (error) {
        console.error("Error al obtener pedidos:", error);
      }
    };

    fetchOrders();
  }, []);

  return (
    <div style={chartStyle}>
      <h5 style={{ color: '#fff', marginBottom: '1rem' }}>Pedidos por Fecha</h5>
      <ResponsiveContainer width="100%" height="90%">
        <BarChart data={chartData} margin={{ top: 20, right: 30, left: 10, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#333" />
          <XAxis dataKey="date" stroke="#ccc" />
          <YAxis stroke="#ccc" />
          <Tooltip />
          <Bar dataKey="pedidos" fill="#60a5fa" name="Cantidad de pedidos" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
