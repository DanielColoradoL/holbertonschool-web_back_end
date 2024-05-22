export default function updateUniqueItems(inMap) {
  if (!(inMap instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const [key, value] of inMap) {
    if (value === 1) {
      inMap.set(key, 100);
    }
  }
  return inMap;
}
