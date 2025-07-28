const OrdersList = () => {
//   return (
//      <div>
//       <h2>Lista de Pedidos</h2>
//       <div style={{ background: "#eee", padding: "20px", textAlign: "center" }}>
//         [Aquí iría un gráfico...]
//       </div>
//     </div>
//   );
return (
    <div className="p-6 max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Órdenes por Rango de Fecha</h2>
      <table className="w-full border">
        <thead className="bg-gray-100">
          <tr>
            <th className="border px-4 py-2">ID</th>
            <th className="border px-4 py-2">Cliente</th>
            <th className="border px-4 py-2">Precio Compra</th>
            <th className="border px-4 py-2">Precio Venta</th>
            <th className="border px-4 py-2">Fecha Pedido</th>
          </tr>
          
        </thead>
        <tbody>
          {orders.length === 0 ? (
            <tr>
              <td colSpan="5" className="text-center py-4">No hay órdenes en ese rango.</td>
            </tr>
          ) : (
            orders.map((order) => (
              <tr key={order.id}>
                <td className="border px-4 py-2">{order.id}</td>
                <td className="border px-4 py-2">{order.customer?.name || '—'}</td>
                <td className="border px-4 py-2">€{order.purchase_price}</td>
                <td className="border px-4 py-2">€{order.retail_price}</td>
                <td className="border px-4 py-2">{new Date(order.gotten_date).toLocaleDateString()}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );

};


