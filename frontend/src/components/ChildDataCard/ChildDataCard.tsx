import React, { useState } from "react";
import ChildDataInput from "../ChildDataInput/ChildDataInput";

interface DataInput {
  inputLabel: string;
  placeholder: string;
  type: 'date' | 'text';
  regex?: string;
}

interface Props {
  dataSets: DataInput[][];
}

const ChildDataCard: React.FC<Props> = ({ dataSets }) => {
  const [currentSetIndex, setCurrentSetIndex] = useState(0);

  const nextSet = () => setCurrentSetIndex((prevIndex) => (prevIndex + 1) % dataSets.length);
  const prevSet = () => setCurrentSetIndex((prevIndex) => (prevIndex - 1 + dataSets.length) % dataSets.length);

  return (
    <div className="childData-card">
      {dataSets[currentSetIndex].map((data, index) => (
        <ChildDataInput
          key={index}
          inputLabel={data.inputLabel}
          placeholder={data.placeholder}
          type={data.type}
          regex={data.regex} 
        />
      ))}
      <button onClick={prevSet} type="button">Poprzedni zestaw</button>
      <button onClick={nextSet} type="button">Następny zestaw</button>
    </div>
  );
};

export default ChildDataCard;