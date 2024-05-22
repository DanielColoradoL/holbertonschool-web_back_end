export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  const stringLength = startString.length;
  let outputString = '';
  for (const value of set) {
    if (value.startsWith(startString) && startString) {
      if (outputString !== '') {
        outputString += '-';
      }
      outputString += value.slice(stringLength);
    }
  }
  return outputString;
}
