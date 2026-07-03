import { useState } from "react";

import WorkoutForm from "./components/WorkoutForm";
import WorkoutResults from "./components/WorkoutResults";

import api from "./services/api";

function App() {

    const [result, setResult] = useState(null);

    const generateWorkout = async (formData) => {

        try {

            const response = await api.post(
                "/recommend",
                formData
            );

            setResult(response.data);

        }

        catch (error) {

            console.error(error);

        }

    };

    return (

        <div className="container">

            <h1>Workout Recommendation System</h1>

            <WorkoutForm
                onSubmit={generateWorkout}
            />

            <WorkoutResults
                result={result}
            />

        </div>

    );

}

export default App;