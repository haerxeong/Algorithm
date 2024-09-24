let [A, B] = require("fs").readFileSync(0, "utf-8").split("\n");
A = Number(A);
B = Number(B);
console.log(A + B);
