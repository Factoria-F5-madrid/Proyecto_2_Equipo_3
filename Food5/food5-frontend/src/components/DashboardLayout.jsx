import Navbar from "./Navbar";


const DashboardLayout = ({ children }) => {
  return (
    <div className="dashboard-container">
      <div className="dashboard-content">
      
        <main className="dashboard-main">
          {children}
        </main>
      </div>
    </div>
  );
};

export default DashboardLayout;