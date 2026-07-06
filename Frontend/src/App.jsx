import { useState } from "react";
import F from "./components/F";
import R from "./components/R";
import api from "./services/api";
function App() {
    const [result, setResult] = useState(null);
    const genwork = async (formData) => {
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
        <div className={`main-card ${result ? "results-mode" : "form-mode"}`}>
    <h1>GYMY</h1>
    {!result ? (
        <F onSubmit={genwork}/>
    ) : (
        <R result={result} onBack={goBack}/>
    )}
        </div>
    </div>
);
}
export default App;