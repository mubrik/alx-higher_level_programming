#!/usr/bin/node

export function callMeMoby (num, func) {
  let index = 0;
  while (index < num) {
    func();
    index++;
  }
}
