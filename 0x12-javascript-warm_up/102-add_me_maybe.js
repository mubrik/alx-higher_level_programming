#!/usr/bin/node

export function addMeMaybe (num, func) {
  let index = 0;
  while (index < num) {
    func();
    index++;
  }
}

module.exports = {
  addMeMaybe
};
