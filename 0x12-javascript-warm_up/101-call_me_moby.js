#!/usr/bin/node

function callMeMoby (num, func) {
  let index = 0;
  while (index < num) {
    func();
    index++;
  }
}

module.exports = {
  callMeMoby
};
