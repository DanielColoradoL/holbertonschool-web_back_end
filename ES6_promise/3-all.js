import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then((out) => {
      console.log(`${out[0].body} ${out[1].firstName} ${out[1].lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}
