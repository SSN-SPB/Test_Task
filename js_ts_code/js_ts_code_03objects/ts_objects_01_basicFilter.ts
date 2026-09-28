interface User {
  name: string;
  age: number;
}

const users: Users[] = [
  { name: "Tom", age: 29 },
  { name: "Colin", age: 39 },
  { name: "Tim", age: 11 },
];

function selectAdults(users: Users[]): Users[] {
  return users.filter((user) => user.age >= 18);
}

console.log(selectAdults(users));
