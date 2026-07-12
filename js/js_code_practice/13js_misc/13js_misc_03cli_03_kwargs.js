const args = {};

for (const arg of process.argv.slice(2)) {
  const [key, value] = arg.replace(/^--/, "").split("=");
  args[key] = value;
}

//node scriptName.js --name=Alice --age=25

console.log("All args are: ");
console.log(args);
console.log("Name is: " + args.name);
console.log("Age is: " + args.age);
console.log("Id is: " + args.id);
