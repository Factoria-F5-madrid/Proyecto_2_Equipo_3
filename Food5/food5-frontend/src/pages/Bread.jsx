import { useState, useEffect } from 'react';

function Bread() {
  const [breadItems, setBreadItems] = useState([]);{/*React Hook useState -useState(initialState)- lets you add a state variable to your component . useState returns an array with exactly two values:
The current state. During the first render, it will match the initialState you have passed.
The set function that lets you update the state to a different value and trigger a re-render
useState is used here for fetching data (storing bread items) loading state, and error messages,on component mount*/}  
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    {/*hook useEffect handles the initial data fetch when the component mounts. */}
    const fetchBread = async () => {
      try {
        setLoading(true);
        const response = await fetch('http://localhost:8000/bread/');
        
        if (!response.ok) {
          throw new Error('Failed to fetch bread items');
        }
        
        const data = await response.json();
        setBreadItems(data);
      } catch (err) {
        console.error('Error fetching bread:', err);
        setError('Could not load bread items. Make sure the Django server is running.');
        // For now, use dummy data
        setBreadItems([
          { id: 1, name: 'Sourdough Bread', price: 4.50, description: 'Fresh baked sourdough' },
          { id: 2, name: 'Garlic Bread', price: 3.25, description: 'Toasted with garlic butter' },
          { id: 3, name: 'Focaccia', price: 5.00, description: 'Italian herb focaccia' }
        ]);
      } finally {
        setLoading(false);
      }
    };

    fetchBread();
  }, []);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="text-center">
          <div className="spinner-border" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-2">Loading bread items...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="row">
        <div className="col-12">
          <h1 className="mb-4">🍞 Bread</h1>
          
          {error && (
            <div className="alert alert-warning">
              <strong>Note:</strong> {error}
            </div>
          )}
        </div>
      </div>

      <div className="row">
        {breadItems.length > 0 ? (
          breadItems.map((item) => (
            <div key={item.id} className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{item.name}</h5>
                  <p className="card-text">{item.description}</p>
                  <p className="card-text">
                    <strong className="text-success">${item.price}</strong>
                  </p>
                </div>
                <div className="card-footer">
                  <button className="btn btn-primary btn-sm">Add to Order</button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info">
              <h5>No bread items available</h5>
              <p>Check back later or contact the restaurant.</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Bread;