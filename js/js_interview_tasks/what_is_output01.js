const assert = require("node:assert");
function get_console_log(comment = "Initial log") {
  console.log(comment);
  console.log(obj1);
  console.log(obj2);
  console.log(obj3);
}

const obj1 = { a: 1, b: { c: 2 } };
const obj2 = { ...obj1 }; // shallow copy
const obj3 = obj1; // same object/reference
/*
obj1 and obj3 point to the same object
obj2 is a new object
but obj2.b points to the same nested object as obj1.b

obj1 ──► Object A
          ├── a: 1
          └── b ──► Object B
                     └── c: 2

obj2 ──► Object C
          ├── a: 1
          └── b ─────────────► Object B
*/

get_console_log();

obj2.a = 10;

get_console_log("after changing obj2.a");
obj2.b.c = 20;
get_console_log("after changing obj2.b.c");
obj3.b.c = 30;
get_console_log("after changing obj3.b.c");

assert(obj1.a === 1);
