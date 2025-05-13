import React from 'react';

const TablePreview = ({ data }) => {
  const { columns, preview } = data;
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full table-auto border">
        <thead>
          <tr className="bg-gray-200">
            {columns.map((col, idx) => (
              <th key={idx} className="px-4 py-2 border">{col}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {preview.map((row, i) => (
            <tr key={i} className="hover:bg-gray-100">
              {columns.map((col) => (
                <td key={col} className="px-4 py-2 border">{row[col]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TablePreview;
