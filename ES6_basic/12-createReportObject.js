export default function createReportObject(employeesList) {
  function getNumberOfDepartments() {
    return Object.keys(employeesList).length;
  }
  return {
    allEmployees: employeesList,
    getNumberOfDepartments,
  };
}
