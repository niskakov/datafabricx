import React, { useState } from 'react';
import { uploadFile } from '../api';
import TablePreview from './TablePreview';

const FileUploader = () => {
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setLoading(true);
    try {
      const result = await uploadFile(file);
      setPreview(result);
    } catch (err) {
      alert("Upload failed");
    }
    setLoading(false);
  };

  return (
    <div className="space-y-4">
      <input
        type="file"
        onChange={handleUpload}
        accept=".csv,.xlsx,.xls,.pdf"
        className="block w-full text-sm text-gray-700 file:bg-blue-600 file:text-white file:py-2 file:px-4"
      />
      {loading && <p>Loading...</p>}
      {preview && <TablePreview data={preview} />}
    </div>
  );
};

export default FileUploader;
