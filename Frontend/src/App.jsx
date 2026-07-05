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
    const goBack = () => {

    setResult(null);

};

return (
    <div className="app-background">

        <div
    className={`main-card ${result ? "results-mode" : "form-mode"}`}
>

<h1>Workout Recommendation System</h1>

{!result ? (

    <WorkoutForm
        onSubmit={generateWorkout}
    />

) : (

    <WorkoutResults
        result={result}
        onBack={goBack}
    />

)}

        </div>

    </div>
);

}

export default App;