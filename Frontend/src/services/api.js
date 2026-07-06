import axios from "axios";
/**
 * Axios communication with the backend API.
 */
const api = axios.create({
    baseURL: "http://localhost:8000"
});
export default api;