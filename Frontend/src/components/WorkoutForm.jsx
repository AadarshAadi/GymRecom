import { useState } from "react";

function WorkoutForm({ onSubmit }) {
    const [formData, setFormData] = useState({
        workout_type: "Strength",
        days: 5,
        age: 22,
        duration: 60,
        experience_level: "Intermediate",
        available_equipment: [
            "Dumbbell",
            "Machine"
        ],
        injury: "None"
    });

    const handleChange = (e) => {
        const { name, value } = e.target;

        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleEquipmentChange = (e) => {
        const { value, checked } = e.target;

        let updatedEquipment;

        if (checked) {
            updatedEquipment = [
                ...formData.available_equipment,
                value
            ];
        } else {
            updatedEquipment =
                formData.available_equipment.filter(
                    (item) => item !== value
                );
        }

        setFormData({
            ...formData,
            available_equipment: updatedEquipment
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <form onSubmit={handleSubmit}>

            <h2>Workout Details</h2>

            <label>Workout Goal</label>

            <select
                name="workout_type"
                value={formData.workout_type}
                onChange={handleChange}
            >
                <option>Strength</option>
                <option>Hypertrophy</option>
            </select>

            <label>Days Per Week</label>

            <input
                type="number"
                name="days"
                min="2"
                max="6"
                value={formData.days}
                onChange={handleChange}
            />

            <label>Workout Duration (minutes)</label>

            <input
                type="number"
                name="duration"
                value={formData.duration}
                onChange={handleChange}
            />

            <label>Age</label>

            <input
                type="number"
                name="age"
                value={formData.age}
                onChange={handleChange}
            />

            <label>Experience</label>

            <select
                name="experience_level"
                value={formData.experience_level}
                onChange={handleChange}
            >
                <option>Beginner</option>
                <option>Intermediate</option>
                <option>Advanced</option>
            </select>

            <label>Available Equipment</label>

            {[
                "Dumbbell",
                "Machine",
                "Cable",
                "Body Only"
            ].map((equipment) => (
                <div key={equipment}>
                    <input
                        type="checkbox"
                        value={equipment}
                        checked={formData.available_equipment.includes(
                            equipment
                        )}
                        onChange={handleEquipmentChange}
                    />
                    {equipment}
                </div>
            ))}

            <label>Injury</label>

            <select
                name="injury"
                value={formData.injury}
                onChange={handleChange}
            >
                <option>None</option>
                <option>Knee Pain</option>
                <option>Lower Back Pain</option>
                <option>Shoulder Pain</option>
            </select>

            <button type="submit">
                Generate Workout
            </button>

        </form>
    );
}

export default WorkoutForm;