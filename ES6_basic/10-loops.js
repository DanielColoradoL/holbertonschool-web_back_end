export default function appendToEachArrayValue(array, appendString) {
  const output = [];
  for (const str of array) {
    output.push(appendString + str);
  }
  return output;
}
