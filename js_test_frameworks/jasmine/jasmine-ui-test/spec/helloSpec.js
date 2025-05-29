const { JSDOM } = require("jsdom");
console.log("✅ Loaded spec file helloSpec!");
describe("UI Interaction", function () {
  let window, document;

  beforeEach(function () {
    const dom = new JSDOM(`
      <h1 id="title">Welcome</h1>
      <button id="myBtn">Click me</button>
    `);

    window = dom.window;
    document = dom.window.document;

    // Optionally expose globally if needed
    global.window = window;
    global.document = document;

    // JS logic
    window.changeTitle = function () {
      document.getElementById("title").textContent = "Title Changed!";
    };

    document.getElementById("myBtn").addEventListener("click", window.changeTitle);
  });

  it("should change the title text on button click", function () {
    document.getElementById("myBtn").click();
    expect(document.getElementById("title").textContent).toBe("Title Changed!");
  });
});