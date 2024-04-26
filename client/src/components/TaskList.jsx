import { useEffect, useState } from "react";
import { getAllTasks } from '../api/tasks.api';
import { TaskCard } from '../components/TaskCard';

export function TaskList() {
    const [tasks, setTasks] = useState([])

    useEffect(() => {
        async function loadTasks() {
            const res = await getAllTasks();
            setTasks(res.data);
            console.log(res);
        }
        loadTasks();
    }, []);

    return (<div className="grid grid-cols-3 gap-3">
        {tasks.map(task => (
            <TaskCard key={task.id} task={task} />
        ))}
    </div >);

    // useEffect(() => { console.log('Page loaded') }, []);
    // return (
    //     <div>
    //         TaskList
    //     </div>
    // )
}

