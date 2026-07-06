import { useState } from "react";
import Select from "react-select";
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
    setFormData({ ...formData, [name]: value });
  };
  const submitfo = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className="form-card">
      <form onSubmit={submitfo}>
        <h2>Workout Restrictions</h2>

        <label>Workout Goal</label>
        <select name="workcat" value={formData.workcat} onChange={hanchang}>
          <option>Strength</option>
          <option>Hypertrophy</option>
        </select>

        <label>Days Per Week</label>
        <input type="number" name="days" min="2" max="6" value={formData.days} onChange={hanchang} />

        <label>Workout Duration (minutes)</label>
        <input type="number" name="duration" value={formData.duration} onChange={hanchang} />

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