export default function setFromArray(array) {
  const outputSet = new Set();
  for (const item of array) {
    outputSet.add(item);
  }
  return outputSet;
}
