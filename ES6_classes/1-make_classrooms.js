import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const output = [];
  for (const i of [19, 20, 34]) {
    output.push(new ClassRoom(i));
  }
  return output;
}
