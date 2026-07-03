function WorkoutResults({ result }) {
    if (!result) return null;
    return (
        <div className="results">
            <div className="summary">

                <h2>Workout Recommendation</h2>

                <p>
                    <strong>Recommended Split:</strong>
                    {" "}
                    {result.split}
                </p>

                <p>
                    <strong>Exercises Per Day:</strong>
                    {" "}
                    {result.exercise_count}
                </p>

                <p>
                    <strong>Age Recommendation:</strong>
                    {" "}
                    {result.age_note}
                </p>

            </div>

            <hr />

            {Object.entries(result.weekly_plan).map(([day, plan]) => (

                <div
                    key={day}
                    className="day-card"
                >

                    <h3>{day}</h3>

                    {plan === "Rest" ? (

                        <p className="rest-day">
                            💤 Rest Day
                        </p>

                    ) : (

                        plan.map((exercise, index) => (

                            <div
                                key={index}
                                className="exercise-card"
                            >

                                <h4>
                                    {exercise.Exercise}
                                </h4>

                                <p>
                                    Muscle:
                                    {" "}
                                    {exercise.Muscle}
                                </p>

                                <p>
                                    Equipment:
                                    {" "}
                                    {exercise.Equipment}
                                </p>

                                <p>
                                    Level:
                                    {" "}
                                    {exercise.Level}
                                </p>

                                <p>
                                    {exercise.Sets} Sets
                                    {" • "}
                                    {exercise.Reps} Reps
                                </p>

                                <p>
                                    Rest:
                                    {" "}
                                    {exercise.Rest}
                                </p>

                            </div>

                        ))

                    )}

                </div>

            ))}

        </div>

    );

}

export default WorkoutResults;