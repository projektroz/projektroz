import React, { useState } from "react";

// Define the props for the input data and the card component
interface DataInput {
  inputLabel: string;
  placeholder: string;
  type: 'date' | 'text';
  regex?: string;
}

interface DataCardProps {
  dataSets: DataInput[][];
  setters: React.Dispatch<React.SetStateAction<string>>[];
}

// DataCard component with integrated input fields
const DataCard: React.FC<DataCardProps> = ({ dataSets, setters }) => {
  const [currentSetIndex, setCurrentSetIndex] = useState(0);

  const nextSet = () => setCurrentSetIndex((prevIndex) => (prevIndex + 1) % dataSets.length);
  const prevSet = () => setCurrentSetIndex((prevIndex) => (prevIndex - 1 + dataSets.length) % dataSets.length);

  return (
    <div className="childData-card">
      {dataSets[currentSetIndex].map((data, index) => (
        <div className="childData-input" key={index}>
          <h3>{data.inputLabel}</h3>
          <input 
            type={data.type} 
            placeholder={data.placeholder} 
          />
        </div>
      ))}
      <button onClick={prevSet} type="button">Poprzedni zestaw</button>
      <button onClick={nextSet} type="button">Następny zestaw</button>
    </div>
  );
};

export default DataCard;