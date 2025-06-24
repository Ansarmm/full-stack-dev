import { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="p-2 flex flex-col gap-4">
      <h1 className="text-3xl font-semibold">Счетчик: </h1>
      <div className="flex flex-row gap-4">
        <p className="font-semibold">Текущий счет: {count}</p>
        <button className ="shadow-md w-64 p-2 bg-green-500 text-white font-bold rounded-lg" onClick={() => setCount(count + 1)}>Увеличить</button>
      </div>
    </div>
  );
}

export default App;