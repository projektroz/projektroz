import Child from "../../types/Child";

export interface Props {
    key: number;
    childData: Child;
}

const ChildDataCard: React.FC<Props> = ({ childData }) => {
    return (
        <div>
            <img src="../../assets/icons/add.png" />
            <p>{childData.name}</p>
        </div>
    );
}

export default ChildDataCard;