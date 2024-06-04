import Rectangle from "../../components/Rectangle/Rectangle";
import { useChildData } from "../../hooks/useChildData";
import "./ManageChild.scss";
import ChildTable from "../../components/ChildTable/ChildTable";

function ManageChild() {
    const links = [
        {
            name: "Panel sterowania",
            url: "/dashboard",
            icon: "../src/assets/icons/manage.png",
        },
        {
            name: "Wyloguj",
            url: "/logout",
            icon: "../src/assets/icons/logout.png",
        },
    ];

    const fosterCarerId = 1;
    const children = useChildData(fosterCarerId);

    return (
        <div className="app-page manage-child-page">
            <Rectangle links={links}>
                <div className="manageChild" style={{ width: "80%" }}>
                    <ChildTable children={children} />
                </div>
            </Rectangle>
        </div>
    );
}

export default ManageChild;
