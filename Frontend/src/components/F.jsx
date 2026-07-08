import { useState } from "react";
import Select from "react-select";
/**
 * Renders a form for collecting workout preferences and restrictions.
 *
 * Allows the user to specify:
 * - Workout goal
 * - Days per week
 * - Workout duration
 * - Age
 * - Experience level
 * - Available equipment
 * - Injury status
 *
 * On submission, the collected form data is passed to the parent component
 * through the `onSubmit` callback.
 */
function F({ onSubmit }) {
  const [formData, setFormData] = useState({
    workcat: "Strength",
    days: 5,
    age: 22,
    duration: 60,
    exper: "Beginner",
    equipm: ["Dumbbell", "Machine"],
    injury: "None"
  });
  const equipmentOptions = [
  { value: "Dumbbell", label: "Dumbbell" },
  { value: "Machine", label: "Machine" },
  { value: "Cable", label: "Cable" },
  { value: "Body Only", label: "Body Only" },
  ];
  const hanchang = (e) => {
    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: name === "days" ? Number(value) : value,
    });
  };
  const submitfo = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className="form-card">
      <form onSubmit={submitfo}>
        <h2>Workout Preferences</h2>
        <label>Workout Goal</label>
        <select name="workcat" value={formData.workcat} onChange={hanchang}>
          <option>Strength</option>
          <option>Hypertrophy</option>
        </select>
        <label>Days Per Week</label>
        <select name="days" value={formData.days} onChange={hanchang}>
          <option value={2}>2</option>
          <option value={3}>3</option>
          <option value={4}>4</option>
          <option value={5}>5</option>
          <option value={6}>6</option>
        </select>
        <label>Workout Duration (minutes)</label>
        <input type="number" name="duration" min="30" max="240" value={formData.duration} onChange={hanchang} />
        <label>Age</label>
        <input type="number" name="age" value={formData.age} onChange={hanchang} />
        <label>Experience</label>
        <select name="exper" value={formData.exper} onChange={hanchang}>
          <option>Beginner</option>
          <option>Intermediate</option>
          <option>Advanced</option>
        </select>
        <label>Available Equipment</label>
        <Select
          isMulti
          options={equipmentOptions}
          placeholder="Select equipment..."
          value={equipmentOptions.filter(option =>
            formData.equipm.includes(option.value)
          )}
          onChange={(selected) =>
            setFormData({
              ...formData,
              equipm: selected ? selected.map(item => item.value) : [],
            })
          }
          styles={{
            control: (base) => ({
              ...base,
              minHeight: "50px",
              borderRadius: "12px",
              borderColor: "#d1d5db",
              boxShadow: "none",
              "&:hover": {
                borderColor: "#6366f1",
              },
            }),
            multiValue: (base) => ({
              ...base,
              backgroundColor: "#6366f1",
              borderRadius: "8px",
            }),
            multiValueLabel: (base) => ({
              ...base,
              color: "white",
              fontWeight: 500,
            }),
            multiValueRemove: (base) => ({
              ...base,
              color: "white",
              ":hover": {
                backgroundColor: "#4f46e5",
                color: "white",
              },
            }),
            option: (base, state) => ({
              ...base,
              backgroundColor: state.isFocused ? "#eef2ff" : "white",
              color: "#111827",
              cursor: "pointer",
            }),
          }}
        />
        <label>Injury</label>
        <select name="injury" value={formData.injury} onChange={hanchang}>
          <option>None</option>
          <option>Knee Pain</option>
          <option>Lower Back Pain</option>
          <option>Shoulder Pain</option>
        </select>
        <button type="submit">Generate Workout</button>
      </form>
    </div>
  );
}

export default F;