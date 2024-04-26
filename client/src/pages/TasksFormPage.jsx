import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { createTask, deleteTask, updateTask, getTask } from "../api/tasks.api"
import { useNavigate, useParams } from "react-router-dom";
import { toast } from 'react-hot-toast'
export function TasksFormPage() {

    const { register, handleSubmit, formState: { errors }, setValue } = useForm();
    const navigate = useNavigate();
    const params = useParams();
    //console.log(params)
    const onSubmit = handleSubmit(async data => {
        if (params.id) {
            console.log("updating");
            console.log(data);

            await updateTask(params.id, data)
            toast.success('Updated Task', {
                position: "bottom-right",
                style: {
                    background: "#101010",
                    color: "#fff"

                }
            })
        } else {
            await createTask(data);
            toast.success('Created Task', {
                position: "bottom-right",
                style: {
                    background: "#101010",
                    color: "#fff"

                }
            })
        }
        navigate("/tasks");
        // console.log(res)
    })
    useEffect(() => {
        async function loadTask() {
            if (params.id) {
                // console.log("getting data")
                const { data: { title, description } } = await getTask(params.id)
                // console.log({ title, description })
                setValue('title', title)
                setValue('description', description)
            }
        }
        loadTask();
    }, [])
    return (
        //yup
        //sop
        <div className="max-w-xl mx-auto">
            <form onSubmit={onSubmit}>
                <input
                    type="text"
                    placeholder="title"
                    {...register("title", { required: true })} className="bg-zinc-700 p-3 rounded-lg block w-full mb3"
                />
                {errors.title && <spam>title is required </spam>}
                <textarea
                    rows="3"
                    placeholder="Description"
                    {...register("description", { required: true })} className="bg-zinc-700 p-3 rounded-lg block w-full mb3"
                ></textarea>
                {errors.description && <spam>description is required </spam>}
                <button className="bg-indigo-500 p-3 rounded-lg w-full mt-3">Save</button>
            </form>
            {
                params.id && <div className="flex justify-end"><button
                    className="bg-red-500 p-3 rounded-lg w-48 mt-3"
                    onClick={async () => {
                        const accepted = window.confirm('are you sure?')
                        if (accepted) {
                            await deleteTask(params.id);
                            navigate("/tasks");
                            toast.success('Deleted Task', {
                                position: "bottom-right",
                                style: {
                                    background: "#101010",
                                    color: "#fff"

                                }
                            })
                        }

                    }}>
                    Delete
                </button></div>


            }
        </div>
    );
}
