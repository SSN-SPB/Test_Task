const compose = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args)),
  );
const pipe = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args)),
  );

const half = (x) => x / 2;
const triple = (x) => x * 3;
const plusTen = (x) => x + 10;

const transform_compose = compose(half, triple, plusTen);
const transform_pipe = pipe(half, triple, plusTen);

console.log(transform_compose(2));
console.log(transform_pipe(2));
