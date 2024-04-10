// import React, { useState } from "react";

// interface DataInput {
//   inputLabel: string;
//   placeholder: string;
//   type: 'date' | 'text';
//   regex?: string;
// }

// type Setters = {
//     [key: string]: React.Dispatch<React.SetStateAction<string>>;
//   };

// interface DataCardProps {
//   dataSets: DataInput[][];
//   setters: Setters;
// }

// const DataCard: React.FC<DataCardProps> = ({ dataSets, setters }) => {
//   const [currentSetIndex, setCurrentSetIndex] = useState(0);

//   const handleInputChange = (label: string, value: string) => {
//     const setterFunction = setters[label];
//     if (setterFunction) {
//       setterFunction(value);
//     }
//   };

//   const nextSet = () => setCurrentSetIndex((prevIndex) => (prevIndex + 1) % dataSets.length);
//   const prevSet = () => setCurrentSetIndex((prevIndex) => (prevIndex - 1 + dataSets.length) % dataSets.length);

//   return (
//     <div className="childData-card">
//       {dataSets[currentSetIndex].map((data, index) => (
//         <div className="childData-input" key={index}>
//           <h3>{data.inputLabel}</h3>
//           <input 
//             type={data.type} 
//             placeholder={data.placeholder} 
//             onChange={(e) => handleInputChange(data.inputLabel, e.target.value)}
//           />
//         </div>
//       ))}
//       <button onClick={prevSet} type="button">Poprzedni zestaw</button>
//       <button onClick={nextSet} type="button">Następny zestaw</button>
//     </div>
//   );
// };

// export default DataCard;


import React, { useState } from "react";

interface DataInput {
  inputLabel: string;
  placeholder: string;
  type: 'date' | 'text';
  regex?: string;
}

interface DataCardProps {
  dataSets: DataInput[][];
  formData: { [key: string]: string };
  handleInputChange: (name: string, value: string) => void; 
}

const DataCard: React.FC<DataCardProps> = ({ dataSets, formData, handleInputChange }) => {
  const [currentSetIndex, setCurrentSetIndex] = useState(0);

  const nextSet = () => setCurrentSetIndex((prevIndex) => (prevIndex + 1) % dataSets.length);
  const prevSet = () => setCurrentSetIndex((prevIndex) => (prevIndex - 1 + dataSets.length) % dataSets.length);

  return (
    <div className="childData-card">
      {dataSets[currentSetIndex].map((data, index) => {
        const inputName = data.inputLabel.replace(/\s+/g, '');
        return (
          <div className="childData-input" key={index}>
            <h3>{data.inputLabel}</h3>
            <input 
              type={data.type}
              name={inputName}
              value={formData[inputName] || ""} 
              onChange={(e) => handleInputChange(inputName, e.target.value)}
              placeholder={data.placeholder}
            />
          </div>
        );
      })}
      <button onClick={prevSet} type="button">Poprzedni zestaw</button>
      <button onClick={nextSet} type="button">Następny zestaw</button>
    </div>
  );
};

export default DataCard;