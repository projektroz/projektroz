import { useEffect, useState } from "react";
import { api } from "../api/axios";
import Child from "../types/Child";

export function useChildData(fosterCarerId: number) {
    const [childData, setChildData] = useState<Child[]>([]);

    useEffect(() => {
        api.get("/children/").then((response) => {
            const children = response.data.filter(
                (child: Child) => child.foster_carer === fosterCarerId
            );
            // const children = response.data;
            console.log("dziecko benc", children);
            console.log("Fetched children:", children); // Log the fetched data
            setChildData(children);
        });

        return () => {
            console.log("Component is unmounting");
        };
    }, [fosterCarerId]);

    return childData;
}
