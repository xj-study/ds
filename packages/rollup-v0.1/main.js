import { add } from "./demo1";
console.log("hello rollup");

export default {
  say: function () {
    console.log("add", add(10, 20));
  },
};
