// src/components/WelcomeCard.jsx
export default function WelcomeCard({ title, message }) {
  return (
    <div className="card p-3 my-3">
      <h3>{title}</h3>
      <p>{message}</p>
    </div>
  );
}