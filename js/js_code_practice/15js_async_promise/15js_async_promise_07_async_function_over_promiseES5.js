function fetchPerson() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ id: 1, name: "Tom" });
    }, 3000);
  });
}

async function main() {
  try {
    const user = await fetchPerson();
    console.log(user);
    console.log(`Hello, ${user.name}`);
  } catch {
    console.log(error);
  }
}

main();

console.log("Start programm");
