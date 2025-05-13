import React from 'react';
import FileUploader from './components/FileUploader';

function App() {
  return (
    <div className="max-w-3xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">📊 DataFabricX – Upload & Parse</h1>
      <FileUploader />
    </div>
  );
}

export default App;
