import Child from "../../types/Child";
import DashboardLine from "../DashboardLine/DashboardLine";

import "./ChildDataCard.scss";

export interface Props {
    key: number;
    childData: Child;
}

const ChildDataCard: React.FC<Props> = ({ childData }) => {
    
    const cards = [
        {
            title: `${childData.name}`  + "\u00A0" + `${childData.surname}\n ${childData.birth_date === null ? "" : childData.birth_date.toString()}`,
            url: "",
            image: "../src/assets/icons/user.png",
        },
        {
            title: "Edytuj dziecko",
            url: "/dashboard/manage-child/edit-child",
            image: "../src/assets/icons/manage.png",
            childData: childData,
        },
        // {
        //     title: "Zarządzaj dziećmi",
        //     url: "/dashboard/manage-child",
        //     image: "../src/assets/icons/add.png",
        // },
        // {
        //     title: "dziecko za okno",
        //     url: "/dashboard/manage-child",
        //     image: "../src/assets/icons/manage.png",
        // },
    ];

    return (

        <div className="content-row">
            <DashboardLine title="" cards={cards} />
        </div>
    );
}

export default ChildDataCard;