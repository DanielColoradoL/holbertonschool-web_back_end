export default function getListStudents() {
  const output = [];
  output.push({ id: 1, firstName: 'Guillaume', location: 'San Francisco' });
  output.push({ id: 2, firstName: 'James', location: 'Columbia' });
  output.push({ id: 5, firstName: 'Serena', location: 'San Francisco' });
  return output;
}
