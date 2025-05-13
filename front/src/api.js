import axios from 'axios';

const API_BASE = 'https://your-backend-url.up.railway.app'; // <-- replace with your backend

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  const res = await axios.post(`${API_BASE}/upload`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });

  return res.data;
};
