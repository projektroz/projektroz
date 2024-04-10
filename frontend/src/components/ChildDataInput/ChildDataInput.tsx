import React from "react";

interface DataInputProps {
    inputLabel: string;
    placeholder: string;
    type: 'date' | 'text';
    regex?: string;
}

const ChildDataInput: React.FC<DataInputProps> = ({ inputLabel, placeholder, type }) => {
    return (
        <div className="childData-input">
            <h3>{inputLabel}</h3>
            <input 
                type={type} 
                placeholder={placeholder} 
            />
        </div>
    );
};

export default ChildDataInput;