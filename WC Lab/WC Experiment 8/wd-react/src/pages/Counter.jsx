import React, { useState, useEffect } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);

  function adjustCount(amount) {
    setCount((prev) => prev + amount);
  }

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="flex flex-col gap-8">
        <h1 className="text-5xl font-bold text-center">{count}</h1>
        <div className="flex gap-5">
          <button
            onClick={() => adjustCount(1)}
            className="h-16 w-32 bg-green-500 hover:bg-green-600 text-white px-5 py-2 rounded-md"
          >
            Add
          </button>
          <button
            onClick={() => adjustCount(-1)}
            className="h-16 w-32 bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded-md"
          >
            Subtract
          </button>
        </div>
      </div>
    </div>
  );
};

export default Counter;
