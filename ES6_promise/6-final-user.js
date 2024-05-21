import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName)
    .then((value) => ({
      status: 'fulfilled',
      value,
    }))
    .catch((err) => ({
      status: 'rejected',
      value: err.toString(),
    }));

  const photoPromise = uploadPhoto(fileName)
    .then((value) => ({
      status: 'fulfilled',
      value,
    }))
    .catch((err) => ({
      status: 'rejected',
      value: err.toString(),
    }));

  return Promise.all([userPromise, photoPromise]);
}
