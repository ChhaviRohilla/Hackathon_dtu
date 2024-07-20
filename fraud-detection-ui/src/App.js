// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

//---2md---

// import React, { useState } from 'react';
// import axios from 'axios';
// import './App.css';

// function App() {
//   const [transactions, setTransactions] = useState([]);
//   const [alerts, setAlerts] = useState([]);

//   const fetchPredictions = async () => {
//     try {
//       const response = await axios.post('http://localhost:5000/predict', transactions);
//       const data = response.data;

//       const newAlerts = transactions.map((txn, index) => ({
//         ...txn,
//         fraudProbability: data.probabilities[index],
//         isFraud: data.predictions[index]
//       }));

//       setAlerts(newAlerts);
//     } catch (error) {
//       console.error("Error fetching predictions", error);
//     }
//   };

//   const handleTransactionChange = (index, event) => {
//     const { name, value } = event.target;
//     const newTransactions = [...transactions];
//     newTransactions[index][name] = value;
//     setTransactions(newTransactions);
//   };

//   const addTransaction = () => {
//     setTransactions([...transactions, { transaction_id: '', amount: '', transaction_time: '', user_id: '', merchant_id: '' }]);
//   };

//   return (
//     <div className="App">
//       <h1>Transaction Monitoring System</h1>
//       <button onClick={addTransaction}>Add Transaction</button>
//       <button onClick={fetchPredictions}>Check for Fraud</button>
//       <table>
//         <thead>
//           <tr>
//             <th>Transaction ID</th>
//             <th>Amount</th>
//             <th>Time</th>
//             <th>User ID</th>
//             <th>Merchant ID</th>
//             <th>Fraud Probability</th>
//             <th>Is Fraud</th>
//           </tr>
//         </thead>
//         <tbody>
//           {transactions.map((txn, index) => (
//             <tr key={index}>
//               <td><input type="text" name="transaction_id" value={txn.transaction_id} onChange={e => handleTransactionChange(index, e)} /></td>
//               <td><input type="number" name="amount" value={txn.amount} onChange={e => handleTransactionChange(index, e)} /></td>
//               <td><input type="text" name="transaction_time" value={txn.transaction_time} onChange={e => handleTransactionChange(index, e)} /></td>
//               <td><input type="number" name="user_id" value={txn.user_id} onChange={e => handleTransactionChange(index, e)} /></td>
//               <td><input type="number" name="merchant_id" value={txn.merchant_id} onChange={e => handleTransactionChange(index, e)} /></td>
//               <td>{txn.fraudProbability ? txn.fraudProbability.toFixed(2) : ''}</td>
//               <td>{txn.isFraud !== undefined ? (txn.isFraud ? 'Yes' : 'No') : ''}</td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// }

// export default App;


import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [transactions, setTransactions] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    // Fetch transactions from the backend
    const fetchTransactions = async () => {
      try {
        const response = await axios.get('http://localhost:5000/transactions');
        setTransactions(response.data);
      } catch (error) {
        console.error("Error fetching transactions", error);
      }
    };
    fetchTransactions();
  }, []);

  const fetchPredictions = async () => {
    try {
      const response = await axios.post('http://localhost:5000/predict', transactions);
      const data = response.data;

      const newAlerts = transactions.map((txn, index) => ({
        ...txn,
        fraudProbability: data.probabilities[index],
        isFraud: data.predictions[index]
      }));

      setAlerts(newAlerts);
    } catch (error) {
      console.error("Error fetching predictions", error);
    }
  };

  return (
    <div className="App">
      <h1>Transaction Monitoring System</h1>
      <button onClick={fetchPredictions}>Check for Fraud</button>
      <table>
        <thead>
          <tr>
            <th>Transaction ID</th>
            <th>Amount</th>
            <th>Time</th>
            <th>Fraud Probability</th>
            <th>Is Fraud</th>
          </tr>
        </thead>
        <tbody>
          {alerts.length > 0 ? (
            alerts.map((alert, index) => (
              <tr key={index}>
                <td>{alert.transaction_id}</td>
                <td>{alert.amount}</td>
                <td>{alert.transaction_time}</td>
                <td>{alert.fraudProbability.toFixed(2)}</td>
                <td>{alert.isFraud ? 'Yes' : 'No'}</td>
              </tr>
            ))
          ) : (
            transactions.map((txn, index) => (
              <tr key={index}>
                <td>{txn.transaction_id}</td>
                <td>{txn.amount}</td>
                <td>{txn.transaction_time}</td>
                <td>N/A</td>
                <td>N/A</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;
