// import React, { useState } from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
import ChildDataCard from "../../components/ChildDataCard/ChildDataCard";
// import { addChild, addFather, addMother } from "../../api/addChild";
// import { getChildData } from '../../functions/AddChildFunctions';
import {useChildData} from "../../components/ChildData/ChildData";
import "./ManageChild.scss";
import Child from "types/Child";


function ManageChild() {
    const links = [
        {
            name: "Strona główna",
            url: "/home",
            icon: "../src/assets/icons/home.png",
        },
        {
            name: "Panel sterowania",
            url: "/dashboard",
            icon: "../src/assets/icons/manage.png",
        },
        { name: "Wyloguj", url: "/logout", icon: "../src/assets/icons/logout.png" },
    ];

    const fosterCarerId = 1;
    const children = useChildData(fosterCarerId);

    return (
        <div className="app-page manage-child-page">
            <Rectangle links={links}>
                <div className='manageChild'>
                    {children.map((child: Child, index: number) => (
                        <ChildDataCard key = {index} childData = {child} />
                    ))}
                </div>
            </Rectangle>
        </div>
    );
} 
export default ManageChild;