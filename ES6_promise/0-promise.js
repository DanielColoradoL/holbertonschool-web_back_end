export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const success = true;
    if (success) {
      resolve("Success - API");
    } else {
      reject(new Error('Fail - API'));
    }
  });
}
