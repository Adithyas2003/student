import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [students, setStudents] = useState([]);
  const [newStudent, setNewStudent] = useState({
    name: '',
    age: '',
    classes: '',
  });
  const [error, setError] = useState('');
  const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/std/';

  useEffect(() => {
    axios.get(apiUrl)
      .then(response => {
        setStudents(response.data);
      })
      .catch(error => {
        setError("There was an error fetching the students!");
        console.error(error);
      });
  }, [apiUrl]);

  const handleInputChange = (e) => {
    setNewStudent({
      ...newStudent,
      [e.target.name]: e.target.value,
    });
  };

  const handleAddStudent = (e) => {
    e.preventDefault();
    
    const studentData = {
      ...newStudent,
      age: Number(newStudent.age), 
    };

    axios.post(apiUrl, studentData)
      .then(response => {
        setStudents([...students, response.data]);
        setNewStudent({
          name: '',
          age: '',
          classes: '',
        });
      })
      .catch(error => {
        setError("There was an error adding the student!");
        console.error(error);
      });
  };

  return (
    <div className="App">
      <h1>Student Management System</h1>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      <form onSubmit={handleAddStudent}>
        <input
          type="text"
          name="name"
          value={newStudent.name}
          onChange={handleInputChange}
          placeholder="Name"
          required
        />
        <input
          type="number"
          name="age"
          value={newStudent.age}
          onChange={handleInputChange}
          placeholder="Age"
          required
          min="1" 
        />
        <input
          type="number"
          name="classes"
          value={newStudent.classes}
          onChange={handleInputChange}
          placeholder="Classes"
          required
        />
       
        <button type="submit">Add Student</button>
      </form>

      <h2>Student List</h2>
      <ul>
        {students.map(student => (
          <li key={student.id}>
            {student.name} {student.age} - {student.classes} 
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

