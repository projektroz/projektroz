import { useEffect, useState } from 'react';
import { api } from "../../api/axios";
import Child from "../../types/Child";

// Custom hook to fetch child data
export function useChildData(fosterCarerId: number) {
    const [childData, setChildData] = useState<Child[]>([]);

    useEffect(() => {
        api.get('/children').then((response) => {
            setChildData(response.data.filter((child: Child) => child.foster_carer === fosterCarerId));
        });

        return () => {
            console.log('Component is unmounting');
        };
    }, [fosterCarerId]);

    return childData;
}
