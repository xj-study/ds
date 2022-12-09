(function (factory) {
  typeof define === 'function' && define.amd ? define(factory) :
  factory();
})((function () { 'use strict';

  function add(a, b) {
    return a + b;
  }

  console.log("hello rollup");

  console.log("add", add(10, 20));

}));
