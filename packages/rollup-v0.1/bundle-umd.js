(function (global, factory) {
  typeof exports === "object" && typeof module !== "undefined"
    ? (module.exports = factory())
    : typeof define === "function" && define.amd
    ? define(factory)
    : ((global = typeof globalThis !== "undefined" ? globalThis : global || self), (global.myBundle = factory()));
})(this, function () {
  "use strict";

  function add(a, b) {
    return a + b;
  }

  console.log("hello rollup");

  var main = {
    say: function () {
      console.log("add", add(10, 20));
    },
  };

  return main;
});
